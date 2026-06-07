# DETSU v1.2 : Risque Palu avec Humidité
print("=== DETSU Palu Risk 2025 v1.2 ===")

nom_quartier = input("Ton quartier à Lomé : ")
pluie_mm = int(input("Pluie ce mois en mm : "))
temp_c = int(input("Température moyenne °C : "))
humidite = int(input("Humidité en % : "))

# Logique triple facteur
if pluie_mm > 150 and temp_c > 25 and humidite > 70:
    risque = "CRITIQUE 🔴🔴🔴"
    conseil = "ALERTE MAX : Moustiquaire + Répulsif + Éliminer eaux"
elif pluie_mm > 100 or temp_c > 28 or humidite > 80:
    risque = "ÉLEVÉ 🔴" 
    conseil = "Dormir sous moustiquaire impératif"
else:
    risque = "MODÉRÉ 🟡"
    conseil = "Restez vigilant"

print(f"\nQuartier : {nom_quartier}")
print(f"Pluie : {pluie_mm}mm | Temp : {temp_c}°C | Humidité : {humidite}%")
print(f"Risque Palu : {risque}")
print(f"Conseil DETSU : {conseil}")
print("\nProjet DETSU Togo - Objectif KAIST 2029")