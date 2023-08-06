# Hotot: RabbitMQ/Requests Python client

**Hotot** is a thin wrapper around [Pika](https://github.com/pika/pika) and [requests](http://docs.python-requests.org/en/master/) to provide: 
* clients that handles connection, publish and receive operations on RabbitMQ without any hassle.
* functions to simplify API calls

Each *service* from the [backend](https://gitlab.lancey.fr/nuage/backend) should use this package to make (a)synchronous requests to internals APIs or brokers.

This package is named after the *(cute)* french rabbit [Blanc de Hotot](https://en.wikipedia.org/wiki/Blanc_de_Hotot).

## How to use


### Installation

Install it with [pip](https://pypi.org/project/pip/). Add `hotot` to your [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#id1) if needed. As easy as pie! 🥧

```
pip install hotot
```


### API calls

With the function `api`, you can construct a new single function to call your API with the right endpoint parameters. The function assumes that the response can be parsed as a JSON object and will be returned as such. If the request has failed for any reason, the function will return `None`.

``` python
from hotot import api

os.environ['API_ENDPOINT'] = 'localhost'
os.environ['API_PORT'] = '5000'

# api() can detect environment variables 
# or directly uses variables, strings, ints,...
db_api = api('API_ENDPOINT', 'API_PORT')
# is equivalent to
db_api = api('localhost', 5000)

# the db_api() function has the same parameters as requests.get()
# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request

# curl -X GET "http://localhost:5000/heaters/" -H  "accept: application/json"
print(db_api('heaters')) 

# curl -X GET "http://localhost:5000/frames/main/0?last=1" -H  "accept: application/json"
print(db_api('frames/main/0', params={'last': 1}))

# By default, the `api` function will provide logging on the standard output to the `ERROR` level. 
# You can provide our own logger using

import logging

logging.basicConfiglevel(level=logging.INFO)
# Only your imagination limits you
logger = logging.getLogger(__name__)

db_api = api.api('localhost', 5000, logger=logger)
# or 
db_api = api.api('localhost', 5000, logger)

```


### RPC client

**RpcClient** is a [Remote Procedure Call](https://www.rabbitmq.com/tutorials/tutorial-six-python.html) client.

``` python
from hotot import RpcClient

with RpcClient('localhost') as client:
    
    # Send a RPC with call()
    response = client.call('rpc_queue', a=1, b=2)
    # which is equivalent to
    body = {'a': 1, 'b': 2}
    response = client.call('rpc_queue', **body)
    
    # The send() will not await any response
    client.send('rpc_queue', a=1)

with RpcClient(host, exchange = '', header = {}, timeout=60, connection_attempts=100) as client:
    # host:     the RabbitMQ endpoint
    # exchange: the exchange where the message will be sent
    # header:   an optional dict that will be added to the body
    # timeout:  the number of seconds before a call() is considered closed
    # connection_attempts: the number of connexions retries to the host before aborting
    pass
```

The RabbitMQ messages will be sent and received with an `application/json` content type.



### Consumer client

**ConsumerClient** is a synchronous [RabbitMQ consumer](https://www.rabbitmq.com/tutorials/tutorial-three-python.html) client, creating a blocking connection to listen to arriving messages on a exchange.

``` python
def callback(ch, method, properties, body):
    ch.basic_ack(method.delivery_tag)
    # Do what you want with the received data...
    pass 

client = ConsumerClient(host, 'consumer-exchange', 'consumer-queue')
client.consume(callback) # Blocking function!


with ConsumerClient(host, exchange='', queue='', routing_key=None, exclusive=False, durable=False, **kwargs) as client:
    # host:         the RabbitMQ endpoint
    # exchange:     the exchange from where the messages are consumed
    # queue:        the queue name where the messages are directed, an empty string will define a random name
    # routing_key:  the binding key between the queue and the exchange
    # exclusive:    a boolean flag to set that no others consumers can be feed from this queue
    # durable:      a boolean flag to set that this queue contents may not be destroyed in case of failure 
    # connection_attempts: the number of connexions retries to the host before aborting   
    client.consume(callback)
```

## Release & Development version

Each release is automatically uploaded to [PyPI](https://pypi.org/project/hotot/#history) for every tagged commit. The tag version must be [PEP400](https://www.python.org/dev/peps/pep-0440/) compliant, and have not been already used for any previous *(even deleted)* release.

To try the package deployement without publishing on PyPI, you can push the build on [the test version of PyPI](https://test.pypi.org/project/hotot) and create a virtualenv to try to the download and installation of the new version:

```
pip install twine
VERSION=1.0 python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
virtualenv py3
source py3/bin/activate
pip install --extra-index-url https://test.pypi.org/simple hotot==1.0-dev
```

With `$VERSION`, you specify a version number (not already used for any previous *- even deleted -* release). A `dev` will be automatically appended to the version number.

# Test suite

A test suite is available in `tests/`. Every new commit to the repo will automatically trigger a new [test suite pipeline](https://gitlab.lancey.fr/nuage/hotot/pipelines). Adding or modifying a *Hotot* feature should add or modify tests. A new release will be only deployed if the pipeline status is green.

The suite uses [pytest](https://docs.pytest.org/en/latest/) as its main framework. If you want to launch the test suite locally, you need to launch our own instance of RabbitMQ before firing up the suite:

```
pip install pytest
docker run -p 5672:5672 -p 15672:15672 -d rabbitmq:3.7-rc-management
python setup.py test
```