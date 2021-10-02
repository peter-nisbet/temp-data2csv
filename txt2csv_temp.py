import csv

x = 0

#def create_csv(date, amb, xps_temp, axp_temp, total_pwr, QSFP1_temp, QSFP2_temp, QSFP3_temp, QSFP4_temp):
def create_csv(csv_data):
    print(csv_data)
    #with open('temp.csv', 'w') as out_file:
        #writer = csv.writer(out_file)
    writer.writerow(csv_data) 

#with open('temp.csv', 'w') as out_file:
out_file = open('temp.csv', 'w')
writer = csv.writer(out_file)
writer.writerow(("Date", "Time","Ambient Temp (C)", "XPS Temp (C)", "13P Temp (C)", "Total Power (W)", "QSFP 1 Temp (C)", "QSFP 2 Temp (C)", "QSFP 3 Temp (C)", "QSFP 4 Temp (C)"))

with open('test_I_2.txt', 'r') as in_file:
    for l in in_file:
        l = l.strip()
        if l.find('-') != -1:
            date = l.strip("-").replace(" ", "").split(",")
            #print(l.strip("-").replace(" ", ""))
        if l.find('AMBIENT_TEMP') != -1:
            amb = l.strip("C").replace("\t", " ").strip("AMBIENT_TEMP")
            #print(l.strip("C").replace("\t", ","))
        if l.find('XPS_TEMP') != -1:
            xps_temp = l.strip("C").replace("\t", " ").strip("XPS_TEMP")
            #print(l.strip("C").replace("\t", ","))
        if l.find("13P_TEMP") != -1:
            axp_temp = l.strip("C").replace("\t", " ").replace("13P_TEMP","")
            #print(l.strip("C").replace("\t", ","))
        if l.find("TOTAL POWER") != -1:
            total_pwr = l.strip("W").replace("\t", " ").strip("TOTAL POWER")
            #print(l.strip("W").replace("\t", ","))
        if l.find("Temperature QSFP 1") != -1:
            QSFP1_temp = l.strip("C").replace(" : ", " ").replace("Temperature QSFP 1", "")
            #print(l.strip("C").replace(" : ", ","))
        if l.find("Temperature QSFP 2") != -1:
            QSFP2_temp = l.strip("C").replace(" : ", " ").replace("Temperature QSFP 2", "")
            #print(l.strip("C").replace(" : ", ","))
        if l.find("Temperature QSFP 3") != -1:
            QSFP3_temp = l.strip("C").replace(" : ", " ").replace("Temperature QSFP 3", "")
            #print(l.strip("C").replace(" : ", ","))
        if l.find("Temperature QSFP 4") != -1:
            QSFP4_temp = l.strip("C").replace(" : ", " ").replace("Temperature QSFP 4", "")
            csv_data = date.copy()
            csv_data.append(amb)
            csv_data.append(xps_temp)
            csv_data.append(axp_temp)
            csv_data.append(total_pwr)
            csv_data.append(QSFP1_temp)
            csv_data.append(QSFP2_temp)
            csv_data.append(QSFP3_temp)
            csv_data.append(QSFP4_temp)
            create_csv(csv_data)
            #create_csv(date, amb, xps_temp, axp_temp, total_pwr, QSFP1_temp, QSFP2_temp, QSFP3_temp, QSFP4_temp)
            #print(l.strip("C").replace(" : ", ","))
out_file.close()
in_file.close()