Gaji = {
    "Tetap": 1000000,
    "Honor": 750000
}

Bonus = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}

for stat in ["Tetap", "Honor"]:
    print("Status", stat)
    for gol in ["A", "B", "C"]:
        print("Golongan", gol)
        print("Bonus", Bonus.get(stat).get(gol))
        print("Gaji Total", Gaji.get(stat) + Bonus.get(stat).get(gol))
        print()