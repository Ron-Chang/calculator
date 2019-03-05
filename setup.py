# python3 setup.py py2app

from setuptools import setup
OPTIONS= {
    'iconfile':'icon_calculator.icns',
}


setup(
    app=["main.py"],
    setup_requires=["py2app"],
    )
