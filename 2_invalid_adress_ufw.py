# This is just quick PoC, definitely deserves better implementation
def is_private(ip_addr):
    if ip_addr[0:3] == "10.":
        return True
    if ip_addr[0:3] == "172":
        try:
            if int(ip_addr[4:6]) >= 16 and int(ip_addr[4:6]) <= 31 and ip_addr[6] == ".":
                return True
        except:
            pass
    if ip_addr[0:7] == "192.168":
        return True
    return False


def is_not_known(ip_addr):
    known_subnets = ['192.168.50.101', '192.168.50.102', '192.168.50.105','192.168.50.106', '192.168.50.254', '192.168.56.1','192.168.56.50','192.168.56.254','192.168.1.1', '192.168.50.255', '192.168.56.255' ]
    if is_private(ip_addr):
        if ip_addr not in known_subnets:
            return True
    return False

known_subnets = ['192.168.50.0/24', '192.168.56.0/24']

def main():
    with open('fwdata.csv') as data, open('malicious_ips', 'w') as out:
        mals = set()
        for line in data:
            line = line.split(';')
            if is_not_known(line[1]):
                outstr = line[1] + "\n"
                mals.add(outstr)
                print(line)
            if is_not_known(line[2]):
                outstr = line[2] + "\n"
                mals.add(outstr)
                print(line)
        for elem in mals:
            out.write(elem)
main()