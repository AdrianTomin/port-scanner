import asyncio
import termcolor
from utils.port_scanner import scan


async def main():
    """
        Main function to gather user input and start scanning.

        Prompts the user to enter IP addresses or hostnames and the number of ports to scan.
        Initiates scanning tasks for the provided targets.

        Returns:
            None

        Example:
            asyncio.run(main())
        """
    ip_addresses = input('[*] Enter IP addresses or hostnames to scan (comma-separated): ')
    number_of_ports = int(input('[*] Enter how many ports to scan: '))

    if ',' in ip_addresses:
        print(termcolor.colored('[*] Scanning multiple targets...', color='cyan'))
        targets = ip_addresses.split(',')
    else:
        targets = [ip_addresses]

    tasks = [scan(target.strip(), number_of_ports) for target in targets]
    await asyncio.gather(*tasks, return_exceptions=True)

    print(termcolor.colored('[*] Scanning complete. Exiting program.', color='yellow'))


if __name__ == '__main__':
    """
        Entry point for the program. Runs the main function in an asyncio event loop
        and handles interruptions gracefully.
        """
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(termcolor.colored('\n[!] Scan interrupted. Exiting...', color='red'))
