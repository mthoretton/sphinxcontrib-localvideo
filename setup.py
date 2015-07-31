# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('./README.rst') as stream:
  long_desc = stream.read()

requires = ['Sphinx>=1.0.5']

setup(
    name='sphinxcontrib-localvideo',
    version='0.1',
    url='http://packages.python.org/sphinxcontrib-localvideo',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-localvideo',
    license='LGPL',
    author='C. Brun',
    author_email='christophe.brun.cl194@gadz.org',
    description='Include HTML5 webm videos in html output',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    test_suite= 'nose.collector'
)
