##      ____                     __     __     __      _                _
##     / __ \  __  __   _____   / /_   / /_   / /_    (_)   _____      (_)  ____
##    / /_/ / / / / /  / ___/  / __ \ / __/  / __ \  / /   / ___/     / /  / __ \
##   / ____/ / /_/ /  (__  )  / / / // /_   / / / / / /   (__  )  _  / /  / /_/ /
##  /_/      \__,_/  /____/  /_/ /_/ \__/  /_/ /_/ /_/   /____/  (_)/_/   \____/

import requests
import json

class Pushthis:

    ## create instance of object ##
    def __init__(self, key, secret, accessPoint):
        self.setKey = key
        self.setSecret = secret
        self.setAccessPoint = accessPoint
        self.payloadQueue = []

    ## set the channel ##
    def setChannel(self, channel):
        self.setChannel = channel

    ## set the event ##
    def setEvent(self, event):
        self.setEvent = event

    ## set the data
    def attach(self, data):
        self.insertData = data

    ## Add payload to queue ##
    def add(self, payload):
        self.payloadQueue.append(payload)

    ## Send Payload to RESTful API ##
    def send(self):
            ## check if payloads in queue
            if len(self.payloadQueue) != 0:
                ## Create Payload Build - Multi-Payload
                print('Multi Request')
                payload = {
                    'secret': self.setSecret,
                    'key': self.setKey,
                    'payload': self.payloadQueue
                }
                
                headers = {'content-type': 'application/json'}
                response = requests.post(self.setAccessPoint, data=json.dumps(payload), headers=headers)
                print(response)

            else:
                ## Create Payload Build - Single Payload
                print('Single Request')
                payload = {
                    'secret': self.setSecret,
                    'key': self.setKey,
                    'payload': {
                        'channel': self.setChannel,
                        'event': self.setEvent,
                        'data': self.insertData
                    }
                }

                headers = {'content-type': 'application/json'}
                response = requests.post(self.setAccessPoint, data=json.dumps(payload), headers=headers)
                print(response)

    def authorize(self, status, channel, socket_id):
                ## Create Authorize Payload Build
                print('Authorizing Request')
                payload = {
                    'secret': self.setSecret,
                    'key': self.setKey,
                    'payload': {
                        'channel': channel,
                        'authorized': status,
                        'socket_id': socket_id
                    }
                }

                headers = {'content-type': 'application/json'}
                response = requests.post(self.setAccessPoint, data=json.dumps(payload), headers=headers)
                print(response)
