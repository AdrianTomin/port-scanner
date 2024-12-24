import socket


def is_ip(address: str) -> bool:
    """
    Determines if the provided string is a valid IP address.

    Args:
        address (str): The string to validate as an IP address.

    Returns:
        bool: True if the string is a valid IP address, False otherwise.

    Example:
        is_valid = is_ip("192.168.1.1")
    """
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False
