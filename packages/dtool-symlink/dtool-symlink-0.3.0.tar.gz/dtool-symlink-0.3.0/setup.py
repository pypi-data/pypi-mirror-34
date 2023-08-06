from setuptools import setup

url = "https://github.com/jic-dtool/dtool-symlink"
version = "0.3.0"
readme = open('README.rst').read()

setup(
    name="dtool-symlink",
    packages=["dtool_symlink"],
    version=version,
    description="Create dataset where data directory is a symlink",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[
        "dtoolcore>=3.4",
    ],
    entry_points={
        "dtool.storage_brokers": [
            "SymLinkStorageBroker=dtool_symlink.storagebroker:SymLinkStorageBroker",  # NOQA
        ],
    },
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
