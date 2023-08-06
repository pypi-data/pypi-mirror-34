import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="timestamps",
    version="1.0.0",
    author="GHOUL Nadir",
    author_email="gndu91@gmail.com",
    description="Timestamp manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gndu91/timestamps",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
