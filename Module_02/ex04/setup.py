from setuptools import setup

setup(
    name='my_minipack',
    version='1.0.0',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
)
