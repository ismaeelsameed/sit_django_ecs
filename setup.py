from distutils.core import setup

setup(
    name='sit_django_ecs',
    packages=['sit_django_ecs'],  # this must be the same as the name above
    version='1.0.4',
    description='A library to interact with amazon ecs containers from a django application',
    author='Ismaeel Abu Sameed, Zaid Farekh',
    author_email='i.abusameed@sit-mena.com',
    url='https://github.com/ismaeelsameed/sit-django-ecs',  # use the URL to the github repo
    download_url='https://github.com/ismaeelsameed/sit-django-ecs/archive/master.zip',  # I'll explain this in a second
    keywords='django ecs amazon-ecs sit sit-django-ecs django-ecs sit-django amazon-containers',
    install_requires=['Fabric==1.10.2', 'argparse==1.2.1', 'awscli==1.9.6', 'blessings==1.6',
                      'boto3==1.2.1', 'botocore==1.3.6', 'colorama==0.3.3', 'docopt==0.6.2', 'docutils==0.12',
                      'ecdsa==0.13', 'futures==2.2.0', 'jmespath==0.9.0', 'paramiko==1.16.0', 'pyasn1==0.1.9',
                      'pycrypto==2.6.1', 'pyfiglet==0.7.3', 'python-dateutil==2.4.2', 'rsa==3.2.3', 'six==1.10.0',
                      'termcolor==1.1.0', 'wsgiref==0.1.2'],
    classifiers=[],
)
