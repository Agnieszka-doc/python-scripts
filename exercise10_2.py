import pandas as pd
import numpy as np

# dni bieżącego miesiąca
dates = pd.date_range("2026-05-01", periods=31)

# losowe temperatury od 15 do 25 stopni
temps = np.random.randint(15, 26, size=31)

# utworzenie Series
s = pd.Series(data=temps, index=dates)

print(s)