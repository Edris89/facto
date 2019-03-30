import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='facto',  
     version='0.1',
     scripts=['facto'] ,
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
 )


 