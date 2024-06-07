# SNMP Trap Sender

A simple Python script to send SNMP traps using `pysnmp`.

## Requirements

- Python 3.x
- `pysnmp` library

## Installation

Install the `pysnmp` library using `pip`:

```bash
pip install pysnmp
```


## Usage

Run the script with the IP address, port, and trap message as arguments:

```bash
python send_snmp_trap.py <IP_ADDRESS> <PORT> <MESSAGE>
```

### Example

```bash
python send_snmp_trap.py 172.1.0.1 162 "Sample SNMP Trap Message"
```

This command sends an SNMP trap to the IP address 172.1.0.1  on port 162 with the message `"Sample SNMP Trap Message"`.

## Script Explanation

- IP_ADDRESS: The IP address of the SNMP manager to send the trap to.
- PORT: The port number to send the trap to (default for SNMP traps is 162).
- MESSAGE: The message to include in the SNMP trap.


