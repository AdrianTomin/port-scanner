import socket
import asyncio
import termcolor


async def resolve_dns(host: str) -> str | None:
    """
    Resolves a hostname to an IP address.

    Params:
        host (str): The hostname to resolve.

    Returns:
        str | None: The resolved IP address as a string, or None if resolution fails.

    Example:
        resolved_ip = await resolve_dns("example.com")
    """
    try:
        ip_info = await asyncio.get_event_loop().getaddrinfo(host, None)
        return ip_info[0][4][0]
    except socket.gaierror:
        print(termcolor.colored(f'[!] Unable to resolve DNS for: {host}', color='red'))
        return None
