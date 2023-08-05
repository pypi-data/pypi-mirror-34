import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "standard",
    packages = ["standard"],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = "1.0.0",
    description = "Standard Library for Python",
    author = "Yoginth",
    author_email = "yoginth@zoho.com",
    url = "https://yoginth.ml",
    classifiers=(
        "Programming Language :: Python",
        "Natural Language :: English",
        "Environment :: Plugins",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ),
    project_urls={
        'Patreon': 'https://www.patreon.com/yoginth',
        'Source': 'https://gitlab.com/yoginth/standard',
    },
)
