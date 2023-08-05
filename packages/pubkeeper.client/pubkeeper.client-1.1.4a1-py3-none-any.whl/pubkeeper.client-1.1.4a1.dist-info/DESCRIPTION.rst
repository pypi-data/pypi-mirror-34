# Pubkeeper Python Client

The Pubkeeper Python Client enables you to connect to a Pubkeeper Server and to participate in the production and subscription of data topics.

## Quick Start

### Install for Use
### Requirements

The Python Pubkeeper client requires Python version 3.5 or higher


#### Install

Into your environment install the wheel files together:

```
pip3 install pubkeeper.client
```

### Install for Development
#### Clone the repo

If you have access to the Pubkeeper project you may install directly from source for development purposes.

```
git clone git@github.com:pubkeeper/python-client
```

#### Install

Ensure the protocol, and communicaiton wheels are installed into your environment before installing the Pubkeeper Python Client and Brews.  Then you can install Pubkeeper Python Client and Brews into your own virtualenv.

```
pip3 install -e /path/to/where/you/cloned/python-client
```

### Using the Pubkeeper Python Client
#### Authentication Tokens

Pubkeeper Server handles client authentication with JWT.  As such you will need to acquire a token from the server you are going to be connecting to.

#### Running

In the most basic example, we will connect to the Pubkeeper Server, and register a single Brewer and publish a string.  Note that the client sits upon a Tornado IOLoop, as such it runs inside of its own thread, and will need to be gracefilly shutdown when your program ends.  This example assumes you are running an unsecured Pubkeeper Server, and Websocket Server on your localhost.  You will need to replace these with actual values.

```py
from pubkeeper.client import PubkeeperClient
from pubkeeper.brew.websocket.brew import WebsocketBrew
from time import sleep

config = {
    'host': 'localhost',
    'port': 9898,
    'secure': False
    'token': 'your-auth-token',
    'bridge_mode': False
}
client = PubkeeperClient(config)

websocket_brew = WebsocketBrew()
websocket_brew.configure({
    'ws_host': 'localhost',
    'ws_port': 8000,
    'ws_secure': False
})

client.add_brew(websocket_brew)
client.start()

try:
    brewer = client.add_brewer('demo.topic')

    while True:
        brewer.brew(b'data')
        sleep(1)
except KeyboardInterrupt:
    client.shutdown()
```

## Complete Documentation

A more complete documentation of the Pubkeeper Python Client, and Pubkeeper System may be found at: [docs.pubkeeper.com](http://docs.pubkeeper.com)

# License
This software is proprietary and may only be used in conjunction with a current niolabs plan and the associated nio software license.  See [https://niolabs.com/pricing](https://niolabs.com/pricing) for available plans.


