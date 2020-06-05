import setuptools
import foo.main

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="foo",
    version="0.0.1",
    author="Alexandru Pavilcu",
    author_email="alexandrupavilcu@gmail.com",
    description="A small test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': ['main=foo.main:main'],
    }
)