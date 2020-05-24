#!/usr/bin/env python

import subprocess
import optparse
import re

def mac_Changer(interface, new_Mac):
    print("[+] Changing the MAC address of " + interface + " to " + new_Mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_Mac])
    subprocess.call(["ifconfig", interface, "up"])

def args_parser_returner():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="This is Interface Option")
    parser.add_option("-m", "--mac-address", dest="mac", help="This is the MAC Option")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Enter a correct interface, --help for more info")
    elif not options.mac:
        parser.error("[-] Enter a correct Mac Address")
    return options

def get_current_MAC(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] The mac address could not be read")

options = args_parser_returner()

current_Mac = get_current_MAC(options.interface)
print("The Current Mac => " + str(current_Mac))

mac_Changer(options.interface, options.mac)

current_Mac = get_current_MAC(options.interface)

if current_Mac == options.mac:
    print("[+] Mac Successfully Changed ! ")
else:
    print("[-] Mac not changed")