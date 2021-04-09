#!/usr/bin/env python3
import requests
from flask import Flask, Response
from flask_restful import Resource, Api, abort

from .constants import DISCORD_WIDGET_URI

app = Flask(__name__)
api = Api(app)


class DiscordUserDownDetector(Resource):
    def get(self, guild_id: int, username: str):
        guild_widget_response = requests.get(DISCORD_WIDGET_URI.format(guild_id))
        if guild_widget_response.status_code == requests.codes.not_found:
            return abort(http_status_code=requests.codes.not_found, message=f'Guild {guild_id} does not exist')

        guild_member = next((item for item in guild_widget_response.json()['members'] if item['username'] == username), None)
        if guild_member is None:
            return abort(http_status_code=requests.codes.not_found,
                         message=f'{username} is not a member of guild {guild_id} or is offline')

        return {'status': guild_member['status']}


@app.errorhandler(404)
def not_found_handler(e) -> Response:
    return Response(status=404)


api.add_resource(DiscordUserDownDetector, '/guild/<int:guild_id>/username/<string:username>')

if __name__ == '__main__':
    app.run()