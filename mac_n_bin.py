"""mac_n_bin"""

def mac2list(mac) -> int | None:
    """mac2str"""
    if ":" not in mac:
        return None
    else:
        mac_list = mac.split(":")
        for i in range(len(mac_list)):
            mac_list[i] = int(mac_list[i], 16)
        mac_list = [bin(i)[2:].zfill(8) for i in mac_list]
        return mac_list

def mac2bin(mac) -> list | None:
    """mac2list"""
    mac_list = mac2list(mac)
    mac_str = "".join(mac_list)
    return mac_str

def bin2mac(mac, upper=True) -> str | None:
    """bin2mac"""
    x = "X" if upper else "x"
    mac_str = mac
    mac_list = [int(mac_str[i:i+8], 2) for i in range(0, len(mac_str), 8)]
    mac_str = ":".join([f"{i:02{x}}" for i in mac_list])
    return mac_str
