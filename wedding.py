import csv     # imports the csv module
import os      # imports the os module
import sys     # imports the sys module

f = open(sys.argv[1], 'rb')  # opens the csv file
try:
    reader = csv.reader(f)  # creates the reader object
    action = sys.argv[2]  # grabs the desired action
    next(reader)  # skips the headers
    if action == 'count':
        guest_col = os.environ.get('GUEST_COL', 4)  # sets the guest list column
        guest_list = []  # provisions empty guest list
        for row in reader:  # iterates the rows of the file in order
            [guest_list.append(guest.strip()) for guest in row[guest_col].split(',')]
        print 'Guest count: ' + str(len(guest_list))  # prints guest count
    else:
        print "Actions: count"  # lists available actions
finally:
    f.close()      # closing
