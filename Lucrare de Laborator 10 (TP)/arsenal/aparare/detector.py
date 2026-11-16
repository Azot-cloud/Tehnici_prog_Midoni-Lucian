# B1
from collections import Counter
from arsenal.aparare.parse_auth import citeste_esecuri, pe_ip, esec
def suspecti(counts, prag=10):
    if prag < 1:
        raise ValueError(f"prag invalid: {prag} (cel putin 1)")
    # TODO: intoarce lista de (ip, n) cu n >= prag,
    #       sortata descrescator dupa n

    return [(ip,n)for ip,n in counts.most_common() if n>= prag]

from collections import Counter
c = Counter({"203.0.113.9": 13, "198.51.100.7": 2})
print(suspecti(c))
print(suspecti(c, prag=2))


# B2

#python -c "from arsenal.aparare.detector import suspecti; suspecti({}, 0)"

#  File "C:\Users\midon\Uni Projects\TP\Labs\Lucrare de Laborator 10 (TP)\arsenal\aparare\detector.py", line 6, in suspecti
#     raise ValueError(f"prag invalid: {prag} (cel putin 1)")
# ValueError: prag invalid: 0 (cel putin 1)


# B3

import argparse, json
from collections import Counter
from arsenal.aparare.parse_auth import citeste_esecuri
 
def main():
    p = argparse.ArgumentParser()
    p.add_argument("log")
    p.add_argument("--prag", type=int, default=10)
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    esecuri = citeste_esecuri(a.log)
    counts = Counter(e["ip"] for e in esecuri)
    sus = suspecti(counts, a.prag)
    # TODO: cu --json, scoate json.dumps cu {esecuri, pe_ip, suspecti};
    #       fara, un rezumat cu "BRUTE FORCE" pe fiecare suspect
    if a.json:
        lista = {
            "esecuri": len(esecuri),
            "pe_ip": dict(counts),
            "suspecti": sus,
        }
        print(json.dumps(lista))
    else:
        for ip, nr in counts.most_common():
            print(f" {ip}: {nr}")
        for ip, nr in sus:
            print(f"{ip}({nr} incercari)  BRUTE FORCE")
    
    
#python -m arsenal.aparare.detector arsenal/aparare/start/auth.log

if __name__ == "__main__":
    main()

