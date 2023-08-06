# Copyright (C) 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPL v2


from setuptools import setup

setup(
    name='fsdiff',
    version='0.1.post1',
    description='Byte to byte comparison of local disk images or filesystems',
    author='Team Kano',
    author_email='dev@kano.me',
    url='https://github.com/KanoComputing/fsdiff',
    packages=['fsdiff'],
    scripts=['bin/fsdiff']
)
