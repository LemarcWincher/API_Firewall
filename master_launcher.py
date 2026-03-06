
import subprocess
import sys
import time

# Paths to indivdual scripts

flask_path = r"C:\Users\Lemarc\Desktop\College\Python\API Firewall\firewall.py"
master_path = r"C:\Users\Lemarc\Desktop\College\Python\API Firewall\master_script.py"

# Start Flask in the background

print("Starting background Flask server...")
flask_proc = subprocess.Popen([sys.executable, flask_path])

# Wait a few seconds to let Flask start, server HAS to be running for scripts to work
time.sleep(3)


# Run the master script (test + user packets)

print("Running master script (test packets + user packets)...")
result = subprocess.run([sys.executable, master_path])

if result.returncode != 0:
    print(f"Master script exited with errors (code {result.returncode})")
else:
    print("Master script finished successfully.\n")


# Optional: terminate Flask

terminate_flask = input("Do you want to terminate the background Flask server? (y/n): ").strip().lower()
if terminate_flask == "y":
    flask_proc.terminate()
    print("Background Flask server terminated.")
else:
    print("Background Flask server is still running. You can terminate manually later.")

print("Launcher script finished.")
