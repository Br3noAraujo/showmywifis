#!/usr/bin/python3
#! encoding: utf-8

'''Code By Br3noAraujo'''

import subprocess
from tabulate import tabulate 

# getting meta data
meta_data = subprocess.check_output(['sudo grep psk= /etc/NetworkManager/system-connections/*'], shell=True)

# decoding meta data
data = meta_data.decode('utf-8', errors ="backslashreplace")

# splitting data by line by line
data = data.split('\n')
data.remove(data[-1])

wifi_list = [['WI-FI NAME', 'PASSWORD'], [' ', ' ']]
# parsing data
for line in data:

    # parsing line for ESSID
    essid = line.split('/')
    essid = essid[4]
    essid = essid.split('.')[0]
    
    # parsing line for psk
    
    if line.find('psk')!= -1:
        psk = line.split('psk')[1]
        psk = psk.replace('=', '')
    wifi_list.append([essid, psk])

# showing output
print(tabulate(wifi_list))