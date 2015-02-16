from setuptools import setup, find_packages

VERSION = '2.4.0'

setup(
    name='django-node',
    version=VERSION,
    packages=find_packages(exclude=('test', 'example',)),
    package_data={
        'django_node': [],
    },
    install_requires=[
        'django',
    ],
    description='Bindings and utils for integrating Node.js and NPM into a Django application',
    long_description='Documentation at https://github.com/markfinger/django-node',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/django-node',
)