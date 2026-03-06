import subprocess
import sys
import time

# Paths to individual scripts
test_packets_path = r"C:\Users\Lemarc\Desktop\College\Python\API Firewall\test_packets.py"
user_packets_path = r"C:\Users\Lemarc\Desktop\College\Python\API Firewall\user_packets.py"

# Function to run Python script within 
def run_script(path):
    print(f"\n=== Running {path.split('/')[-1]} ===")
    result = subprocess.run([sys.executable, path])
    if result.returncode != 0:
        print(f"Script {path} exited with errors.")
    else:
        print(f"Finished running {path.split('/')[-1]}.\n")

# Runs predefined test packets first
run_script(test_packets_path)

#Sleeps for 4 seconds so the screen doesn't flood
time.sleep(4)

# Runs user packet prompts last
run_script(user_packets_path)
