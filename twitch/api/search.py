from twitch.api.base import TwitchAPI
from twitch.exceptions import TwitchAttributeException
from twitch.resources import Channel, Game, Stream


class Search(TwitchAPI):
    async def channels(self, query, limit=25, offset=0):
        if limit > 100:
            raise TwitchAttributeException(
                "Maximum number of objects returned in one request is 100"
            )

        params = {"query": query, "limit": limit, "offset": offset}
        response = await self._request_get("search/channels", params=params)
        return [Channel.construct_from(x) for x in response["channels"] or []]

    async def games(self, query, live=False):
        params = {
            "query": query,
            "live": live,
        }
        response = await self._request_get("search/games", params=params)
        return [Game.construct_from(x) for x in response["games"] or []]

    async def streams(self, query, limit=25, offset=0, hls=None):
        if limit > 100:
            raise TwitchAttributeException(
                "Maximum number of objects returned in one request is 100"
            )

        params = {"query": query, "limit": limit, "offset": offset, "hls": hls}
        response = await self._request_get("search/streams", params=params)
        return [Stream.construct_from(x) for x in response["streams"] or []]
