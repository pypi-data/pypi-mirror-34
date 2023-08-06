import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="web_scraper",
    version="1.0",
    author="Vahid Vaezian",
    author_email="vahid.vaezian@gmail.com",
    description="A package for getting data from the intenet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vvaezian/Web-Scraper",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
