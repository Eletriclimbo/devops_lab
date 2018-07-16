import ipaddress
mask_array = []
print("Number of masks: ")
n = int(input("Number: "))
for i in range(int(n)):
    k = input("Mask: ")
    mask_array.append(k)
ip_array = []
print("Number of IP pairs: ")
l = int(input())
for j in range(int(l)):
    m = input("IP 1: ")
    p = input("IP 2: ")
    ip_array.append(m)
    ip_array.append(p)
ip_number = l * 2 - 1
same_network = []
for s in range(int(l)):
    same_network.append(0)
mm = kk = int(0)
for i in range(0, ip_number, 2):
    mm = 0
    for j in range(int(n)):
        IP1 = ip_array[i]
        IP2 = ip_array[i + 1]
        MASK = mask_array[j]
        net1 = ipaddress.IPv4Network(IP1 + '/' + MASK, False)
        if (ipaddress.ip_address(IP1) in
                ipaddress.ip_network(net1)
                and ipaddress.ip_address(IP2) in
                ipaddress.ip_network(net1)):
            mm += 1
    print("mm", mm)
