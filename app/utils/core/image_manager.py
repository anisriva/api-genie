import os
import logging
from app.utils.core.singleton import Singleton

class ProductListManager(metaclass=Singleton):
    """
    A singleton class that manages a list of product image details within a specified directory.

    Scans a directory for image files (PNG, JPG, JPEG, GIF, BMP) and compiles a list of image details,
    including path, size, category, and a formatted title. 

    Args:
        directory_path (str): Directory path to scan for product images. Defaults to "static/images/products".
    """

    def __init__(self, directory_path="static/images/products"):
        self.image_details_list = self.__get_product_list(directory_path)

    def __get_product_list(self, directory_path):
        """
        Scans the specified directory path for image files and compiles their details.

        The function walks through the directory, checking for files with specific image extensions
        and compiles their details such as path, size, category, and a formatted title.

        Args:
            directory_path (str): Directory path to scan for image files.

        Returns:
            List[Dict]: A list of dictionaries with compiled image details.
        """
        def format_title(title):
            """
            Formats the file name into a more readable title.

            Args:
                title (str): The original file name, typically derived from the image file name.

            Returns:
                str: A formatted title with each word capitalized and separated by spaces.
            """
            return ' '.join(word.capitalize() for word in title.replace('-', ' ').split())

        image_details_list = []
        for root, _, files in os.walk(directory_path):
            *_, category = root.split(os.sep)
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                    file_path = os.path.join(root, file)
                    image_size_bytes = os.path.getsize(file_path)
                    image_details = {
                        'image_path': os.path.join('images','products',category, file),
                        'image_bytes': image_size_bytes,
                        'image_category': category,
                        'image_details': {
                            'item_title': format_title(os.path.splitext(file)[0])
                        }
                    }
                    image_details_list.append(image_details)
        logging.info(f"Loaded product images from: [ {directory_path} ]")
        return image_details_list

    def get_product_detail_list(self):
        """
        Retrieves the list of product image details.

        Returns:
            List[Dict]: The list of product image details compiled during class instantiation.
        """
        return self.image_details_list
