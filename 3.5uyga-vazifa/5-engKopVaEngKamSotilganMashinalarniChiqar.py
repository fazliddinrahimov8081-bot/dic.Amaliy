car_count = {
    "Chevrolet": 120,
    "Toyota": 95,
    "BMW": 60,
    "Kia": 75
}
eng_kop = max(car_count, key=car_count.get)
eng_kam = min(car_count, key=car_count.get)
print(f"Eng kop sotilgan mashina: {eng_kop} ({car_count[eng_kop]} dona)")
print(f"Eng kam sotilgan mashina: {eng_kam} ({car_count[eng_kam]} dona)")
