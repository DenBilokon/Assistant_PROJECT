from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="help-assistant",
    version="0.0.11",
    description="Addressbook, notebook, clean folder",
    url="https://github.com/DenBilokon/Assistant_PROJECT",
    readme="README.md",
    authors="Denis Bilokon, Kirill Sheremeta, Denys Zaycev, Dmytro Marchenko, Maria Palona",
    author_email="greenjuiced@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    entry_points={"console_scripts": ["assistant = assistant.menu:menu"]},
)
