import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kahanit",
    version="0.0.0",
    author="Kahanit",
    author_email="care@kahanit.com",
    description="Kahanit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.kahanit.com/",
    packages=[
        "kahanit"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
