import datetime

MONTH_TRANSLATION = {
    "Januar": "January",
    "Februar": "February",
    "März": "March",
    "April": "April",
    "Mai": "May",
    "Juni": "June",
    "Juli": "July",
    "August": "August",
    "September": "September",
    "Oktober": "October",
    "November": "November",
    "Dezember": "December"
}


filename = r'C:\Users\Angel\OneDrive\Desktop\Messprotokolle-und-daten\Gesammt\Log-WV1ZZZ2HZHH007098-149760km\Log-WV1ZZZ2HZHH007098-149760km.txt'  # Setzen Sie den Dateipfad hier

with open(filename, 'r') as f:
    # Extrahieren Sie die Fahrzeug-Ident.-Nr.
    lines = f.readlines()
    date_line = lines[0].split(',')
    # Verwenden Sie das Wörterbuch zur Übersetzung des Monatsnamens
    month_name = date_line[2].strip()
    month = MONTH_TRANSLATION.get(month_name, month_name)
    date = str(date_line[1] +"_"+ datetime.datetime.strptime(month, "%B").strftime("%m") +"_"+ date_line[3]+"_")
    