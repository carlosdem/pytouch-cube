"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

import app

APP = ['gui.py']
DATA_FILES = []
OPTIONS = {'iconfile': 'pytouch3.icns'}

setup(
    name=app.APP_NAME,
    version=app.APP_VERSION,
    author=app.APP_AUTHOR,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['barcode', 'PyQt5', 'django-qrcode']
)