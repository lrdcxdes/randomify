import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="randomify",
    version="0.11",
    author="lordcodes",
    author_email="me@lordnet.ml",
    description="Simple python library for generate random words",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LORD-ME-CODE/randomify",
    project_urls={
        "Bug Tracker": "https://github.com/LORD-ME-CODE/randomify/issues",
        "Community": "https://t.me/lordnet_userbot",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
    packages=["randomify"],
)
