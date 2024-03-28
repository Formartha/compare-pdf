# setup.py
from setuptools import setup, find_packages

setup(
    name='compare_pdf',
    version='0.1',
    description='A simple package to visually compare PDF files',
    author='Mor Dabastany',
    author_email='morpci@gmail.com.com',
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