import re
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os

readme = os.path.join(os.path.dirname(__file__), 'README.rst')
LONG_DESCRIPTION = open(readme).read()


def read_module_contents():
    with open('helga_productpages/__init__.py') as init:
        return init.read()


module_file = read_module_contents()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", module_file))
version = metadata['version']


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main('helga_productpages/tests', self.pytest_args)
        sys.exit(errno)


setup(name="helga-productpages",
      version=version,
      description='Red Hat Product Pages plugin for Helga',
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Intended Audience :: Developers',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   'Topic :: Software Development',
                   ],
      keywords='irc bot productpages',
      author='ken dreyer',
      author_email='ktdreyer@ktdreyer.com',
      url='https://github.com/ktdreyer/helga-productpages',
      license='MIT',
      long_description=LONG_DESCRIPTION,
      packages=find_packages(),
      install_requires=[
          'helga',
          'rhcalendar',
          'txproductpages',
      ],
      tests_require=[
          'pytest',
      ],
      entry_points=dict(
          helga_plugins=[
              'productpages = helga_productpages:helga_productpages',
          ],
      ),
      cmdclass={'test': PyTest},
)
