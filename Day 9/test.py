ip_address = ["192.168.1.1","192.168.1.0","192.168.1.2","192.168.1.3","0.0.0.0","78.45.256.256"]
i = 0
while i<len(ip_address):
    if ip_address[i] == "0.0.0.0":
        break
    else:
        print(ip_address[i])
    i +=1
else:
    print("No 0.0.0.0 found in the list")
