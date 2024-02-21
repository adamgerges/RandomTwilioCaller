import subprocess
import time

while True:
    # Execute the other script
    subprocess.call(["python3", "phone_random.py"])

    # Wait for 90 seconds before running it again
    time.sleep(90)
