from colorama import init, Fore
import subprocess
import time

init(autoreset=True)

def run():
    print(Fore.GREEN + "======== Executing CIS Microsoft Windows Server 2022 Benchmark v2.0.0 script ========")
    time.sleep(2)
    
def account_policies():   
    print(Fore.BLUE + "======== 1. Account Policies ========")

def password_policy_check():
    time.sleep(2)
    print(Fore.CYAN + "======== 1.1 Password Policies ========")
    time.sleep(2)
    password_history = "net accounts | Select-String 'Password history' | ForEach-Object { $_ -replace '\D+(\d+)','$1'}"
    password_history_result = subprocess.run(['powershell', '-command', password_history], shell=True, capture_output=True, text=True)
    
    if password_history_result.returncode == 0:
        output = password_history_result.stdout.strip()
        password_history_value = int(output)
        
        if password_history_value >= 24:
            print(Fore.GREEN + "[+] 1.1.1 PASSED: " + "Length of password history value:", password_history_value)  
        else:
            print(Fore.RED + "[-] 1.1.1 FAILED: Length of password history value:", password_history_value)
    
    if password_history_value < 24:
        print(Fore.RED + "   [!] Password history length should be 24 or more.")
    else:
        return f"Command failed. Error output: {password_history_result.stderr}"
