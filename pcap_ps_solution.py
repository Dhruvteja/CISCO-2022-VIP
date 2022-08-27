numberdictionary = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
                    7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth"}
f = open("conversion.txt", "w")
iplist = []
clist = []
check = True
print("Enter 10 IPv4 addresses.")

for item in range(1, 11):
    iplist.append(input(f'Enter {numberdictionary[item]} IP address : '))
print("\n")
for j in iplist:
    final = []
    dectobin = []
    dectooct = []
    dectohex = []
    w = j
    if w[0] == '0' or w.count('.') != 3:
        continue

    w = w.split('.')
    w = [int(i) for i in w]

    for i in w:
        if ((i < 0) or (i > 255)) or len(w) != 4:
            check = False
            break
    if check:
        clist.append(1)
        for i in w:
            dectooct.append(oct(i)[2:])
            dectobin.append('{:0>8}'.format(str(bin(i))[2:]))
            dectohex.append(hex(i)[2:])
    else:
        clist.append(0)

    x = ".".join(dectobin)
    y = ".".join(dectooct)
    z = ".".join(dectohex)

    if check:
        final.append(j)
        final.append(x)
        final.append(y)
        final.append(z)

        for k in final:
            f.write(k + "\t")
        f.write("\n")

    else:
        f.write("Invalid IPv4 address\n")
        check = True

f.close()
fread = open("conversion.txt", "r")
for p in range(0, 10):
    if clist[p] == 1:
        print(f"The {numberdictionary[p+1]} IP address in Decimal, Binary,"
              f" Octal and hexadecimal format is {fread.readline()}")
    else:
        print(f"The {numberdictionary[p+1]} IP address is invalid IPv4 address\n")
        fread.readline()
fread.close()
