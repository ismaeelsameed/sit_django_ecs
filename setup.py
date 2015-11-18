"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sit=django-ecs',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='A library to interact with amazon ecs containers from a django application',
    long_description=long_description,

    # The project's main homepage.
    url='',

    # Author details
    author='Ismaeel Abu Sameed, Zaid Farekh',
    author_email='i.abusameed@sit-mena.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # What does your project relate to?
    keywords='django ecs amazon-ecs sit sit-django-ecs django-ecs sit-django amazon-containers',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages('django-ecs'),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['Fabric==1.10.2', 'argparse==1.2.1', 'awscli==1.9.6', 'blessings==1.6',
                      'boto3==1.2.1', 'botocore==1.3.6', 'colorama==0.3.3', 'docopt==0.6.2', 'docutils==0.12',
                      'ecdsa==0.13', 'futures==2.2.0', 'jmespath==0.9.0', 'paramiko==1.16.0', 'pyasn1==0.1.9',
                      'pycrypto==2.6.1', 'pyfiglet==0.7.3', 'python-dateutil==2.4.2', 'rsa==3.2.3', 'six==1.10.0',
                      'termcolor==1.1.0', 'wsgiref==0.1.2'],

    # put your pem key in this path
    data_files=[('my_data', ['data/key.pem'])],
)
