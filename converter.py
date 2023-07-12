import os
import logging

from PIL import Image
from pillow_heif import register_heif_opener
from pdf2image import convert_from_path

"""
The program converts a file (.png, .heic, .tiff, .pdf) to PNGs and saves them to a directory
"""


class ConvertToImage:

    @staticmethod
    def convert_pdf_to_png(pdf_file_path: str,
                           poppler_path: str) -> list[object]:
        """
        Converts a PDF to PNGs and saves them to a directory

        Parameters
        ----------
        pdf_file_path: str
            The path to the PDF
        poppler_path: str
            The path to the poppler bin folder
            
        Returns
        -------
        pages: list[object]
            List of PIL.Image.Image objects  
        """
        pages = convert_from_path(pdf_file_path, poppler_path=poppler_path)
        return pages

    @staticmethod
    def save_pngs(images: list[object],
                  file_name: str,
                  directory: str = "result") -> None:
        """
        Saves PNGs to a specified directory     
        
        Parameters
        ----------
        directory: str
            The folder path to save the PNGs to
        images: str
            List of PIL.Image.Image objects
        file_name: str
            The file name of input

        Returns
        -------
        """

        logging.info("Saving PNGs to directory...")

        for i, image in enumerate(images):
            image.save(f"{directory}/{file_name}_{i}.png", "PNG")

        logging.info("Saving complete.")

    @staticmethod
    def convert(from_path: str, to_path: str = None) -> list[object]:
        """
        Converts a file (.png, .heic, .tiff, .pdf) to PNGs and saves them to a directory.
        
        Parameters
        ----------
        from_path: str
            The file path
        to_path: str
            The folder path to save the PNGs to

        Returns
        -------
        images:  list[object]
            List of PIL.Image.Image objects
        """

        # Support heic conversion
        register_heif_opener()

        # Get file format
        file_extension = os.path.splitext(from_path)[1].lower()

        # Get file name
        file_name = os.path.basename(from_path)
        file_name = os.path.splitext(file_name)[0]

        logging.info("Converting file to PNG.")

        if file_extension == '.pdf':
            images = ConvertToImage.convert_pdf_to_png(from_path)[0]
        else:
            images = [Image.open(from_path)]

        logging.info("Conversion complete.")

        # Save PNGs to directory
        if to_path != None:
            ConvertToImage.save_pngs(images, file_name, to_path)

        return images
