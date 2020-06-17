from setuptools import setup


setup(
    name='bitcalc',
    version='0.1',
    py_modules=['bitcalc'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bitcalc=bitcalc:cli
    ''',
)
