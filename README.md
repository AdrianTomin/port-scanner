# Port Scanner Tool 🔍

A Python-based tool that scans IP addresses or hostnames for open ports. This tool supports scanning multiple targets and resolves hostnames to IP addresses before performing the scan.

Built with:
<br>
<br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
<br>
<br>

## Features ✨
- **Hostname resolution**: Resolves hostnames to their corresponding IP addresses.
- **Port scanning**: Identifies open ports on a given IP address or hostname.
- **Multiple target support**: Scans one or more IPs/hostnames simultaneously.
- **Asynchronous design**: Efficient and fast scanning using Python’s `asyncio`.

## Requirements 🛠️
- `python 3.x`
- `termcolor` – For colored terminal output.

## Installation Guide 📝

### 1. Clone the repository:
```bash
git clone https://github.com/AdrianTomin/port-scanner.git
cd port-scanner
```

### 2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  
```
> On Windows: venv\Scripts\activate

### 3. Install dependencies:
The required libraries are listed in requirements.txt. You can install them using pip:
```bash
pip install -r requirements.txt
```
If you don’t have the requirements.txt file yet, you can generate it as follows:
```bash
pip freeze > requirements.txt
```

### 4. Run the tool:
After installing the dependencies, you can run the tool by executing the following command:

```bash
python main.py
```

## Example Output 🖥️
```
[*] Enter IP addresses or hostnames to scan (comma-separated): example.com
[*] Enter how many ports to scan: 100

[*] Starting scan for: 93.184.216.34 (example.com)
[+] Port Opened: 80
[*] Scanning complete. Exiting program.
```

## Badges
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

## Authors
- [@AdrianTomin](https://www.github.com/AdrianTomin)
