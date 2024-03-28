from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='compare_pdf',
    version='0.1',
    description='A simple package to visually compare PDF files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mor Dabastany',
    author_email='morpci@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pymupdf',
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'compare_pdf=compare_pdf:ComparePDF',
        ],
    },
)
