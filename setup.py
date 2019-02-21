import setuptools

setuptools.setup(
    name='samfeng279-test',
    version='0.1',
    author="Sam Feng",
    author_email="samfeng279@gmail.com",
    description="Testing for deployment of Python packages",
    url="https://github.com/s38feng/dea-extractor-public",
    packages=['package'],
    install_requires=[
        'pandas',
        'cognite-sdk'
    ],
    scripts=['package/test.py'],
 )
