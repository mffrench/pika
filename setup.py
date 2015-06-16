# ***** BEGIN LICENSE BLOCK *****
#
# For copyright and licensing please refer to COPYING.
#
# ***** END LICENSE BLOCK *****
from setuptools import setup
import os

# Conditionally include additional modules for docs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
requirements = list()
if on_rtd:
    requirements.append('tornado')

long_description = ('This is a forked version of Pika which help you tune '
                    'the client properties. '
                    'Pika is a pure-Python implementation of the AMQP 0-9-1 '
                    'protocol that tries to stay fairly independent of the '
                    'underlying network support  library. Pika was developed '
                    'primarily for use with RabbitMQ, but should also work '
                    'with other AMQP 0-9-1 brokers.')

setup(name='epika-python3',
      version='0.9.14',
      description='echinopsii Pika Python AMQP Client Library',
      long_description=long_description,
      author='Tony Garnock-Jones',
      author_email='tonygarnockjones@gmail.com',
      maintainer='Mathilde Ffrench',
      maintainer_email='mathilde.ffrench@echinopsii.net',
      url='https://github.com/echinopsii/net.echinopsii.3rdparty.pika',
      download_url='https://github.com/echinopsii/net.echinopsii.3rdparty.pika/tarball/e-p3-0.9.14',
      packages=['pika', 'pika.adapters'],
      license='MPL v2.0',
      install_requires=requirements,
      package_data={'': ['LICENSE', 'README.md']},
      extras_require={'tornado': ['tornado'],
                      'twisted': ['twisted'],
                      'libev': ['pyev']},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Communications',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Networking'],
      zip_safe=True)
