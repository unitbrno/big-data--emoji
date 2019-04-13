# PoC
import subprocess

with open('log_deletion', 'a') as out:
    cmd = 'grep -i "log was cleared" PC*'
    subprocess.run(cmd, shell=True, stdout=out) 
    cmd = 'grep -i "log file was cleared" PC*'
    subprocess.run(cmd, shell=True, stdout=out) 