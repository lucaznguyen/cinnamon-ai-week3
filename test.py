import os
from PIL import Image

from converter import ConvertToImage


def test_convert_file_to_image(tmpdir):
    """
    Test the sample file with extension (.png, .heic, .tiff, .pdf) if they are converted into a file with extension .png.
        
    Parameters
    ----------
    tmpdir: str
        The test directory.

    Assert
    -------
    The test result has extension .png and the given input size (here is 100x100).
    """
    # Define the file extensions and their corresponding expected image extensions
    file_extensions = ['.png', '.heic', '.tiff', '.pdf']
    image_extension = '.png'

    for file_extension in file_extensions:
        # Create a temporary file with the specified extension
        file_path = os.path.join(tmpdir, 'test_file{}'.format(file_extension))
        with open(file_path, 'wb') as file:
            file.write(b'This is a sample file content')

        # Define the expected image path with the PNG extension
        expected_image_path = os.path.join(tmpdir, 'test_image.png')

        # Call the function to convert the file to an image
        convert_func = ConvertToImage()

        convert_func.convert(file_path, expected_image_path)

        # Assert that the image file exists
        assert os.path.exists(expected_image_path)

        # Open the image file and check its contents
        with Image.open(expected_image_path) as image:
            # Assert that the image size matches the expected size
            assert image.size == (100, 100)

            # Get the image pixels
            pixels = list(image.getdata())

            # Convert the file content to list of integers
            expected_pixels = list(b'This is a sample file content')

            # Assert that the image pixels match the expected pixels
            assert pixels == expected_pixels
