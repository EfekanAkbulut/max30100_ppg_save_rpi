# max30100_ppg_save_rpi

Requirements:
sudo apt-get install python-smbus
pip install max30100


In this script, a CSV file is created with the name "ppg_data.csv". The script opens the CSV file in write mode and creates a writer object using the csv library. The writer object is used to write a header row to the CSV file with the column names "Red" and "IR".

Inside the while loop, the script reads PPG data from the MAX30100 sensor and prints it to the console. The script also writes the PPG data to the CSV file using the writer object. The script waits for 100 milliseconds between each reading to avoid overwhelming the sensor.

When you run this modified script, it will continuously read PPG data from the sensor and save it to the "ppg_data.csv" file in the same directory as the script. You can open the CSV file in a spreadsheet program like Microsoft Excel to visualize and analyze the PPG data.
