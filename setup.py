import setuptools

install_requires='pandas scikit-learn matplotlib numpy statmodels scipy'.split()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dslibs-baosws", # Replace with your own username
    version="0.0.4",
    author="Example Author",
    author_email="baosws@gmail.com",
    description="An unified package that installs and import frequently used data-science packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)