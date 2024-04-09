import logging
from typing import List, Dict
from random import choice
from copy import deepcopy

from app.configs.config import load_config

from app.utils.core.image_manager import ProductListManager
from app.utils.core.text_generator import async_generate_lorem_ipsum

async def gen_product_card_item_list(
        requested_bytes: int,
        product_desc_text_bytes : int = 75
        ) -> List[Dict]:
    """
    Generates a list of product card items, each containing details about a product image
    and its description.

    Args:
        requested_bytes (int): desired bytes consumption for the product card
        product_desc_text_bytes (int, optional): desired bytes of text for product description. Defaults to 75

    Returns:
        List[Dict]: A list of dictionaries, each representing a product card with image details
                    and a lorem ipsum text description. The structure for each dictionary is:
                    {
                        'image_path': str,  # Relative path of the image
                        'image_bytes': int, # Size of the image in bytes
                        'image_category': str,   # Category of the product image
                        'image_details': {
                            'item_title': str,      # Formatted title of the product image
                            'item_description': str # Generated lorem ipsum description
                        }
                    }

    Notes:
       - Byte distribution may not perfectly match the requested distribution due to varying image size.
    """
    # Check if the requested bytes is within the support limit
    max_supported_bytes = int(load_config()['app']['max_request_bytes'])
    if requested_bytes > max_supported_bytes:
        logging.warn(f"Truncating the request [{requested_bytes}] to max_supported_bytes [{max_supported_bytes}]")
        requested_bytes = max_supported_bytes
    # Invoke variables to capture the memory usage
    image_byte_quota = float(1 if requested_bytes == 0 else requested_bytes)
    product_list = deepcopy(ProductListManager().get_product_detail_list())
    product_card_item_list = []

    total_image_bytes_generated = 0
    total_text_bytes_generated = 0
    
    product_text = await async_generate_lorem_ipsum(product_desc_text_bytes)
    product_text_bytes = len(product_text.encode('utf-8'))

    while image_byte_quota > 0:
        random_product = choice(product_list)
        product_card_item_list.append(random_product)
        image_byte_quota -= int(random_product['image_bytes'])

    if product_card_item_list:
        for product in product_card_item_list:
            product['image_details']['item_description'] = product_text
            total_image_bytes_generated += product['image_bytes']
            total_text_bytes_generated += product_text_bytes
        else:
            logging.debug(f"""
                        Requested Bytes : [{int(requested_bytes)}]
                        Generated Bytes : [{total_text_bytes_generated + total_image_bytes_generated}]
                            Total image bytes : [{total_image_bytes_generated}]
                            Total text bytes  : [{total_text_bytes_generated}] 
                        Extra bytes generated : [{(total_text_bytes_generated + total_image_bytes_generated)- requested_bytes}]""")
    
    return product_card_item_list
