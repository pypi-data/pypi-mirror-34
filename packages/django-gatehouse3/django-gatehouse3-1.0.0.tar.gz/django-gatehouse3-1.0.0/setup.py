import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-gatehouse3",
    version="1.0.0",
    author='Aulemasa',
    author_email='maszs@wp.pl',
    description="A simple Django app to create gatehouse Web app.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aulemasa/gatehouse3",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
)
