from setuptools import setup, find_packages

from pya import VERSION

install_requires = [
    'mysql-python',
    'lxml==2.3.6',
    'PyQuery',
    'Pillow',
    'gunicorn',
    'django==1.8',
    'django-celery',
    'django-crispy-forms',
    'django-reversion',
    'git+git://github.com/fxiao/DjangoUeditor',
    'xlwt',
    'xlsxwriter',
    'python-memcached',
    'python-binary-memcached',
    'django-bmemcached',
]

setup(
    name = 'django-pya',
    version = VERSION,
    license = 'LGPL v3.0',
    description = 'A Django APP for cart',
    long_description = open('README.md').read(),
    author = 'Fxiao',
    author_email = 'heyun51@gmail.com',
    url = 'https://github.com/fxiao/py-a',
    keywords = 'django, cart, weixin',
    packages = find_packages(exclude=('example',)),
    install_requires = install_requires,
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Dev',
        'Topic :: Internet',
        'License :: OSI Approved :: LGPL v3.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
