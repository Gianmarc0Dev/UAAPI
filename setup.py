from setuptools import setup

setup(
    # Needed to silence warnings
    name='UAAPI',
    url='https://github.com/Gianmarc0Dev/UAAPI',
    author='Gianmarco',
    author_email='worldwideoutlander@gmai.com',
    # Needed to actually package something
    packages=['UAAPI'],
    # Needed for dependencies
    install_requires=[''],
    # *strongly* suggested for sharing
    version='1.0',
    license='MIT',
    description='An unoffical amazon API',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.txt').read(),
    # if there are any scripts
    #scripts=['scripts/hello.py'],
)
