import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jlv",
    version="0.0.2",
    author="Stel Drake",
    author_email="stelabr2@gmail.com",
    description="A simple command line journal tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stelabr/jlv",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": [
            "jlv = jlv:main"
        ]
    }
)
