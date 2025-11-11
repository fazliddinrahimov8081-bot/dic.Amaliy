professions = {
    "Bill Gates": "Dasturchi",
    "Cristiano Ronaldo": "Futbolchi",
    "Elon Musk": "Tadbirkor",
    "Messi": "Futbolchi"
}
name = input("Ism kiriting: ").strip()
kasb = professions.get(name)
if kasb:
    print(f"{name} - {kasb}")
else:
    print("Kechirasiz, bunday ism topilmadi")
