import re

def is_valid_ipv4(ipv4):
    pattern = "^(?:0|([1-9]\d{0,2}))\.(?:0|([1-9]\d{0,2}))\.(?:0|([1-9]\d{0,2}))\.(?:0|([1-9]\d{0,2}))$"

    result = re.fullmatch(pattern, ipv4)

    if result:
        return len([octet for octet in ipv4.split('.') if int(octet) > 255]) == 0
    else:
        return False

# print(is_valid_ipv4("192.168.1.1"))
# print(is_valid_ipv4("0.0.0.0"))
# print(is_valid_ipv4("255.01.50.111"))
# print(is_valid_ipv4("255.00.50.111"))
# print(is_valid_ipv4("256.101.50.115"))
# print(is_valid_ipv4("192.168.101."))
# print(is_valid_ipv4("192168145213"))