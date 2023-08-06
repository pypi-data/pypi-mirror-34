# https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pypyorm",
    version="0.1.1",
    author="dotcoo",
    author_email="dotcoo@163.com",
    description="Easy ORM package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dotcoo/pypyorm",
    packages=setuptools.find_packages(),
    install_requires = ["pymysql"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)