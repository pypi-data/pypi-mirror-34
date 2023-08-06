import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rijksdriehoek",
    version="0.0.1",
    author="flimpie",
    author_email="python-packaging@hillebrand.io",
    description="A Rijksdriehoek (EPSG:28992) to WGS'84 conversion utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitea.hillebrand.io/Flippylosaurus/python-rijksdriehoek",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
