from socket import AF_INET, SOCK_DGRAM, socket

def get_ip_locale():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_loc = s.getsockname()[0]
    print("ip locale server: ", ip_loc)
    s.close()
    return ip_loc

# SETTO L'IP DI BROADCAST DELLA RETE


def set_ip_broadcast(ip):
    ip = ip.split('.')
    ip_broadcast = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + '255'
    return ip_broadcast
