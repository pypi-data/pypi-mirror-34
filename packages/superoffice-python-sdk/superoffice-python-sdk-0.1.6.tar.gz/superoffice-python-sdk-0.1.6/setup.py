try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

long_description = '''
SuperOffice Rest API Python SDK
'''

setup(
    name='superoffice-python-sdk',
    version='0.1.6',
    author='Ignotas Petrulis',
    author_email='ignotas.petrulis@gmail.com',
    packages=['superofficesdk'],
    data_files=[('', ['superofficesdk/partner.wsdl'])],
    install_requires=[
        'requests'
    ],
    description='SuperOffice Python SDK',
    long_description=long_description
)
