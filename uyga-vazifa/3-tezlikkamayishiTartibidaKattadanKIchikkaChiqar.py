speed = {
    "Tesla": 250,
    "BMW": 240,
    "Mercedes": 260,
    "Audi": 230
}
print("Mashinalar teligi (kamayish tartibida):")
for nom, tezlik in sorted(speed.items(), key=lambda x: x[1], reverse=True):
    print(f"{nom}: {tezlik} km/soat")

