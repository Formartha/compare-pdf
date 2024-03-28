import fitz  # PyMuPDF library
import cv2
import numpy as np
import logging
import argparse
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class ComparePDF:
    def __init__(self, pdf_paths):
        self.pdf_paths = pdf_paths
        self.pdf_documents = [fitz.open(path) for path in pdf_paths]

    def compare(self):
        if len(self.pdf_paths) < 2:
            logger.error("At least two PDF files are required for comparison")
            return

        logger.info(f"Comparing PDF files: {', '.join(self.pdf_paths)}")

        with ThreadPoolExecutor() as executor:
            images_per_page = executor.map(self._get_page_images, range(min(doc.page_count for doc in self.pdf_documents)))

            for page_num, images in enumerate(images_per_page, start=1):
                self._compare_images(images, page_num)

        logger.info("PDF comparison completed")

    def _get_page_images(self, page_num):
        return [self._convert_to_opencv(doc.load_page(page_num), dpi=150) for doc in self.pdf_documents]

    def _convert_to_opencv(self, pdf_page, dpi=72):
        pix = pdf_page.get_pixmap(alpha=False, dpi=dpi)
        img = np.frombuffer(pix.samples, np.uint8).reshape((pix.height, pix.width, pix.n))
        if pix.n == 4:
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        elif pix.n == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        return img

    def _display_image(self, image, page_num):
        cv2.imshow(f'Page {page_num}', image)
        cv2.waitKey(1)  # Reduce the wait time for better responsiveness
        cv2.destroyAllWindows()

    def _compare_images(self, images, page_num):
        equal = all(np.array_equal(images[0], img) for img in images)
        if equal:
            logger.info(f"All images on Page {page_num} are equal")
        else:
            logger.info(f"Some images on Page {page_num} are not equal (Page {page_num} compared across files):")
            for i in range(len(images)):
                for j in range(i + 1, len(images)):
                    if not np.array_equal(images[i], images[j]):
                        logger.info(
                            f"Image {i + 1} from {self.pdf_paths[i]} is different from Image {j + 1} from {self.pdf_paths[j]} on Page {page_num}")


def main():
    parser = argparse.ArgumentParser(description='Compare PDF files visually')
    parser.add_argument('--pdf', action='append', required=True, help='Path to the PDF file')
    args = parser.parse_args()

    compare = ComparePDF(args.pdf)
    compare.compare()


if __name__ == "__main__":
    main()