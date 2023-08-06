import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ecp",
    version="0.0.0",
    author="Eraple",
    author_email="care@eraple.com",
    description="Eraple ECP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.eraple.com/",
    packages=[
        "ecp"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
