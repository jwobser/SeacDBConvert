import sqlite3
import csv

conn = sqlite3.connect("divesDB.db")
cur = conn.cursor()
cur.execute("SELECT DISTINCT dive_number FROM dive_data")

divecount = 0
for dive in cur.fetchall():
    output = "dive" + str(dive[0]) + ".csv"
    csvfile = open(output, 'w', newline='')
    csvw = csv.writer(csvfile)
    csvw.writerow(["Sample Time", "Sample NDL","Sample CNS","Sample depth","Sample temperature"])
    cur.execute("SELECT runtime_s, ndl_tts_s, cns, depth_cm, temperature_mCx10 FROM dive_data WHERE dive_number=? ORDER BY runtime_s ASC",dive)
    result = cur.fetchone()
    while result != None:
        result = result[0:3] + (result[3]/100.0,) + (result[4]/100.0,)
        # print(result)
        csvw.writerow(result)
        result = cur.fetchone()
    # result = result + (result[3]/100.0,) + (result[4]/100.0,)  #print all values for testing purposes
    csvfile.close()
    divecount += 1

conn.close()

print("Success! Converted", divecount, "dives.")