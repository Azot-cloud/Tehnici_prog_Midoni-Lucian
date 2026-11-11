import sys

print(sys.modules.get("enum"))

import argparse, json, os
# A1

def citeste_linii(cale):
    with open(cale, encoding="utf-8") as f:
        # TODO: intoarce lista liniilor .strip(), fara cele goale si fara cele cu #

        return [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]


cai = citeste_linii("start/suid.txt")

print("linii SUID:", len(cai))



# A2

def nume(cale): 

    # TODO: intoarce ce e dupa ultimul "/"  (vezi rsplit) 
    return cale.rsplit("/")[-1]

nume_unice = {nume(c) for c in cai}    # set comprehension 

print("SUID distincte:", len(nume_unice)) 



# A3

GTFO = {"find", "vim.basic", "vim", "nmap", "cp", "bash", 

        "less", "awk", "python3", "perl"} 

def suid_constatari(cale): 

    cai = citeste_linii(cale) 

    # TODO: pentru fiecare cale UNICA, in ordine sortata, un dict: 
    return [
        {
        
        "cale": c, 
        "nume": nume(c), 
        "risc": "mare" if nume(c) in GTFO else "normal"

        }
        for c in sorted(set(cai))
    ]
    #   {"cale": c, "nume": nume(c), 
    #    "risc": "mare" daca nume(c) in GTFO, altfel "normal"} 

suid = suid_constatari("start/suid.txt") 
mari = [c for c in suid if c["risc"] == "mare"] 

print(len(suid), "SUID,", len(mari), "cu risc mare") 
print(sorted(c["nume"] for c in mari)) 



# A4

def sudo_constatari(cale): 

    out = [] 

    for ln in citeste_linii(cale): 
        if ":" in ln:
            user, drept = ln.split(":", 1)
            user = user.strip()
            drept = drept.strip()
            
            out.append({
                "user": user, 
                "drept": drept, 
                "risc": "mare" if "NOPASSWD" in drept else "normal"
            })
    return out

def cron_constatari(cale):
    rezultate = []
    for ln in citeste_linii(cale):
        campuri = ln.split()
        if len(campuri) >= 7:
            user = campuri[5]
            comanda = " ".join(campuri[6:])
            rezultate.append({
                "user": user,
                "comanda": comanda
            })
    return rezultate

def enumereaza(d): 
    return {
        "suid": suid_constatari(os.path.join(d, "suid.txt")), 
        "sudo": sudo_constatari(os.path.join(d, "sudo.txt")), 
        "cron": cron_constatari(os.path.join(d, "crontab.txt")), 
    }
print("Grupare reusita")



# A5

def main(): 

    p = argparse.ArgumentParser()
    p.add_argument("capturi") 
    p.add_argument("--json", action="store_true")
    a = p.parse_args() 

    raport = enumereaza(a.capturi)

    if a.json: 
        print(json.dumps(raport, indent=2, ensure_ascii=False)); return 

    for categorie, lista in raport.items(): 

        mari = [c for c in lista if c.get("risc") == "mare"] 
        print(f"{categorie}: {len(lista)} gasite, {len(mari)} cu risc mare") 

    # TODO: utilizatorii implicati = multimea userilor din sudo REUNITA cu cei din cron 
    users_sudo = {item["user"] for item in raport["sudo"]}
    users_cron = {item["user"] for item in raport["cron"]}
    utilizatori = sorted(users_sudo | users_cron)

    print(f"utilizatori implicati: {', '.join(utilizatori)}")


    with open("enum.json", "w", encoding="utf-8") as f:
        json.dump(raport, f, indent=2, ensure_ascii=False) 

    print("Raport salvat in enum.json") 

  
  
if __name__ == "__main__": 

    main()

# Comanda de executie : python privesc_enum.py start