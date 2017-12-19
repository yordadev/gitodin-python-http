```//      ____                     __     __     __      _                _        
  //     / __ \  __  __   _____   / /_   / /_   / /_    (_)   _____      (_)  ____ 
  //    / /_/ / / / / /  / ___/  / __ \ / __/  / __ \  / /   / ___/     / /  / __ \
  //   / ____/ / /_/ /  (__  )  / / / // /_   / / / / / /   (__  )  _  / /  / /_/ /
  //  /_/      \__,_/  /____/  /_/ /_/ \__/  /_/ /_/ /_/   /____/  (_)/_/   \____/ 
```

# Pushthis Python Package
This is a package made for Python, to interact with the Pushthis RESTful API Network Access Point to send payloads through the network to your client side in real-time! 

# Installing
> coming soon

# How to use
> Define your keys and access point
```python
key = 'key'
secret = 'secret'
accessPointAPI = 'api access point'
accessPointAuth = 'auth access point'
```

> Single Payload Requests
```python
import Pushthis

pushthis = Pushthis(key, secret, accessPointAPI)
pushthis.setChannel('pushthisNetwork')
pushthis.setEvent('demo')

payload = {
    'username' : 'bob dole',
    'message'  : 'omg soo cool!'
}

pushthis.attach(payload)
pushthis.send()
```

> Multi-Payload Requests
```python
import Pushthis

pushthis = Pushthis(key, secret, accessPointAPI)

sendToModerator = {
    'channel' : 'pythonChat',
    'event' : 'incomingReports',
    'data' : {
        'username' : 'bob dole',
        'message'  : 'he trolled me.'
    }
}

sendToChatRooms = {
    'channel': 'pythonChat',
    'event': 'callbackReport',
    'data': {
        'username': 'bob dole',
        'message': 'thanks for your report.'
    }
}
pushthis.add(sendToModerator)
pushthis.add(sendToChatRooms)
pushthis.send()
```

> Authorizing Payload Request
```python
import Pushthis

pushthis = Pushthis(key, secret, accessPointAuth)
pushthis.authorize(boolean, channel, socket_id)
```

# Indepth Documentation
> Documentation for Pushthis.io can be found at https://pushthis.io/documentation

# Contributors & Honorable Mentions
- Devitgg @ https://github.com/devitgg
- Nhalstead @ https://github.com/nhalstead
