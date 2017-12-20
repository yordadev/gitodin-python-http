##      ____                     __     __     __      _                _
##     / __ \  __  __   _____   / /_   / /_   / /_    (_)   _____      (_)  ____
##    / /_/ / / / / /  / ___/  / __ \ / __/  / __ \  / /   / ___/     / /  / __ \
##   / ____/ / /_/ /  (__  )  / / / // /_   / / / / / /   (__  )  _  / /  / /_/ /
##  /_/      \__,_/  /____/  /_/ /_/ \__/  /_/ /_/ /_/   /____/  (_)/_/   \____/

from __future__ import print_function

import json

import requests


class Pushthis:
    def __init__(self, key, secret, accessPoint):
        self.key = key
        self.secret = secret
        self.access_point = accessPoint
        self.payload_queue = []

    def set_channel(self, channel):
        # type: (str) -> None
        """
        Set the channel.

        :param channel:
        :return:
        """

        self.channel = channel

    def event(self, event):
        # type: (str) -> None
        """
        Set the event.

        :param event:
        :return:
        """

        self.event = event

    def attach(self, data):
        # type: (str) -> None
        """
        Set the data.

        :param data:
        :return:
        """

        self.insert_data = data

    def add(self, payload):
        # type: (dict[str]) -> None
        """
        Add payload to queue.

        :param payload:
        :return:
        """

        self.payload_queue.append(payload)

    def send(self):
        # type: () -> None
        """
        Send the payload to the API.

        :return:
        """

        # check if payloads in queue
        if len(self.payload_queue) != 0:
            # Create Payload Build - Multi-Payload
            print('Multi Request')
            payload = {
                'secret': self.secret,
                'key': self.key,
                'payload': self.payload_queue
            }

            headers = {'content-type': 'application/json'}
            response = requests.post(self.access_point, data=json.dumps(payload), headers=headers)
            print(response)

        else:
            # Create Payload Build - Single Payload
            print('Single Request')
            payload = {
                'secret': self.secret,
                'key': self.key,
                'payload': {
                    'channel': self.channel,
                    'event': self.event,
                    'data': self.insert_data
                }
            }

            headers = {'content-type': 'application/json'}
            response = requests.post(self.access_point, data=json.dumps(payload), headers=headers)
            print(response)

    def authorize(self, status, channel, socket_id):
        # type: (bool, str, str) -> None
        """
        Authorize a payload.

        :param status:
        :param channel:
        :param socket_id:
        :return:
        """
        
        # Create Authorize Payload Build
        print('Authorizing Request')
        payload = {
            'secret': self.secret,
            'key': self.key,
            'payload': {
                'channel': channel,
                'authorized': status,
                'socket_id': socket_id
            }
        }

        headers = {'content-type': 'application/json'}
        response = requests.post(self.access_point, data=json.dumps(payload), headers=headers)
        print(response)
