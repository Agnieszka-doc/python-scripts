from ij import IJ, ImagePlus
from ij.plugin.frame import RoiManager
from ij.gui import Line, Overlay
import csv
import os

# POBRANIE AKTUALNEGO ZDJĘCIA
imp = IJ.getImage()

if imp is None:
    raise ValueError("No active image found")

# ZAMANA STACKA NA ODDZIELNE KANAŁY 1=INTEGRYNY 2=OBRYS KOMÓRKI
stack = imp.getStack()

integrin_channel = ImagePlus("integrin", stack.getProcessor(1))
cell_channel = ImagePlus("cell", stack.getProcessor(2))

cell_channel.show()
integrin_channel.show()

# SEGMENTACJA KOMÓRKI
IJ.setAutoThreshold(cell_channel, "Otsu dark")
IJ.run(cell_channel, "Convert to Mask", "")

rm = RoiManager.getRoiManager()
rm.reset()

IJ.run(cell_channel, "Analyze Particles...", "size=500-Infinity add")

if rm.getCount() == 0:
    raise ValueError("No cells detected")

roi = rm.getRoi(0)

# USTAWIENIE ROI NA OBU KANAŁACH
cell_channel.setRoi(roi)
integrin_channel.setRoi(roi)

# POBRANIE MASKI I GRANIC ROI
mask = roi.getMask()
bounds = roi.getBounds()

ip_int = integrin_channel.getProcessor()

# WYZNACZENIE WSPÓŁRZĘDNYCH X W OBRĘBIE ROI
xs = []

for yy in range(bounds.height):
    for xx in range(bounds.width):

        if mask is not None and mask.getPixel(xx, yy) == 0:
            continue

        x = bounds.x + xx
        xs.append(x)

if len(xs) == 0:
    raise ValueError("Empty ROI")

xs.sort()

n = len(xs)

rear_limit = xs[int(n * 0.333)]
front_limit = xs[int(n * 0.667)]

print("Rear limit :", rear_limit)
print("Front limit:", front_limit)

# RYSOWANIE LINII PODZIAŁU NA OBRAZIE
overlay = Overlay()

line1 = Line(rear_limit, bounds.y, rear_limit, bounds.y + bounds.height)
line2 = Line(front_limit, bounds.y, front_limit, bounds.y + bounds.height)

overlay.add(line1)
overlay.add(line2)

integrin_channel.setOverlay(overlay)

# ANALIZA INTENSYWNOŚCI
sum_rear = 0.0
sum_front = 0.0

count_rear = 0
count_front = 0

for yy in range(bounds.height):
    for xx in range(bounds.width):

        if mask is not None and mask.getPixel(xx, yy) == 0:
            continue

        x = bounds.x + xx
        y = bounds.y + yy

        intensity = ip_int.getPixelValue(x, y)

        # LEWA 1/3 → (ANODA)
        if x <= rear_limit:
            sum_rear += intensity
            count_rear += 1

        # PRAWA 1/3 → (KATODA)
        elif x >= front_limit:
            sum_front += intensity
            count_front += 1

        # ŚRODEK 
        else:
            pass


# OBLICZENIE PARAMETRÓW
mean_rear = sum_rear / count_rear if count_rear > 0 else 0
mean_front = sum_front / count_front if count_front > 0 else 0

intden_rear = sum_rear
intden_front = sum_front

ratio = mean_front / mean_rear if mean_rear > 0 else 0

# WYNIKI
print("=== RESULTS ===")
print("Rear pixels :", count_rear)
print("Front pixels:", count_front)

print("Rear mean :", mean_rear)
print("Front mean:", mean_front)

print("Rear IntDen :", intden_rear)
print("Front IntDen:", intden_front)

print("Front/Rear ratio:", ratio)

# EKSPORT PLIKU
desktop = IJ.getDirectory("home") + "Desktop\\integrins\\"

if not os.path.exists(desktop):
    os.makedirs(desktop)

output_csv = desktop + "results.csv"

file_exists = os.path.exists(output_csv)

# OTWARCIE PLIKU
with open(output_csv, "a") as f:

    writer = csv.writer(
        f,
        delimiter=';',
        lineterminator='\n'
    )

    if not file_exists:

        writer.writerow([
            "Measurement",
            "Image",
            "Rear_mean",
            "Front_mean",
            "Rear_IntDen",
            "Front_IntDen"
        ])

    
# WYZNACZENIE NUMERU POMIARU
    measurement_id = 1

    if file_exists:

        try:
            with open(output_csv, "r") as rf:
                measurement_id = sum(1 for line in rf)
        except:
            measurement_id = 1

    
# ZAPIS WYNIKÓW DO PLIKU CSV
    writer.writerow([
        measurement_id,
        imp.getTitle(),
        round(mean_rear, 3),
        round(mean_front, 3),
        round(intden_rear, 3),
        round(intden_front, 3),
    ])

print("Saved to:", output_csv)