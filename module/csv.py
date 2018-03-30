import csv

with open('mycsv.csv','w',newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['name','sal','add'])
    thewriter.writerow(['uday','25000','vzm'])

#for execution better to go to pycharm ide
