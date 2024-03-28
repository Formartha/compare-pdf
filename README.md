PDF Visual Comparison Tool
==========================

This script compares PDF files visually by converting each page into images and then comparing them using OpenCV. It's particularly useful for identifying differences between PDF files that may not be apparent through text comparison alone.

Features
--------

*   Compares PDF files visually, page by page.
*   Supports multi-page PDF files.
*   Reports differences between PDF files, specifying the page number and source file.

Requirements
------------

*   Python 3.x
*   PyMuPDF (`fitz`) library
*   OpenCV (`cv2`) library
*   NumPy (`numpy`) library

Installation
------------

1.  Clone the repository:
    
    bashCopy code
    
    `git clone https://github.com/your_username/pdf-visual-comparison.git`
    
2.  Install the required dependencies:
    
    bashCopy code
    
    `pip install -r requirements.txt`
    

Usage
-----

bashCopy code

`python compare_pdf.py --pdf <path_to_pdf1> --pdf <path_to_pdf2> ...`

*   Replace `<path_to_pdf1>`, `<path_to_pdf2>`, etc. with the paths to the PDF files you want to compare.
*   At least two PDF files are required for comparison.

Example
-------

bashCopy code

`python compare_pdf.py --pdf file1.pdf --pdf file2.pdf`

This will compare `file1.pdf` and `file2.pdf` visually, reporting any differences found.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.

