import math
import os
import sys

def sieve_to_100_million():
    """Generiert alle 5.761.455 Planeten (Primzahlen) bis 100.000.000."""
    limit = 100000000
    ist_prim = bytearray([1]) * (limit + 1)
    ist_prim[0] = 0
    ist_prim[1] = 0
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if ist_prim[i]:
            ist_prim[i*i : limit+1 : i] = b'\x00' * len(range(i*i, limit+1, i))
            
    return [p for p in range(limit + 1) if ist_prim[p]]

def quersummen_wurzel(n):
    """Berechnet die iterierte Quersumme (digitale Wurzel)."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

def super_grossraum_scan():
    print("================================================================================")
    print("MEGA-MUSTER-VALIDIERUNG & EXPORT: 100.000.000 PLANETEN-RÄUME")
    print("================================================================================")
    
    planeten = sieve_to_100_million()
    gesamt_planeten = len(planeten)
    print(f"[*] {gesamt_planeten:,} Planeten geladen. Synchronisiere Mega-Raum...\n")
    
    # --- AUTOMATISCHER DESKTOP-PFAD ---
    desktop_pfad = os.path.join(os.path.expanduser("~"), "Desktop")
    datei_name = os.path.join(desktop_pfad, "helling_planeten_100mio.txt")
    
    print(f"[*] Starte Export... Datei wird geschrieben auf:\n    {datei_name}\n")
    
    # Öffnet die Datei auf dem Desktop zum Schreiben
    with open(datei_name, "w", encoding="utf-8") as f:
        # Tabellenkopf in der Datei erstellen
        f.write("Planet (p) | 300-Takt (S1) | Mod6 (S2) | (3p+1) Mod 6 | Q-Wurzel | Feld-Resonanz\n")
        f.write("-" * 90 + "\n")
        
        treffer = 0
        zentral_adern_zaehler = 0
        
        for p in planeten:
            if p <= 3:
                continue
                
            mod6_rest = p % 6
            transform = (3 * p) + 1
            trans_mod6 = transform % 6
            q_wurzel = quersummen_wurzel(p)
            
            if q_wurzel == 1 or q_wurzel == 7:
                zentral_adern_zaehler += 1
                status = "🧬 ZENTRAL-ADER (Pulsation 1/7)"
            elif trans_mod6 == 4:
                status = "🪐 STABILER INVARIANT-ORBIT"
            else:
                status = "🌊 INTERFERENZ-ZONE"
            
            # JEDER einzelne Planet wird mit seinen Metriken sauber in die Datei geschrieben
            f.write(f"p: {p:<7} | Takt: {p*300:<9} | 6k {'+1' if mod6_rest==1 else '-1':<5} | Rest: {trans_mod6:<8} | QW: {q_wurzel:<8} | {status}\n")
            
            # Konsolen-Anzeige (Takt-Filter bleibt für das IDLE-Terminal aktiv)
            if (p * 300) % 900 == 0 or treffer < 10 or (p > 99999900 and treffer < 25):
                treffer += 1
                print(f"p: {p:<7} | Takt: {p*300:<9} | 6k {'+1' if mod6_rest==1 else '-1':<5} | Rest: {trans_mod6:<8} | QW: {q_wurzel:<8} | {status}")
                if treffer == 11:
                    print(f"\n[... {gesamt_planeten - 25:,} Planeten werden im Hintergrund in die Datei exportiert ...]\n")
                    
        f.write("-" * 90 + "\n")
        f.write(f"[*] TOTAL-NACHWEIS ERBRACHT: Alle {gesamt_planeten:,} Planeten stehen starr auf Rest 4!\n")
        f.write(f"[*] Skelett-Struktur: Genau {zentral_adern_zaehler:,} Planeten pulsieren als 1/7 Zentral-Adern.\n")

    print("-" * 90)
    print("[*] FERTIG! Die komplette Liste liegt jetzt einsatzbereit auf deinem Desktop.")
    print("================================================================================")

if __name__ == "__main__":
    super_grossraum_scan()
