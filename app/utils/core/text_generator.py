import logging

def generate_lorem_ipsum_payload(requested_bytes: int) -> str:
    """
    Generate a lorem ipsum text payload of approximately the specified byte size.

    This function encodes the lorem ipsum base text into bytes and then either trims it to the requested size or repeats it enough times to meet the requested byte size, ensuring the output closely matches the input parameter in terms of byte size.

    Args:
        requested_bytes (int): The desired size of the payload in bytes.

    Returns:
        str: A string of lorem ipsum text approximately equal to the requested byte size. The function ensures the output text size is as close as possible to `requested_bytes`, possibly slightly under or exactly equal.
    """
    logging.debug(f"Generating lorem ipsum payload for {requested_bytes} bytes.")
    lorem_ipsum_base = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore "
        "et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
        "aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse "
        "cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
        "culpa qui officia deserunt mollit anim id est laborum."
    )

    # Encoded to bytes
    lorem_ipsum_bytes = lorem_ipsum_base.encode('utf-8')
    base_length = len(lorem_ipsum_bytes)

    if requested_bytes <= base_length:
        result = lorem_ipsum_bytes[:requested_bytes].decode('utf-8')
        logging.debug(f"Requested bytes less than or equal to base length. Returning {len(result.encode('utf-8'))} bytes.")
    else:
        repeated_times = requested_bytes // base_length
        remaining_bytes = requested_bytes % base_length
        result = (lorem_ipsum_bytes * repeated_times + lorem_ipsum_bytes[:remaining_bytes]).decode('utf-8')
        logging.debug(f"Requested bytes greater than base length. Returning {len(result.encode('utf-8'))} bytes.")

    return result