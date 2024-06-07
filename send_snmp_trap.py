#!/usr/bin/env python3

import sys
from pysnmp.hlapi import *

def print_usage():
    print("Usage: send_snmp_trap.py <IP_ADDRESS> <PORT> <MESSAGE>")
    print("Example: send_snmp_trap.py 172.1.0.1 \"Sample SNMP Trap Message\"")

def send_snmp_trap(ip, port, message):
    community_string = 'public'  # Change as needed
    enterprise_oid = '1.3.6.1.4.1.8072.2.3.0'
    trap_oid = '1.3.6.1.4.1.8072.2.3.0.1'
    
    errorIndication, errorStatus, errorIndex, varBinds = next(
        sendNotification(
            SnmpEngine(),
            CommunityData(community_string),
            UdpTransportTarget((ip, int(port))),
            ContextData(),
            'trap',
            NotificationType(
                ObjectIdentity(trap_oid)
            ).addVarBinds(
                ('1.3.6.1.2.1.1.1.0', OctetString(message))
            )
        )
    )

    if errorIndication:
        print(f"Error: {errorIndication}")
    else:
        print("SNMP trap sent successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(1)

    ip_address = sys.argv[1]
    port = sys.argv[2]
    trap_message = sys.argv[3]

    send_snmp_trap(ip_address, port, trap_message)

