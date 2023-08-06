from distutils.core import setup

setup(
    name='marsha',
    version='0.2.2',
    packages=['marsha', 'marsha.formats'],
    license='MIT',
    url='https://gitlab.com/deckar01/marsha',
    author='Jared Deckard',
    author_email='jared@shademaps.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
