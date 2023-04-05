filename = r'C:\Users\Angel\OneDrive\Desktop\Messprotokolle-und-daten\Gesammt\Log-WV1ZZZ2HZHH007098-149760km\Log-WV1ZZZ2HZHH007098-149760km.txt'  # Setzen Sie den Dateipfad hier

with open(filename, 'r') as f:
    # Extrahieren Sie die Fahrzeug-Ident.-Nr.
    lines = f.readlines()
    id_line = lines[7].split(':')[1]
    id = id_line[:18]
    print(id)