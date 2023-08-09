# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J34..00","system":"readv2"},{"code":"110120.0","system":"med"},{"code":"12086.0","system":"med"},{"code":"24703.0","system":"med"},{"code":"256.0","system":"med"},{"code":"31732.0","system":"med"},{"code":"33779.0","system":"med"},{"code":"34691.0","system":"med"},{"code":"44233.0","system":"med"},{"code":"48153.0","system":"med"},{"code":"4987.0","system":"med"},{"code":"60697.0","system":"med"},{"code":"62920.0","system":"med"},{"code":"63180.0","system":"med"},{"code":"68880.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diaphragmatic-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hernia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hernia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hernia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
