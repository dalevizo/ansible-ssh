import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ansible-ssh',  
     version='0.8',
     scripts=['ansible-ssh'] ,
     author="Dimos Alevizos",
     author_email="dimos@alevizos.gr",
     description="Interactive SSH for Ansible",
     long_description=long_description,
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
