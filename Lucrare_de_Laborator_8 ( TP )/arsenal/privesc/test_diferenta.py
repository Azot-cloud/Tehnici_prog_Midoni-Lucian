# B4

def test_doar_ce_e_nou(): 

    acum = {"a", "b", "c"} 
    baza = {"a", "b"} 
    assert acum - baza == {"c"}

# Comanda de rulare:    python -m pytest -q test_diferenta.py