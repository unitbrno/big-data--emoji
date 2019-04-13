import subprocess

with open('privileges_escalation', 'a') as out:
    cmd = 'grep -in "special privileges" PC*'
    subprocess.run(cmd, shell=True, stdout=out)