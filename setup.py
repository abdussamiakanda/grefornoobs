import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="grefornoobs",
    version="1.0.0",
    description="Your python GRE preparation tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/abdussamiakanda/grefornoobs",
    author="Md. Abdus Sami Akanda",
    author_email="abdussamiakanda@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["gre"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "gre=gre.__main__:main",
        ]
    },
)