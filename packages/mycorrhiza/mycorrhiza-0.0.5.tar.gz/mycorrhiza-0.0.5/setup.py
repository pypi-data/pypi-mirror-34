import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mycorrhiza",
    version="0.0.5",
    author="Jeremy Georges-Filteau",
    author_email="jeremy.georges-filteau@mail.mcgill.ca",
    description="Mycorrhiza population assignment tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jgeofil/mycorrhiza",
    packages=setuptools.find_packages(),
    install_requires=[
        'tqdm',
        'numpy',
        'scikit-learn',
        'pathos',
        'matplotlib'
    ],
    python_requires='>=3',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
)