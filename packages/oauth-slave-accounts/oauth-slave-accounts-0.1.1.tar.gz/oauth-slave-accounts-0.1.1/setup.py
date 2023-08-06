import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name="oauth-slave-accounts",
        packages=find_packages(),
        include_package_data=True,
        license='BSD License',  # example license
        description='Custom Django Oauth backend for Ressource Servers to download full user data fom Authorization Server',
        long_description=README,
        author='Jean Ribes',
        author_email='jean@ribes.me',
        install_requires=[
            'requests',
            'django-oauth-toolkit',
        ],
        classifiers=[
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
        version='0.1.1'
)