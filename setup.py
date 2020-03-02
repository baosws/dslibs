import setuptools

install_requires='pandas scikit-learn matplotlib numpy statsmodels scipy seaborn'.split()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dslibs-baosws", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="baosws@gmail.com",
    description="A unified module of frequently used data-science modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baosws/dslibs/",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
