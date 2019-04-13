# quick PoC
import subprocess

with open("malicious_ips") as data, open('malicious_ips_in_other_logs', 'w') as out:
    for line in data:
        cmd = "grep -i " + line.strip() + " PC*"
        t = subprocess.run(cmd, shell=True, stdout=out)
