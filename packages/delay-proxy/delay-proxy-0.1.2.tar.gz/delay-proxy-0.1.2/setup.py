from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='delay-proxy',
    version='0.1.2',
    packages=find_packages(),
    url='https://github.com/maribelacosta/delay-proxy',
    license='Apache 2',
    author='Maribel Acosta',
    author_email='maribel.acosta@kit.edu',
    description='An HTTP proxy that introduces network delays to the response from the server',
    long_description=read('README.md'),
    classifiers=("License :: OSI Approved :: Apache Software License", "Topic :: System :: Networking"),
    scripts=['bin/run-delay-proxy']
)
