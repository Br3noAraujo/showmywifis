#!/usr/bin/python3
#! encoding: utf-8

'''Code By Br3noAraujo'''

import subprocess
import os
import json
from datetime import datetime
from tabulate import tabulate
from colorama import init, Fore, Style
import sys

# Initialize colorama
init()

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def get_wifi_data():
    """Get Wi-Fi network data"""
    try:
        # Get network data
        meta_data = subprocess.check_output(['sudo grep psk= /etc/NetworkManager/system-connections/*'], shell=True)
        data = meta_data.decode('utf-8', errors="backslashreplace")
        return data.split('\n')[:-1]  # Remove last empty line
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}Error: Script must be run with superuser privileges (sudo){Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error getting data: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

def parse_wifi_data(data):
    """Process Wi-Fi network data"""
    wifi_list = []
    for line in data:
        try:
            # Extract network name
            essid = line.split('/')[4].split('.')[0]
            
            # Extract password
            if 'psk' in line:
                psk = line.split('psk')[1].replace('=', '')
                
                # Try to get last connection date
                try:
                    last_modified = os.path.getmtime(f"/etc/NetworkManager/system-connections/{essid}.nmconnection")
                    last_modified_date = datetime.fromtimestamp(last_modified).strftime('%m/%d/%Y %H:%M')
                except:
                    last_modified_date = "N/A"
                
                wifi_list.append([essid, psk, last_modified_date])
        except Exception as e:
            print(f"{Fore.YELLOW}Warning: Error processing line: {str(e)}{Style.RESET_ALL}")
            continue
    
    return wifi_list

def display_wifi_list(wifi_list, search_term=None):
    """Display Wi-Fi network list"""
    headers = ['NETWORK NAME', 'PASSWORD', 'LAST CONNECTION']
    
    if search_term:
        wifi_list = [wifi for wifi in wifi_list if search_term.lower() in wifi[0].lower()]
    
    if not wifi_list:
        print(f"{Fore.YELLOW}No networks found.{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}=== SAVED WI-FI NETWORKS ==={Style.RESET_ALL}")
    print(tabulate(wifi_list, headers=headers, tablefmt="grid"))

def export_to_file(wifi_list, filename="wifi_networks.txt"):
    """Export network list to file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=== SAVED WI-FI NETWORKS ===\n\n")
            for wifi in wifi_list:
                f.write(f"Network Name: {wifi[0]}\n")
                f.write(f"Password: {wifi[1]}\n")
                f.write(f"Last Connection: {wifi[2]}\n")
                f.write("-" * 50 + "\n")
        print(f"{Fore.GREEN}Data successfully exported to {filename}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error exporting data: {str(e)}{Style.RESET_ALL}")

def main_menu():
    """Main program menu"""
    while True:
        clear_screen()
        print(f"{Fore.CYAN}=== SHOW MY WIFIS ==={Style.RESET_ALL}")
        print("1. Show all networks")
        print("2. Search network by name")
        print("3. Export to file")
        print("4. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            data = get_wifi_data()
            wifi_list = parse_wifi_data(data)
            display_wifi_list(wifi_list)
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            search_term = input("Enter network name to search: ")
            data = get_wifi_data()
            wifi_list = parse_wifi_data(data)
            display_wifi_list(wifi_list, search_term)
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            data = get_wifi_data()
            wifi_list = parse_wifi_data(data)
            filename = input("Enter filename to export (or Enter for default): ")
            if not filename:
                filename = "wifi_networks.txt"
            export_to_file(wifi_list, filename)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            print(f"{Fore.GREEN}Exiting...{Style.RESET_ALL}")
            break
        
        else:
            print(f"{Fore.RED}Invalid option!{Style.RESET_ALL}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
