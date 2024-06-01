# CALIBER, 2024.

import sys, csv, re

codes = [{"code":"133..11","system":"readv2"},{"code":"25503","system":"readv2"},{"code":"33153","system":"readv2"},{"code":"22934","system":"readv2"},{"code":"12325","system":"readv2"},{"code":"63118","system":"readv2"},{"code":"41203","system":"readv2"},{"code":"333","system":"readv2"},{"code":"42386","system":"readv2"},{"code":"23514","system":"readv2"},{"code":"9910","system":"readv2"},{"code":"2093","system":"readv2"},{"code":"16552","system":"readv2"},{"code":"24769","system":"readv2"},{"code":"1580","system":"readv2"},{"code":"25149","system":"readv2"},{"code":"23385","system":"readv2"},{"code":"42321","system":"readv2"},{"code":"36333","system":"readv2"},{"code":"28360","system":"readv2"},{"code":"23409","system":"readv2"},{"code":"45178","system":"readv2"},{"code":"38003","system":"readv2"},{"code":"20313","system":"readv2"},{"code":"7419","system":"readv2"},{"code":"3719","system":"readv2"},{"code":"23974","system":"readv2"},{"code":"16315","system":"readv2"},{"code":"45005","system":"readv2"},{"code":"30950","system":"readv2"},{"code":"37113","system":"readv2"},{"code":"97398","system":"readv2"},{"code":"3483","system":"readv2"},{"code":"28985","system":"readv2"},{"code":"42398","system":"readv2"},{"code":"34771","system":"readv2"},{"code":"3394","system":"readv2"},{"code":"15777","system":"readv2"},{"code":"8470","system":"readv2"},{"code":"25097","system":"readv2"},{"code":"20536","system":"readv2"},{"code":"39292","system":"readv2"},{"code":"33006","system":"readv2"},{"code":"16262","system":"readv2"},{"code":"36299","system":"readv2"},{"code":"11251","system":"readv2"},{"code":"4204","system":"readv2"},{"code":"1328","system":"readv2"},{"code":"88373","system":"readv2"},{"code":"42428","system":"readv2"},{"code":"723","system":"readv2"},{"code":"21860","system":"readv2"},{"code":"15950","system":"readv2"},{"code":"3551","system":"readv2"},{"code":"15527","system":"readv2"},{"code":"23508","system":"readv2"},{"code":"27434","system":"readv2"},{"code":"2159","system":"readv2"},{"code":"38325","system":"readv2"},{"code":"954","system":"readv2"},{"code":"50485","system":"readv2"},{"code":"28440","system":"readv2"},{"code":"94917","system":"readv2"},{"code":"54816","system":"readv2"},{"code":"13001","system":"readv2"},{"code":"20079","system":"readv2"},{"code":"20217","system":"readv2"},{"code":"400","system":"readv2"},{"code":"838","system":"readv2"},{"code":"56178","system":"readv2"},{"code":"5055","system":"readv2"},{"code":"21346","system":"readv2"},{"code":"30597","system":"readv2"},{"code":"27385","system":"readv2"},{"code":"50149","system":"readv2"},{"code":"96856","system":"readv2"},{"code":"33188","system":"readv2"},{"code":"36077","system":"readv2"},{"code":"1349","system":"readv2"},{"code":"15313","system":"readv2"},{"code":"60723","system":"readv2"},{"code":"25452","system":"readv2"},{"code":"15404","system":"readv2"},{"code":"94044","system":"readv2"},{"code":"42402","system":"readv2"},{"code":"32984","system":"readv2"},{"code":"15824","system":"readv2"},{"code":"36947","system":"readv2"},{"code":"4925","system":"readv2"},{"code":"20149","system":"readv2"},{"code":"6056","system":"readv2"},{"code":"17802","system":"readv2"},{"code":"59829","system":"readv2"},{"code":"41236","system":"readv2"},{"code":"1540","system":"readv2"},{"code":"31678","system":"readv2"},{"code":"3321","system":"readv2"},{"code":"24055","system":"readv2"},{"code":"33001","system":"readv2"},{"code":"94555","system":"readv2"},{"code":"11103","system":"readv2"},{"code":"16344","system":"readv2"},{"code":"22336","system":"readv2"},{"code":"17538","system":"readv2"},{"code":"29544","system":"readv2"},{"code":"95101","system":"readv2"},{"code":"7869","system":"readv2"},{"code":"97076","system":"readv2"},{"code":"37551","system":"readv2"},{"code":"1522","system":"readv2"},{"code":"10330","system":"readv2"},{"code":"40493","system":"readv2"},{"code":"15020","system":"readv2"},{"code":"12076","system":"readv2"},{"code":"9112","system":"readv2"},{"code":"47411","system":"readv2"},{"code":"59817","system":"readv2"},{"code":"49666","system":"readv2"},{"code":"61291","system":"readv2"},{"code":"47408","system":"readv2"},{"code":"207","system":"readv2"},{"code":"42454","system":"readv2"},{"code":"37265","system":"readv2"},{"code":"27572","system":"readv2"},{"code":"21925","system":"readv2"},{"code":"9612","system":"readv2"},{"code":"15115","system":"readv2"},{"code":"3988","system":"readv2"},{"code":"29543","system":"readv2"},{"code":"54096","system":"readv2"},{"code":"22873","system":"readv2"},{"code":"23445","system":"readv2"},{"code":"4312","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('marital-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["marital---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["marital---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["marital---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
