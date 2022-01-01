import csv
header=['first_name','last_name','phone_no','email']
data = ['Tom','Hardy','7485961425']
with open('test.csv','w',encoding='UTF8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(data)