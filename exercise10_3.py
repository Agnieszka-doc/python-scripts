import pandas as pd

# dane
data = {
    "Name": [
        "Hydrogen",
        "Helium",
        "Lithium",
        "Beryllium",
        "Boron",
        "Carbon",
        "Nitrogen",
        "Oxygen",
        "Fluorine",
        "Neon"
    ],
    
    "Symbol": [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne"
    ],
    
    "Weight": [
        1.008,
        4.0026,
        6.94,
        9.0122,
        10.81,
        12.011,
        14.007,
        15.999,
        18.998,
        20.180
    ]
}

# index od 1
index = range(1, 11)

# DataFrame
df = pd.DataFrame(data, index=index)

print(df)