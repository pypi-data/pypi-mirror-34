import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="byteArk",
    version="0.0.10",
    author="Kundjanasith Thonglek",
    author_email="kundjanasith.t@ku.th",
    description="Kundjanasith's package",
    long_description="B Y T E A R K",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
