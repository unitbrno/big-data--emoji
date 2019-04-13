# PoC
blacklisted_ports = ['137','138']
with open('fwdata.csv') as data:
    for line in data:
        if (line.split(';')[4] in blacklisted_ports) or (line.split(';')[5] in blacklisted_ports):
            print(line)
