import os
from setuptools import setup, find_packages
from wagtailmenus import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="wagtailmenus",
    version=__version__,
    author="Mikael Dunhem",
    author_email="mikael.dunhem@gmail.com",
    description=(
        "Allows for easier inclusion of menus in your Wagtail project"
    ),
    long_description=README,
    packages=find_packages(),
    license="MIT",
    keywords="wagtail cms model utility",
    download_url="https://github.com/mdunhem/wagailmenus/tarball/0.1",
    url="https://github.com/mdunhem/wagailmenus",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "Django>=1.9,<1.10",
        "wagtail>=1.3.1",
    ],
)
