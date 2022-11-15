from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='helloworldfromodou',
    version='0.0.1',
    description='Say Hello world',
    py_modules=["helloworldfromodou"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Licence :: OSI Approved :: GNU General Public Licence v2 or later(GPLv2+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "blessings == 1.7", 
    ],
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    },
     
)