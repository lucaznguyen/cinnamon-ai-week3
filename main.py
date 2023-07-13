import argparse

from converter import ConvertToImage

"""
The program converts a file (.png, .heic, .tiff, .pdf) to PNGs and saves them to a directory
"""


def convert_to_images(opt: object) -> None:

    # Conversion process
    ConvertToImage.convert(opt.from_path, opt.to_path)


if __name__ == "__main__":
    """Argument"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--f",
        default="example.heic",
        help="the path of the file that needs to be converted",
    )
    parser.add_argument(
        "--o",
        default="./",
        help="the path of the converted file",
    )

    opt = parser.parse_args()

    convert_to_images(opt)
