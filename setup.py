import setuptools
import scripts.main

INSTALL_REQUIRES = ['pytest==5.4.3']

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scripts",
    version="0.0.2",
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
    install_requires=INSTALL_REQUIRES,
    entry_points = {
        'console_scripts': ['runtests=scripts.main:main'],
    }
)