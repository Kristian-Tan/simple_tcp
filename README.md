# SIMPLE TCP TESTING TOOL
Simple tools to manually test socket programming project. Requires python3.

## Features:
- Arguments can be inputted via command line arguments vs via interactive console
- Verbose mode vs silent mode
- SSL/TLS wrapped socket (optional)
- Does not require additional python module (only using ```socket```, ```argparse```, and ```ssl```)

## Common Usage:

## Arguments:
- "-h"/"--help": display all command line arguments
- "-a"/"--host": (optional) set target host, ex: ```-a 192.168.137.20```, will default to ```localhost``` if not set
- "-p"/"--port": (optional) set target port, ex: ```-p 8888```, will default to ```80``` if not set
- "-b"/"--buffer": (optional) set buffer size, ex: ```-b 1024```, will default to ```4092``` if not set
- flag mode: "-s"/"--server" or "-c"/"--client", can only choose one, will default to client mode if not set
- flag interactive: "-i"/"--interactive", ask for host, port, buffer, and mode interactively (easier for noobs)
- flag verbose: "--verbose", display verbose output (useful for debugging)

### SSL Arguments:
- flag ssl: "--ssl": add this flag to use ssl mode
- "--ssl_server_certificate": set path to ssl server certificate (for ssl server mode only)
- "--ssl_server_privatekey": set path to ssl server private key (for ssl server mode only)
- "--ssl_client_ca": set path to certificate authority (CA)'s certificate (for ssl client mode only)