import socket

import requests
from docopt import docopt as docoptinit

register_kong_doc = """
Usage:
    register_kong [options]
    
Options:
    --name=<name>
    --uris=<uris>
    --hosts=<hosts>
    --port=<port>
    --ip=<ip>
    --region=<region>
    --preserve-host
"""


def register_kong(argv):
    timeout = 3
    docopt = docoptinit(register_kong_doc, argv)
    print(docopt)
    name = docopt['--name']
    uris = docopt['--uris']
    port = docopt['--port']
    hosts = docopt['--hosts']
    region = docopt['--region']
    preserve = docopt['--preserve-host']
    if region == 'alihz':
        url = 'http://alihz-master.qbtrade.org:8001/apis'
    elif region == 'alihk-stage':
        url = 'http://alihk-stage-0.qbtrade.org:8001/apis'
    else:
        url = 'http://kong-admin.qbtrade.org/apis'
    if not docopt['--ip']:
        ip = socket.gethostbyname(socket.gethostname())
    else:
        ip = docopt['--ip']
    r = requests.delete('{url}/{name}'.format(url=url, name=name), timeout=timeout)
    print('delete', r.text)
    data = {'name': name,
            'upstream_url': 'http://{}:{}'.format(ip, port),
            }

    if hosts:
        data['hosts'] = hosts
    if uris:
        data['uris'] = uris
        data['strip_uri'] = 'true'
    if preserve:
        data['preserve_host'] = 'true'

    print(data)
    r = requests.post(url, data=data, timeout=timeout)
    print('add', r.text)
    print('register ip', ip)


if __name__ == '__main__':
    # register_kong(['--name', 'pytest', '--ip', '1.2.3.4', '--uris', '/pytest', '--port', '8080'])
    register_kong(['--name', 'pytest', '--ip', '1.2.3.4', '--hosts', 'pytest.qbtrade.org', '--port', '8080'])
