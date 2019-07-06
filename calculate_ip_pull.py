import sys
import ipaddress

try:
    listIP = sys.argv[1:][0].split(",")
except (IndexError):
    print('Add line with ip addresses')
    exit()

templList = []
for selected_ip in listIP:
    templList.append(ipaddress.ip_address(selected_ip))

templList.sort()

try:
    select_part_of_pull = sys.argv[2:][0]
except (IndexError):
    print("Select first or last")
    exit()

if select_part_of_pull == 'first':
    print(templList[0])
elif select_part_of_pull == 'last':
    print(templList[-1])
else:
    print(templList)



