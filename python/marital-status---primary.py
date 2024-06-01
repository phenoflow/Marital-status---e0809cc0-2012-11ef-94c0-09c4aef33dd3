# CALIBER, 2024.

import sys, csv, re

codes = [{"code":"13H4.11","system":"readv2"},{"code":"13H4200","system":"readv2"},{"code":"13H4.12","system":"readv2"},{"code":"13H4213","system":"readv2"},{"code":"13IL300","system":"readv2"},{"code":"13H4211","system":"readv2"},{"code":"13H4212","system":"readv2"},{"code":"13HV400","system":"readv2"},{"code":"13H5.00","system":"readv2"},{"code":"13HT114","system":"readv2"},{"code":"1333.13","system":"readv2"},{"code":"13H4100","system":"readv2"},{"code":"13IL200","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('marital-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["marital-status---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["marital-status---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["marital-status---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
