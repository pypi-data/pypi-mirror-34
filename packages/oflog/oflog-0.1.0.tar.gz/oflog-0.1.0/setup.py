import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oflog",
    version="0.1.0",
    author="OpenFin",
    author_email="dev@openfin.co",
    description="CLI for the OpenFin Log Management Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openfin/log-manager-cli",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: Apache Software License"
    ),
    entry_points={
        "console_scripts": ["oflog=log_manager_cli.openfin_log_cli:main"]
    }
)
