import ipcalc


def calc_sub_ret(masti, base_ip, base_mask, base_nr_hosturi):

    na = base_ip
    ba = ipcalc.Network(str(base_ip) + '/' + str(base_mask)).broadcast()
    f = open("ipuri.txt", 'w')

    # Scriu reteaua de baza

    f.write('\nN.A.:')
    f.write(str(na) + '/' + str(base_mask))
    f.write('\nB.A.:')
    f.write(str(ba) + '/' + str(base_mask))
    na = na + 1
    ba = ba - 1
    f.write('\nR.A.:')
    f.write(str(na) + " - " + str(ba) + '/' + str(base_mask) + '\n')
    
    na = na - 1

    for i in range(len(masti)):
        ba = ipcalc.Network(str(na) + '/' + str(masti[i])).broadcast()

        f.write('\n' + str(base_nr_hosturi[i]))
        f.write('\nN.A.:')
        f.write(str(na) + '/' + str(masti[i]))
        f.write('\nB.A.:')
        f.write(str(ba) + '/' + str(masti[i]))
        x = str(ipcalc.Network(str(na) + '/' + str(masti[i])).netmask())
        na = na + 1
        ba = ba - 1
        f.write('\nR.A.:')
        f.write(str(na) + " - " + str(ba) + '/' + str(masti[i]))
        f.write("\nMasca: " + x + '\n')

        na = ba + 1 + 1

    f.close()


# ////////////

ip = input("IP?\n")
mask = input("Masca?\n")
nr_subretele = int(input("Cate retele a dat nebunu?(nu uita de alea intermediare)\n"))

if nr_subretele > 1:
    print("\nLa final programul scuipa retelele in ordine\n"
          "Daca primeste input 2 la numarul de hosturi, completeaza automat restul cu 2\n")

    nr_hosturi = []
    marime_subret = []

    print("Nr de hosturi al subretelei", 1)
    hosts = int(input())
    nr_hosturi.insert(0, hosts)


    for i in range(1, nr_subretele):
        if i-1 >= 0 and nr_hosturi[i-1] != 2:
            print("Nr de hosturi al subretelei", i + 1)
            hosts = int(input())
            nr_hosturi.insert(i, hosts)
        else:
            nr_hosturi.insert(i, 2)
    nr_hosturi.sort(reverse=True)

    j = 0
    for i in nr_hosturi:

        p = 0
        while pow(2, p) - 2 < i:
            p = p + 1

        marime_subret.insert(j, 32-p)
        j = j + 1

    dummy = ipcalc.Network(ip + '/' + mask).network()

    calc_sub_ret(marime_subret, base_ip=dummy, base_mask=mask, base_nr_hosturi=nr_hosturi)

else:
    f = open("ip.txt", 'w')

    f.write("\nN.A.:" + str(ipcalc.Network(ip + '/' + mask).network()) + "/" + str(mask))
    f.write("\nB.A.:" + str(ipcalc.Network(ip + '/' + mask).broadcast()) + "/" + str(mask))
    f.write("\nR.A.:" + str(ipcalc.Network(ip + '/' + mask).network() + 1) + "-" +
            str(ipcalc.Network(ip + '/' + mask).broadcast() - 1) + "/" + mask)
    x = str(ipcalc.Network(ipcalc.Network(ip + '/' + mask).netmask_long()))
    x = x[:len(x)-3]
    f.write("\nMasca: " + x)
    
    f.close()
