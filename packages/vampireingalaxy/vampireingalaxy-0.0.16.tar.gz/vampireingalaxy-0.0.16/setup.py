import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vampireingalaxy",
    version="0.0.16",
    author="Kyu Sang Han",
    author_email="khan21@jhu.edu",
    description="Vampire Image Analysis Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://wirtzlab.johnshopkins.edu",
    packages=setuptools.find_packages(),
    install_requires=[
        'scipy',
        'pandas',
        'numpy',
        'pillow',
        'matplotlib',
        'scikit-learn',
        'imageio',
        #'opencv'
    ],
    scripts=['bin/vampire-run.py','bin/sort-run.py','bin/analysis-run.py'],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
    ),
)