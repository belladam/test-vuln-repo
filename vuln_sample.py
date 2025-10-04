# vuln_sample.py
import subprocess

# This is intentionally insecure so Bandit can find it.
subprocess.call("ls", shell=True)
