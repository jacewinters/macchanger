#!/usr/bin/env python

# A simple python3 program to change network device MAC address
# Created by
# Jace Winters
# November 8 2019

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change your device MAC address. enter -i or --interface followed by your network adapter")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address to change your device MAC address. enter -m or --mac followed by your new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface using -i or --interface or --help")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC address using -m or --mac or --help")
    return options

# More secure way and not vulnerable to hijacking and code execution.

def change_mac(interface, new_mac):
    print ("Previous MAC address")
    subprocess.call(["ifconfig", interface, ])
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac, ])
    subprocess.call(["ifconfig", interface, "up"])
    print ("Your new MAC address")
    subprocess.call(["ifconfig", interface, ])
    print("[+] Changed the MAC address for " + interface + " to " + new_mac)


options = get_arguments()
change_mac(options.interface, options.new_mac)

print("All done!")
print("You are browsing the internet anonymously now!")
print("Have a nice day!")

# raw_input for python 2
# #interface = input("interface > ")
# interface = options.interface
# #new_mac = input("new_Mac address > ")
# new_mac = options.new_mac
# Unsecure way of writing a simple code, vulnerable to hijacking and root priv code execution.
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
