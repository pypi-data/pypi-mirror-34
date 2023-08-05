from setuptools import setup, find_packages

config = {
    'name': 'productstatus-client',
    'description': 'Productstatus REST API client',
    'author': 'MET Norway',
    'url': 'https://github.com/metno/python-productstatus-client',
    'download_url': 'https://github.com/metno/python-productstatus-client',
    'version': '6.5.0',
    'install_requires': [
        'nose==1.3.7',
        'requests==2.9.1',
        'python-dateutil==2.5.0',
        'httmock==1.2.4',
        'kafka-python==1.4.2',
        'mock==2.0.0',
    ],
    'packages': find_packages(),
    'scripts': [],
}

setup(**config)
