import os

def find_pdf_size(top):
    total_size = 0
    for root, dirs, files in os.walk(top): # przechodzi przez cały katalog i podkatalogi
        for file in files:
            if file.lower().endswith(".pdf"): # sprawdzenie plików
                path = os.path.join(root, file) # pełna ścieżka
                total_size += os.path.getsize(path) # rozmiar w bajtach 
    return total_size
print(find_pdf_size("."))