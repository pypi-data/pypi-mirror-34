from kadal.query import MEDIA_SEARCH, MEDIA_BY_ID, MEDIA_PAGED
from kadal.media import Media

URL = 'https://graphql.anilist.co'


class KadalError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status


class MediaNotFound(KadalError):
    pass


class Client:
    def __init__(self, session=None, *, lib='asyncio', loop=None):
        if lib not in ('asyncio', 'multio'):
            raise ValueError("lib must be of type `str` and be either `asyncio` or `multio`, "
                             "not `{}`".format(lib if isinstance(lib, str) else lib.__class__.__name__))
        self._lib = lib
        if lib == 'asyncio':
            import asyncio
            loop = loop or asyncio.get_event_loop()
        self.session = session or self._make_session(lib, loop)

    @staticmethod
    def _make_session(lib, loop=None):
        if lib == 'asyncio':
            try:
                import aiohttp
            except ImportError:
                raise ImportError("To use Kadal in asyncio mode, it requires the `aiohttp` module.")
            return aiohttp.ClientSession(loop=loop)
        try:
            import asks
        except ImportError:
            raise ImportError("To use Kadal in curio/trio mode, it requires the `asks` module.")
        return asks.Session()

    async def _request(self, query, **variables):
        r = await self.session.post(URL, json={"query": query, "variables": variables})
        if self._lib == 'asyncio':
            data = await r.json()
        else:
            data = r.json()
        if data.get('errors'):
            self.handle_error(data['errors'][0])
        return data

    async def _most_popular(self, query, _type):
        data = await self._request(MEDIA_PAGED, search=query, page=1, perPage=50, type=_type)
        lst = data['data']['Page']['media']
        if not lst:
            raise MediaNotFound("Not Found.", 404)
        return sorted(lst, key=lambda m: m['popularity'], reverse=True)[0]

    @staticmethod
    def handle_error(error):
        msg = error['message']
        status = error['status']
        if status == 404:
            raise MediaNotFound(msg, status)
        else:
            raise KadalError(msg, status)

    async def get_anime(self, id):
        data = await self._request(MEDIA_BY_ID, id=id, type='ANIME')
        return Media(data)

    async def get_manga(self, id):
        data = await self._request(MEDIA_BY_ID, id=id, type='MANGA')
        return Media(data)

    async def search_anime(self, query, *, popularity=False):
        if popularity:
            data = await self._most_popular(query, "ANIME")
        else:
            data = await self._request(MEDIA_SEARCH, search=query, type='ANIME')
        return Media(data, page=popularity)

    async def search_manga(self, query, *, popularity=False):
        if popularity:
            data = await self._most_popular(query, "MANGA")
        else:
            data = await self._request(MEDIA_SEARCH, search=query, type='MANGA')
        return Media(data, page=popularity)
