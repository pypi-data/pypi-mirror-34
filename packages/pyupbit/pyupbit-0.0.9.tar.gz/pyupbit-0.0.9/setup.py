from setuptools import setup

setup(
    name            = 'pyupbit',
    version         = '0.0.9',
    description     = 'python wrapper for Upbit API',
    url             = 'https://github.com/sharebook-kr/pyupbit',
    author          = 'Lukas Yoo, Brayden Jo',
    author_email    = 'jonghun.yoo@outlook.com, pystock@outlook.com',
    install_requires=['requests'],
    license         = 'MIT',
    packages        = ['pyupbit'],
    zip_safe        = False
)