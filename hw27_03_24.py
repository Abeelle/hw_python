def sortstr(sp):
    nsp = []
    for i in sp:
        if type(i) == str:
            nsp.append(i)

    for a in range(len(nsp) - 1):
        for j in range(a + 1, len(nsp)):
            if len(nsp[a]) > len(nsp[j]):
                x = nsp[a]
                nsp[a] = nsp[j]
                nsp[j] = x
    return nsp


sp = ['ghtgjl', 2, True, 'htlbcrf', 'pf,sk','!']
print(sortstr(sp))
