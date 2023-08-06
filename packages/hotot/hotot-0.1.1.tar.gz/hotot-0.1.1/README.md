# Hotot: RabbitMQ Python client

**Hotot** is a thin wrapper around Pika to provide clients that handles connection, publish and receive operations on RabbitMQ without any hassle.

This package is named after the *(cute)* french rabbit [Blanc de Hotot](https://en.wikipedia.org/wiki/Blanc_de_Hotot).

## How to use

```
pip install hotot
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

with RpcClient(host='localhost', exchange = '', header = {}, timeout=60, connection_attempts=100) as client:
    # exchange is the exchange where the message will be sent
    # header is an optional dict that will be added to the body
    # timeout is the number of seconds before a call() is considered closed
    # connection_attempts is the number of connexions retries to the host before aborting
```

The RabbitMQ messages will be sent and received with an `application/json` content type


## Release & Development version

Each release is automatically uploaded to [PyPI](https://pypi.org/project/hotot/#history) for every tagged commit. The tag version must be compliant with the [PEP400](https://www.python.org/dev/peps/pep-0440/), and have been already used for any previous (even deleted) release.

To try the package deployement without publishing on PyPI, you can push the build on [the test version of PyPI](https://test.pypi.org/project/hotot) and create a virtualenv to try to the download and installation of the new version with those commands:

```
pip install twine
VERSION=1.0 python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
virtualenv py3
source py3/bin/activate
pip install --extra-index-url https://test.pypi.org/simple hotot==1.0-dev
```

You need to specify a version number (with `$VERSION`) that hasn't been already used for any previous (even deleted) release. A `dev` will be automatically appended to the version number.

# Test suite

A test suite is available in `tests/` folder. Every new commit to the repo will automatically trigger a new test suite execution with the results available [here](https://gitlab.lancey.fr/nuage/hotot/pipelines). Every new or modified feature to Hotot should add or modify related tests accordingly. A new release will be only deployed if the test suite status is green.

The suite uses [pytest](https://docs.pytest.org/en/latest/) as its main framework. If you want to launch the test suite locally, you can use:

```
pip install pytest
docker run -p 5672:5672 -p 15672:15672 -d rabbitmq:3.7-rc-management
python setup.py test
```