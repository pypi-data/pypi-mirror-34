import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kundjanasith",
    version="0.0.1",
    author="Kundjanasith Thonglek",
    author_email="kundjanasith.t@ku.th",
    description="Kndjanasith's package",
    long_description="K U N D J A N A S I T H",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
