from colorama import init, Fore
import subprocess
import time

init(autoreset=True)

passed_checks = 0
failed_checks = 0
error_checks = 0
requires_manual_check = 0

def winserv2022_da():
    global passed_checks, failed_checks, error_checks, requires_manual_check
    print(Fore.GREEN + "            ======== Executing CIS Microsoft Windows Server 2022 Benchmark v2.0.0 (DC) ========")
    time.sleep(2)
    print()
    print(Fore.BLUE + "                                 ======== 1. Account Policies ========")
    time.sleep(1)
    print()
    print(Fore.CYAN + "                                 ======== 1.1 Password Policies ========")
    print()
    time.sleep(1)
    
    password_history = "net accounts | Select-String 'Password history' | ForEach-Object { $_ -replace '\\D+(\d+|None)','$1'}"
    password_history_result = subprocess.run(['powershell', '-command', password_history], shell=True, capture_output=True, text=True)
    if password_history_result.returncode == 0:
        output = password_history_result.stdout.strip()
        if output == "None":
            print(Fore.RED + "[-] 1.1.1 FAILED: Length of password history value:", output)
            print(Fore.RED + "   [!] Password history length should be 24 or more.")
            failed_checks += 1
        else:
            try:
                password_history_value = int(output)
                if password_history_value >= 24:
                    print(Fore.GREEN + "[+] 1.1.1 PASSED: Length of password history value:", password_history_value)
                    passed_checks += 1
                else:
                    print(Fore.RED + "[-] 1.1.1 FAILED: Length of password history value:", password_history_value)
                    print(Fore.RED + "   [!] Password history length should be 24 or more.")
                    failed_checks += 1
            except ValueError:
                print(Fore.RED + "[!] 1.1.1 Error: Length of password history value is not valid.")
                error_checks += 1
    else:
        print(Fore.RED + "=====================================================================")
        print(Fore.RED + f"1.1.1 Command failed. Error output: {password_history_result.stderr}")
        print(Fore.RED + "=====================================================================")
        error_checks += 1
    
    
    print()
    
    max_password_age = "net accounts | Select-String 'Maximum password age' | ForEach-Object { $_ -replace '\\D+(\\d+)','$1'}"
    max_password_age_result = subprocess.run(['powershell', '-command', max_password_age], shell=True, capture_output=True, text=True)
    if max_password_age_result.returncode == 0:
        output = max_password_age_result.stdout.strip()
        if output.isdigit():
            max_password_age_value = int(output)
            if max_password_age_value <= 365 and max_password_age_value != 0:
                print(Fore.GREEN + "[+] 1.1.2 PASSED: Maximum password age value:", max_password_age_value)
                passed_checks += 1
            else:
                print(Fore.RED + "[-] 1.1.2 FAILED: Maximum password age value:", max_password_age_value)
                print(Fore.RED + "   [!] Maximum password age should be set to 365 or fewer days, but not 0.")
                failed_checks += 1
        else:
            print(Fore.RED + "[-] 1.1.2 Error: Maximum password age value is not valid.")
            error_checks += 1
    else:
        print(Fore.RED + "=====================================================================")
        print(Fore.RED + f"1.1.2 Command failed. Error output: {max_password_age_result.stderr}")
        print(Fore.RED + "=====================================================================")
        error_checks += 1


    print()
    
    min_password_age = "net accounts | Select-String 'Minimum password age' | ForEach-Object { $_ -replace '\D+(\d+)','$1'}"
    min_password_age_result = subprocess.run(['powershell', '-command', min_password_age], shell=True, capture_output=True, text=True)
    if min_password_age_result.returncode == 0:
        output = min_password_age_result.stdout.strip()
        if output.isdigit():
            min_password_age_value = int(output)
            if min_password_age_value >= 1:
                print( Fore.GREEN + "[+] 1.1.3 PASSED: Minimum password age value:", min_password_age_value)
                passed_checks += 1
            else:
                print(Fore.RED + "[-] 1.1.3 FAILED: Minimum password age value:", min_password_age_value)
                print(Fore.RED + "   [!] Minimum password age should be set to 1 or more days")
                failed_checks += 1
        else:
            print(Fore.RED + "[-] 1.1.3 Error: Maximum password age value is not valid.")
            error_checks += 1               
    else:
        print(Fore.RED + "=====================================================================")
        print(Fore.RED + f"1.1.2 Command failed. Error output: {min_password_age_result.stderr}")
        print(Fore.RED + "=====================================================================")
        error_checks += 1    

    print()
    
    min_password_length = "net accounts | Select-String 'Minimum password length' | ForEach-Object { $_ -replace '\D+(\d+)','$1' }"
    min_password_length_result = subprocess.run(['powershell', '-command', min_password_length], shell=True, capture_output=True, text=True)
    if min_password_length_result.returncode == 0:
        output = min_password_length_result.stdout.strip()
        if output.isdigit():
            min_password_length_value = int(output)
            if min_password_length_value >= 14:
                print(Fore.GREEN + "[+] 1.1.4 PASSED: Minimum password length value:", min_password_length_value)
                passed_checks += 1
            else:
                print(Fore.RED + "[-] 1.1.4 FAILED: Minimum password length value:", min_password_length_value)
                print(Fore.RED + "   [!] Minimum password length should be set to 14 or more")
                failed_checks += 1
        else:
            print(Fore.RED + "[-] 1.1.4 Error: Minimum password length value is not valid.")
            error_checks += 1
    else:
        print(Fore.RED + "=====================================================================")
        print(Fore.RED + f"1.1.4 Command failed. Error output: {min_password_length_result.stderr}")
        print(Fore.RED + "=====================================================================")
        error_checks += 1

    print()

    print(Fore.MAGENTA + "[!] 1.1.5 Requires manual check: 'Password must meet complexity requirements' should be set to 'Enabled'. Check 'Computer Configuration\Policies\Windows Settings\Security Settings\Account Policies\Password Policy\Password must meet complexity requirements'")
    requires_manual_check += 1

    print()
    
    

    print()
    
    print(Fore.GREEN + f"Checks Passed: {passed_checks}")
    print(Fore.RED + f"Checks Failed: {failed_checks}")
    print(Fore.RED + f"Checks Errored: {error_checks}")
    print(Fore.RED + f"Manual checks required: {requires_manual_check}")








def splitter():
    splitter = Fore.MAGENTA + "================================================"
    print(splitter)
