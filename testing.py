import re
c = """Interface wlan_soma
        ifindex 8
        wdev 0x100000001
        addr 60:31:97:3d:25:24
        ssid soma
        type AP
        wiphy 1
        channel 1 (2412 MHz), width: 20 MHz, center1: 2412 MHz
        txpower 30.00 dBm"""

ssid = re.search('(?:ssid )(.*)', c).group(1)
# print(ssid)

x = """Interface wlan_soma
        ifindex 8
        wdev 0x100000001
        addr 60:31:97:3d:25:24
        ssid
        type AP
        wiphy 1
        channel 1 (2412 MHz), width: 20 MHz, center1: 2412 MHz
        txpower 30.00 dBm"""
#
# ssid = re.search('(?:ssid )(.*)', x).group(1)
# print(ssid)

def hi(x):
    return x, 'a', 'b'

# a = hi('soma')

# print(a)

a, b, c = hi('soma')

print(a)
print(b)
print(c)
