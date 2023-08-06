from setuptools import setup, find_packages
import os

ROOT = os.path.dirname(os.path.realpath(__file__))

setup(
    name = 'weblib',
    version = '0.1.30',
    description = 'Set of tools for web scraping projects',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    author = 'Gregory Petukhov',
    author_email = 'lorien@lorien.name',
    install_requires = [
        'pytils',
        'six',
        'user_agent',
    ],
    extras_require={
        'full': [
            'feedparser',
            'selenium',
        ],
        'full:platform_system!="Windows"': ['lxml'],
    },
    packages = find_packages(exclude=['test']),
    license = "MIT",
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
