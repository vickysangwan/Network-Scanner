#!/usr/bin/env python

import scapy.all as scapy
import optparse


def get_inputs():
    parser=optparse.OptionParser()
    parser.add_option("-i","--iprange",dest="ip",help="Enter ip range of your network of type 192.162.41.1/24")
    (options, arguments)=parser.parse_args()
    if not options.ip:
        parser.error("[-]Please specify IP range for scanning,--help for more info")
    else:
        return options

def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast_arp_request=broadcast/arp_request
    answered_list=scapy.srp(broadcast_arp_request,timeout=2,verbose=False)[0]
    client_list=[]
    for elements in answered_list:
        client_dict={"ip":elements[1].psrc,"mac":elements[1].hwsrc}
        client_list.append(client_dict)
    return client_list
def print_result(client_list):
    print("IP Address\t\tMAC Address\n------------------------------------------")
    for elements in client_list:
        print(elements["ip"]+"\t\t"+elements["mac"])
options=get_inputs()
client_list=scan(options.ip)
print_result(client_list)





















