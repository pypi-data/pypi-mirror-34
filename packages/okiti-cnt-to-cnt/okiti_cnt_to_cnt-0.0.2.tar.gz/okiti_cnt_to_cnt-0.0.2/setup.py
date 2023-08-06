import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="okiti_cnt_to_cnt",
    version="0.0.2",
    author="bbaattaahh",
    author_email="bbaattaahh@gmail.com",
    description="Create mne readable cnt files from OKITI created ones",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bbaattaahh/okiti_cnt_to_cnt",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)