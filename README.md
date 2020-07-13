# SeacDBConvert
Short Python Script to unpack SEAC Action DB into individual dives for importing into subsurface.

### Usage
1) Sync your Seac Action to your PC
2) Locate the database file. It is likely in C:\users\\\[username]\AppData\Roaming\SeacSync\divesDB.db
3) Copy the database to the same folder as the python script
4) Execute the script with 'python seac_export.py'
5) Import the dives using Subsurface [CTRL + I]. The headers should found automatically. Multiple Dives can be imported at one time.


### Background
The [Seac Action](https://seacsub.com/product/action/) was released at DEMA 2019. At the time of writing, it is not a supported computer in SubSurface. In order to import the dives, it was necessary to download them using the vedor's proprietary sync cable and software. The dive information was found to be stored in two tables in an SQLite3 Database. To import them into subsurface, they must be converted to CSV files, which this script accomplishes.
