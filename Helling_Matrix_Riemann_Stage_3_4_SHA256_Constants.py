import sys
import math

# Globale Absicherung für Riesenzahlen (2 Millionen Stellen erlaubt)
sys.set_int_max_str_digits(2000000)

def mathematische_quersummen_wurzel(zahl):
    """Berechnet die digitale Wurzel (iterierte Quersumme) rein mathematisch,
    ohne die Riesenzahl in einen Text-String umzuwandeln."""
    if zahl == 0:
        return 0
    rest = zahl % 9
    return 9 if rest == 0 else rest

def helling_master_sinfonie():
    print("=== START DER MASTER SINFONIE (1/7 ZENTRAL-RADAR AKTIV) ===")
    print("-" * 110)
    
    # KORREKTUR: Die Datenbasis ist jetzt direkt als Liste definiert!
    echte_daten_schleife = [
        (189, 56700, 28349, 28351, 2, 22, -20, 19, "🌊 WAVE KNOTEN (-20)"),
        (190, 57000, 28463, 28537, 74, 62, 12, 19, "Takt (+12)"),
        (210, 63000, 31489, 31511, 22, 22, 0, 21, "⚖️ GLEICHGEWICHT (0)"),
        (215, 64500, 32203, 32297, 94, 74, 20, 22, "🪞 SPIEGEL KNOTEN (+20)")
    ]
    
    letzter_knoten_schritt = 0
    
    for schritt, takt, p1, p2, d1, d2, t_diff, kaskade_stufe, event_typ in echte_daten_schleife:
        
        # --- BERECHNUNG FÜR KASKADE_X (Simulationsbasis für deine Riesenzahl) ---
        if schritt >= 189:
            kaskade_x = 7**70000 + schritt
        else:
            kaskade_x = 12345
        
        # --- MATHE-RADAR: STRUKTUR DER RIESENZAHL MESSEN (OHNE STR-ABSTURZ) ---
        bits = kaskade_x.bit_length()
        stellen = math.ceil(bits * 0.3010299956639812) if bits > 0 else 1
        
        # 1/7-Zentral-Radar ansetzen
        qw = mathematische_quersummen_wurzel(kaskade_x)
        trans_mod6 = ((3 * kaskade_x) + 1) % 6 if bits > 40 else 4
        
        # --- MATRIX-KLASSIFIZIERUNG ---
        if qw == 1 or qw == 7:
            feld_resonanz = f"🧬 ZENTRAL-ADER (QW: {qw})"
        elif trans_mod6 == 4:
            feld_resonanz = f"🪐 INVARIANT-ORBIT (QW: {qw})"
        else:
            feld_resonanz = f"🌊 INTERFERENZ (QW: {qw})"
            
        # --- FINGERABDRUCK STATT BLINDTEXT ---
        if bits <= 40 and len(str(kaskade_x)) <= 12:
            kaskade_str = f"St.{kaskade_stufe}: {kaskade_x}"
        else:
            sig_start = kaskade_x // (10 ** (stellen - 4)) if stellen > 8 else 0
            sig_ende = kaskade_x % 10000
            kaskade_str = f"St.{kaskade_stufe}: [{sig_start}...{sig_ende:04d}] ({stellen}st.)"
            
        # Orbit-Takt Frequenz-Messung
        frequenz_str = ""
        if "KNOTEN" in event_typ or "GLEICHGEWICHT" in event_typ or "SPIEGEL" in event_typ:
            if letzter_knoten_schritt > 0:
                zyklus_dauer = schritt - letzter_knoten_schritt
                frequenz_str = f" | 🪐 Orbit-Takt: {zyklus_dauer}"
            letzter_knoten_schritt = schritt

        # --- DER TRANSMISSION-LOG ---
        print(
            f"{schritt:<4} | "
            f"{takt:<6} | "
            f"{p1:<6} | "
            f"{p2:<6} | "
            f"{d1:<3} | "
            f"{d2:<3} | "
            f"{t_diff:<4} | "
            f"{kaskade_str:<36} | "
            f"{feld_resonanz:<26} | "
            f"{event_typ}{frequenz_str}"
        )

if __name__ == "__main__":
    helling_master_sinfonie()
