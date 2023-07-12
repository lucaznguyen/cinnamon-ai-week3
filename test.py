import os
from PIL import Image

from converter import ConvertToImage

def test_convert_file_to_image(tmpdir = 'test_folder', expdir = 'expected_folder'):
    """
    Test the sample file with extension (.png, .heic, .tiff, .pdf) if they are converted into a file with extension .png.
        
    Parameters
    ----------
    tmpdir: str
        The test directory.

    Assert
    -------
    The test result has extension .png appears in the expected_folder.
    """
    # Define the file extensions and their corresponding expected image extensions
    file_extensions = ['.png', '.heic', '.tiff', '.pdf']
    image_extension = '.png'
    
    for file_extension in file_extensions:
        # Create a temporary file with the specified extension
        file_path = os.path.join(tmpdir, 'test_file{}'.format(file_extension))
        
        # Define the expected image path with the PNG extension
        expected_image_path = os.path.join(expdir, f'test_file_{file_extension[1:]}.png')

        
        # Call the function to convert the file to an image
        convert_func =  ConvertToImage()
        convert_func.convert(file_path, expdir)
        
        # Assert that the image file exists
        assert os.path.exists(expected_image_path)