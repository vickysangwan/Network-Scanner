#!/usr/bin/env python

import scapy.all as scapy
import optparse
import subprocess
subprocess.call(["nmap","192.168.43.1/24","-O"])
# import platform
# print(platform.python_version())
# print(platform.architecture('192.168.43.145')[0])
# print(platform._syscmd_uname('192.168.43.145'))
# print(platform.s)
# def scan(ip):
    # scapy.arping(ip)
    # arp_request=scapy.ARP(pdst=ip)
    # broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    # broadcast_arp_request=broadcast/arp_request
    # answered, unansered = scapy.srp(broadcast_arp_request,timeout=1)
    #To capture only answered field
    # answered= scapy.srp(broadcast_arp_request, timeout=1)[0]
    # To list all input field associated with scapy.Ether()
    # scapy.ls(scapy.Ether())
    # arp_request.pdst=ip #second way of inputing ip
    # print(arp_request.summary())
    # print(broadcast.summary())
    #To list all input field associated with scapy.ARP()
    # scapy.ls(scapy.ARP)
    # print(broadcast_arp_request.summary())
    # print(answered.summary())
    # for elements in answered:
        # print(elements[1].psrc)
        # print(elements[1].hwsrc)
        # print(elements[1].show())
        # print(".................................")
# scan("192.168.43.1/24")

# def get_inputs():
#     parser=optparse.OptionParser()
#     parser.add_option("-i","--iprange",dest="ip",help="Enter ip range of your network of type 192.162.41.1/24")
#     (options, arguments)=parser.parse_args()
#     if not options.ip:
#         parser.error("[-]Please specify IP range for scanning,--help for more info")
#     else:
#         return options
#
# def scan(ip):
#     arp_request=scapy.ARP(pdst=ip)
#     broadcast=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
#     broadcast_arp_request=broadcast/arp_request
#     answered_list=scapy.srp(broadcast_arp_request,timeout=2,verbose=False)[0]
#
#     client_list=[]
#     for elements in answered_list:
#         client_dict={"ip":elements[1].psrc,"mac":elements[1].hwsrc}
#         client_list.append(client_dict)
#     return client_list
# def get_host()
# def print_result(client_list):
#     print("IP Address\t\tMAC Address\n------------------------------------------")
#     for elements in client_list:
#         print(elements["ip"]+"\t\t"+elements["mac"])
# options=get_inputs()
# client_list=scan(options.ip)
# print_result(client_list)




















