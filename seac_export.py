# seac_export.py
# SeacSync SQLite3 DB export to csv for Subsurface

import sqlite3
import csv

# Global Variables
divecount = 0  # Track the number of dives exported 

# Open SQLite3 Database
# TODO: Catch failure to open DB
conn = sqlite3.connect("divesDB.db")
cur = conn.cursor()

# Query unique dive numbers
cur.execute("SELECT DISTINCT dive_number FROM dive_data")

# Iterate over each dive number
for dive in cur.fetchall():
    # Build output filename string
    output = "dive" + str(dive[0]) + ".csv"
    csvfile = open(output, 'w', newline='')
    csvw = csv.writer(csvfile)
    # Write CSV Headers to match subsurface import names
    csvw.writerow(["Sample Time", "Sample NDL","Sample CNS","Sample depth","Sample temperature"])

    # Query DB for current dive number
    cur.execute("SELECT runtime_s, ndl_tts_s, cns, depth_cm, temperature_mCx10 FROM dive_data WHERE dive_number=? ORDER BY runtime_s ASC",dive)

    # Read result
    result = cur.fetchone()
    # Catch EOF 
    while result != None:
        # Convert cm to m, temperature to Celsius
        result = result[0:3] + (result[3]/100.0,) + (result[4]/100.0,)
        csvw.writerow(result)
        result = cur.fetchone()
    csvfile.close()

    divecount += 1

conn.close()

print("Success! Converted", divecount, "dives.")