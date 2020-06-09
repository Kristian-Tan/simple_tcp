import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='simple_tcp',
     version='0.5',
     author="Kristian Tanuwijaya",
     author_email="tanuwijaya.kristian@gmail.com",
     description="A simple TCP client and server for easy testing",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitlab.com/kristiant/simple_tcp",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
