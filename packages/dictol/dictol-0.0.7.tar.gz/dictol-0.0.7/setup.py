from __future__ import print_function
import setuptools
import re

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

# with open("README.md", "r") as fh:
#     long_description = fh.read()
def find_version(filename):
    """
    Search for assignment of __version__ string in given file and
    return what it is assigned to.
    """
    with open(filename, 'r') as filep:
        version_file = filep.read()
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

print(find_version('dictol/__init__.py'))

setuptools.setup(
    include_package_data=True,
    name="dictol",
    version= find_version('dictol/__init__.py'),
    author="Tiep Vu",
    author_email="vuhuutiep@gmail.com",
    description="A dictionary learning package for classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiepvupsu/dictol_python",
    packages=['dictol'],
    package_dir = {'dictol': 'dictol'},
    parkage_data={'dictol':['data/*.mat']},
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
