from twitch.api.base import TwitchAPI
from twitch.exceptions import TwitchAttributeException
from twitch.resources import Team


class Teams(TwitchAPI):
    async def get(self, team_name):
        response = await self._request_get("teams/{}".format(team_name))
        return Team.construct_from(response)

    async def get_all(self, limit=10, offset=0):
        if limit > 100:
            raise TwitchAttributeException(
                "Maximum number of objects returned in one request is 100"
            )

        params = {"limit": limit, "offset": offset}
        response = await self._request_get("teams", params=params)
        return [Team.construct_from(x) for x in response["teams"]]
