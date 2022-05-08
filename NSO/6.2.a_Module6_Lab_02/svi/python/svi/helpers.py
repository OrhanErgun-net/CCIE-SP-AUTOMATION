from ipaddress import IPv4Network


def get_address(prefix):
    return list(IPv4Network(prefix).hosts())[0]


def get_netmask(prefix):
    return str(IPv4Network(prefix).netmask)