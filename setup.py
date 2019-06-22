import setuptools

__version__ = '1.0.0'

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="caesar_cmd",
    version=__version__,
    author="Benjamin Soyka",
    description="A Python program to create a caesar cipher interactively or programmatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bsoyka/caesar_cmd",
    keywords=[
        "encryption",
        "security"
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'sentry-sdk==0.9.1'
    ]
    include_package_data=True
]
