import subprocess
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve the cycle delay from the .env file, defaulting to 1.5 minutes if not set
cycle_delay_minutes = float(os.getenv('CYCLE_DELAY_MINUTES', 1.5))

while True:
    try:
        # Execute the other script
        subprocess.call(["python3", "phone_random.py"])
        # Wait for the specified delay before running it again, converting minutes to seconds
        time.sleep(cycle_delay_minutes * 60)
    except KeyboardInterrupt:
        print("Script interrupted by user. Exiting.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
