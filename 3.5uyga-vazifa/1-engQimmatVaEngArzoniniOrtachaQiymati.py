cars = {
    "Malibu": 35000,
    "Spark": 12000,
    "Cobalt": 18000,
    "Tracker": 28000
}
eng_qimmat = max(cars, key=cars.get)
eng_arzon = min(cars, key=cars.get)
ortacha = sum(cars.values()) / len(cars)
print("Eng qimmat mashina:", eng_qimmat, '-', cars[eng_qimmat],'$')
print("Eng arzon mashina:", eng_arzon, '-', cars[eng_arzon],'$')
print("Mashinalarning ortacha narxi:", round(ortacha,2),'$')
