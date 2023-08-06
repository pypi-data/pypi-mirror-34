import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cs200",
    version="0.4.2",
    packages=["cs200"],
    author="Joshua Segal",
    author_email="gitpulljoshuasegal@gmail.com",
    description="A SIMPLE package for simplifying concepts available on wikipedia.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dev-segal/cs200",
    install_requires = [
        "flask"
        ],
    scripts=["cs200/bin/cs200"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
