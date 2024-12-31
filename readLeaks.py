from tqdm import tqdm
import sys
import os

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_in_file(file_path, emailtosearch):
    counter = 0
    found = False
    with open(file_path, 'r', encoding='iso-8859-1') as f:
        try:
            with tqdm(f, desc=f"\033[93m \033[1m Processing {file_path} \033[0m") as pbar:
                for line in pbar:
                    counter += 1
                    if emailtosearch in line.strip():
                        ClearConsole()
                        print(f"\n \033[96m \033[1m {line.strip()} \033[0m \n")
                        found = True
                        pbar.close()
                        break 
                    pbar.update(1)
            pbar.close()
        except UnicodeDecodeError as m:
            print('UnicodeDecodeError', m)
            pass
        f.close()
    return found, counter

try:
    allowed_extensions = [".sql", ".txt", ".csv"]
    emailtosearch = input('Enter email to search: (No check for validity of email) ').strip()
    path = input('Enter file or directory name to search in (default: Cit0day Leak): ').strip()
    if path == '':
        path = 'Cit0day cleaned.txt'
    
    ClearConsole()
    sys.stdout.flush()
    print(f"\x1b[6;30;42m Email: {emailtosearch} \t Path: {path} \x1b[6;30;42m \x1b[0m \n")

    total_counter = 0
    email_found = False

    if os.path.isfile(path):
        email_found, total_counter = search_in_file(path, emailtosearch)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for filename in files:
                if any(filename.endswith(ext) for ext in allowed_extensions):
                    file_path = os.path.join(root, filename)
                    email_found, file_counter = search_in_file(file_path, emailtosearch)
                    total_counter += file_counter
                    if email_found:
                        break
            if email_found:
                break
    else:
        print(f"Path {path} does not exist.")
except KeyboardInterrupt:
    print('Interrupted by user Exiting...\n') 
    sys.exit(0)

if not email_found:
    print(f'Email not found, checked: {total_counter} lines')