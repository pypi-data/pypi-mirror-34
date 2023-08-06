import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dupan",
    version="0.1",
    author="Zhu Sheng LI",
    author_email="digglife@gmail.com",
    description="manuplating baidu yun",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/digglife/baidupan",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
