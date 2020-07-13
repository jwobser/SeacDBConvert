# SeacDBConvert
Short Python Script to unpack SEAC Action DB into individual dives for importing into subsurface.

### Usage
1) Sync your Seac Action to your PC
2) Locate the database file. It is likely in C:\users\\\[username]\AppData\Roaming\SeacSync\divesDB.db
3) Copy the database to the same folder as the python script
4) Execute the script with 'python seac_export.py'
5) Import the dives using Subsurface [CTRL + I]. The headers should found automatically.
6) Repeat for each dive.
