# B1

from privesc_enum import citeste_linii
def cai(fisier): 

# TODO: intoarce MULTIMEA cailor din fisier (foloseste citeste_linii din enum) 
    return set(citeste_linii(fisier))


baza = cai("start/baza_suid.txt") 
acum = cai("start/suid.txt") 
print("baza:", len(baza), " acum:", len(acum))


# B2

noi = acum - baza 

print(len(noi), "SUID noi fata de sistemul curat") 

for c in sorted(noi): 

    print(" ", c)


# B3

from privesc_enum import nume, GTFO 


risc = {nume(c): ("mare" if nume(c) in GTFO else "normal") for c in noi}
periculoase = [c for c in sorted(noi) if nume(c) in GTFO] 
print("periculoase NOI:", periculoase)    