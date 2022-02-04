from setuptools import setup

setup(
    name='most_active_cookie',
    version='0.0.0',
    packages=['most_active_cookie'],
    entry_points={
        'console_scripts': [
            'most_active_cookie = most_active_cookie.__main__:main'
        ]
    })
