import ctypes
import os
from colorama import init, Fore
import WinServ2022

# Initialise colorama for colored output
init(autoreset=True)

# Function to check if the script is running with administrator privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Function to check if the script is running with root privileges
def is_redhat_root():
    return os.geteuid() == 0

# Function to display the operating system selection menu
def display_os_menu():
    print(Fore.GREEN + "[+] Administrator privileges detected")
    print("Please select an operating system:")
    print("1. " + Fore.YELLOW + "Windows Server")
    print("2. " + Fore.YELLOW + "Red Hat Enterprise Linux")

# Function to display Windows Server benchmark options
def display_windows_options():
    print("Please select a Windows Server benchmark:")
    print("1. " + Fore.YELLOW + "CIS Microsoft Windows Server 2022 Benchmark v2.0.0")
    print("2. " + Fore.YELLOW + "CIS Microsoft Windows Server 2019 Benchmark v2.0.0")
    print("3. " + Fore.YELLOW + "CIS Microsoft Windows Server 2016 Benchmark v2.0.0")

# Function to display Red Hat Enterprise Linux benchmark options
def display_redhat_options():
    print("Please select a Red Hat Enterprise Linux benchmark:")
    print("1. " + Fore.YELLOW + "CIS Red Hat Enterprise Linux 8 Benchmark v2.0.0")
    print("2. " + Fore.YELLOW + "CIS Red Hat Enterprise Linux 7 Benchmark v2.0.0")


def main():
   
    if is_admin():
        display_os_menu()
        os_choice = input("Enter your choice (1/2): ")
        
        if os_choice == "1":
            print(Fore.GREEN + "[+] Windows Server selected")
            display_windows_options()
            windows_choice = input("Enter your choice (1/2/3): ")
            if windows_choice == "1":
                print(Fore.GREEN + "[+] You selected: " + Fore.YELLOW + "CIS Microsoft Windows Server 2022 Benchmark v2.0.0")
                WinServ2022.run()
                WinServ2022.account_policies()
                WinServ2022.password_policy_check()
            elif windows_choice == "2":
                print(Fore.GREEN + "[+] You selected: " + Fore.YELLOW + "CIS Microsoft Windows Server 2019 Benchmark v2.0.0")
            elif windows_choice == "3":
                print(Fore.GREEN + "[+] You selected: " + Fore.YELLOW + "CIS Microsoft Windows Server 2016 Benchmark v2.0.0")
            else:
                print("Invalid choice")
        elif os_choice == "2":
            
            if is_redhat_root():
                print(Fore.GREEN + "[+] You selected: " + Fore.YELLOW + "Red Hat Enterprise Linux")
                display_redhat_options()
                redhat_choice = input("Enter your choice (1/2): ")
                if redhat_choice == "1":
                    print(Fore.GREEN + "[+] You selected: " + Fore.YELLOW + "CIS Red Hat Enterprise Linux 9 Benchmark v1.0.0")
                elif redhat_choice == "2":
                    print(Fore.GREEN + "[+] You selected: " + Fore.YELLOW + "CIS Red Hat Enterprise Linux 7 Benchmark v2.0.0")
                else:
                    print("Invalid choice")
            else:
                print(Fore.RED + "[-] AutoReview must be run as root")
        else:
            print("Invalid choice")
    else:
        print(Fore.RED + "[-] AutoReview must be run as an administrator")


if __name__ == "__main__":
    main()
