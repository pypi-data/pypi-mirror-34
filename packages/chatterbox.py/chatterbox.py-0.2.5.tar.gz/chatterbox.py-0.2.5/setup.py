import os
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command


if sys.version_info < (3, 4):
    sys.exit('Python < 3.4 is not supported')


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as fp:
        long_description = '\n' + fp.read()

VERSION = '0.2.5'


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel'.format(
            sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(VERSION))
        os.system('git push --tags')

        sys.exit()


setup(
    name='chatterbox.py',
    version=VERSION,
    description='Python library for Kakaotalk chatbot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='JungWinter',
    author_email='wintermy201@gmail.com',
    url='https://github.com/JungWinter/chatterbox',
    packages=find_packages(exclude=('tests', 'examples')),
    py_modules=['chatterbox'],
    install_requires=[],
    tests_require=['pytest', 'pylint', 'tox', 'pytest-cov'],
    include_package_data=True,
    license='MIT',
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Korean',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
