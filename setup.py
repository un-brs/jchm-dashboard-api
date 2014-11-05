from setuptools import setup, find_packages
from jchm import __version__

setup(
    name='jchm',
    version=__version__,

    url='http://localhost:8000/',
    author='Alexander Mazurov',
    author_email='alexander.mazurov@gmail.com',

    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/manage.py'],

    install_requires=(
        'django == 1.7',
    )
)

