import src.pushthis as Please

class Example:

    ## SINGLE PAYLOAD EXAMPLE ##

    ##define these wherever floats your boat
    key = ''
    secret = ''
    accessPointAPI = 'https://na.pushthis.io/api'
    accessPointAuth = 'https://na.pushthis.io/auth'

    ##Create new instance of Pushthis
    pushthis = Please.Pushthis(key, secret, accessPointAPI)

    ##Set the channel and event
    pushthis.setChannel('pushthisNetwork')
    pushthis.setEvent('demo')

    ##Lets build the payload
    payload = {
        'username' : 'bob dole',
        'message'  : 'omg soo cool!'
    }

    #Pass the payload
    pushthis.attach(payload)

    #lets send this off!
    pushthis.send()






    ## MULTI-PAYLOAD EXAMPLE ##

    pushthis = Please.Pushthis(key, secret, accessPointAPI)


    sendToModerator = {
        'channel' : 'pushthisNetwork',
        'event' : 'demo',
        'data' : {
            'username' : 'bob dole',
            'message'  : 'he trolled me.'
        }
    }

    sendToChatRooms = {
        'channel': 'pushthisNetwork',
        'event': 'demo',
        'data': {
            'username': 'bob dole',
            'message': 'thanks for your report.'
        }
    }

    ## lets queue these payloads ##
    pushthis.add(sendToModerator)
    pushthis.add(sendToChatRooms)

    ## lets send the queued payloads
    pushthis.send()




    ## AUTHORIZING PAYLOAD REQUEST ##

    pushthis = Please.Pushthis(key, secret, accessPointAuth)
    # pushthis.authorize(boolean, channel, socket_id) # Example of args
    pushthis.authorize(True, 'python-private-chat-room', '49fjD_damkoij3d')
    pushthis.authorize(False, 'python-private-chat-room', '49fjD_damkoij3d')
