import aioagi

from setuptools import setup, find_packages

README = open('README.rst').read()


setup(
    name='aioagi',
    version=aioagi.VERSION,
    description='Async agi client/server framework (asyncio)',
    long_description=README,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: AsyncIO',
    ],
    author='Shakurov Vadim Vladimirovich',
    author_email='apelsinsd@gmail.com',
    url='https://gitlab.com/VadimShakurov/aioagi.git',
    license='Apache 2',
    keywords='aiogi asyncio asterisk telephony voip',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'aiohttp>=3.3.0',
    ],
    extras_require={
        'dev': [
            'ipdb',
            'ipython',
        ],
    },
)
