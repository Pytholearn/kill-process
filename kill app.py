import subprocess
import time


while True:
    time.sleep(5)
    res = subprocess.getoutput("taskkill /PID cm* /F")