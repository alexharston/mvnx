from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as rm:
    long_description = rm.read()

setup(
    name="mvnx", 
    version="0.1.17",
    author="Alex Harston",
    author_email="alex@harston.io",
    description="A lightweight commandline parser for the MVNX motion capture file format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexharston/mvnx",
    license="MIT",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=['numpy', 'argparse'],
)
