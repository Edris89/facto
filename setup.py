import setuptools

from custom_imports import Install_server
from custom_imports import Update_server
from custom_imports import Remove_server
from custom_imports import scrape_website


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='factocli',  
    version='0.3.5',
    scripts=['factocli'] ,
    author="Edris Keyam",
    author_email="edriskeyam82@hotmail.com",
    description="A Cli for managing a Factorio Headless Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Edris89/facto",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["PyInquirer", "wget", "termcolor", "bs4","psutil"],
 )


