import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pfw",
    version="0.0.1",
    author="Eraple",
    author_email="care@eraple.com",
    description="Eraple PFW(Python Framework)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.eraple.com/",
    packages=[
        "pfw"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
