from setuptools import setup
from anotherpdfmerger.version import DESCRIPTION, NAME, VERSION


# Parse readme to include in PyPI page
with open('README.md') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION.capitalize(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mwiens91/anotherpdfmerger',
    author='Matt Wiens',
    author_email='mwiens91@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
    ],
    data_files=[('/usr/local/man/man1', ['anotherpdfmerger.1']),],
    packages=['anotherpdfmerger'],
    entry_points={
        'console_scripts': ['anotherpdfmerger = anotherpdfmerger.anotherpdfmerger:main'],
    },
    install_requires=[
        'PyPDF2',
    ],
)
