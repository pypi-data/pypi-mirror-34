# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['decouple_aws']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.7,<2.0', 'python-decouple>=3.1,<4.0']

setup_kwargs = {
    'name': 'python-decouple-aws',
    'version': '0.2.1',
    'description': 'AWS Extensions for Python Decouple',
    'long_description': None,
    'author': 'Matt Magin',
    'author_email': 'matt.magin@cmv.com.au',
    'url': 'https://github.com/AzMoo/python-decouple-aws',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
