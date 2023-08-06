from setuptools import setup, find_packages

setup(
    name='shortesttrack-sdk',
    version='0.0.4',
    description='SDK for work with ShortestTrack API',
    packages=find_packages(),
    install_requires=['urlobject', 'requests'],
    author='Stanislav Pospelov',
    author_email='stpospelov@shtr.io',
    license='MIT'
)

