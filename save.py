from max30100 import MAX30100
import time
import csv

sensor = MAX30100()

sensor.enable_spo2()

filename = "ppg_data.csv"

with open(filename, "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(["Red", "IR"])

    while True:
        red, ir = sensor.read_sequential()
        print("Red: {0}, IR: {1}".format(red, ir))
        writer.writerow([red, ir])
        time.sleep(0.1)
