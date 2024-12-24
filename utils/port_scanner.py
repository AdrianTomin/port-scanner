import asyncio
import termcolor
from utils.dns_utils import resolve_dns
from utils.ip_utils import is_ip


async def scan_port(ip_address: str, port: int, timeout: float = 1.0) -> None:
    """
    Attempts to connect to a specific port on the given IP address.

    Args:
        ip_address (str): The IP address to scan.
        port (int): The port number to scan.
        timeout (float): The connection timeout in seconds (default is 1.0).

    Returns:
        None

    Example:
        await scan_port("192.168.1.1", 80)
    """
    try:
        reader, writer = await asyncio.wait_for(asyncio.open_connection(ip_address, port), timeout=timeout)
        print(termcolor.colored(f'[+] Port Opened: {port}', color='green'))
        writer.close()
        await writer.wait_closed()
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        pass  # Port closed or not responding


async def scan(ip_address: str, number_of_ports: int) -> None:
    """
    Scans the given IP address for open ports up to the specified number.

    Args:
        ip_address (str): The IP address or hostname to scan.
        number_of_ports (int): The number of ports to scan, starting from 1.

    Returns:
        None

    Example:
        await scan("192.168.1.1", 100)
    """
    resolved_ip = await resolve_dns(ip_address) if not is_ip(ip_address) else ip_address
    if not resolved_ip:
        print(termcolor.colored(f'[!] Skipping {ip_address} due to DNS resolution failure.', color='red'))
        return

    print(termcolor.colored(f'\n[*] Starting scan for: {resolved_ip} ({ip_address})', color='green'))

    tasks = [scan_port(resolved_ip, port) for port in range(1, number_of_ports + 1)]
    await asyncio.gather(*tasks, return_exceptions=True)
