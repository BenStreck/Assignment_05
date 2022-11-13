#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# BStreck, 2022-Nov-13, Replaced list of lists with list of dictionaries
# BStreck, 2022-Nov-13, Added functionality for deleting entries
#------------------------------------------#

# Variables
lstTbl = []  # list of lists to hold data
strFileName = 'CDInventory.txt'  # data storage file

# Main Content
print('\nThe Magic CD Inventory\n')
while True:
    # 1. Display menu and get user input
    print('[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to File\n[x] Exit (Be sure to save before exiting)')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 2. Exit the program if the user chooses to do so
        break
    
    if strChoice == 'l': # no elif necessary, as this code is only reached if strChoice is not 'x'
        # 3. Load existing data if the user chooses to do so
        try:
            file = open(strFileName, 'r')
            print('\nReading Data from File...\nThis will overwrite any unsaved data in the current table...')
            lstTbl = []
            dum1 = [line.strip().split(',') for line in file]
            for row in dum1:
                lstTbl.append({'ID':int(row[0]),'CD Title':row[1],'Artist Name':row[2]})
            file.close()
            print('Done\n')
        except:
            print('{} does not exist...'.format(strFileName))
            file = open(strFileName, 'w')
            file.close()
            print('The file has now been created!\n')
        continue
    
    elif strChoice == 'a':
        # 4. Add data to the table (2D List) each time the user chooses to do so
        ID = len(lstTbl) + 1
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        newdict = {'ID': ID , 'CD Title': strTitle , 'Artist Name': strArtist}
        lstTbl.append(newdict)
        print()
        continue
    
    elif strChoice == 'i':
        # 5. Display the current data each time the user chooses to do so
        print('\nDisplaying Current Data...')
        if len(lstTbl) == 0:
            print('The List of Dictionaries is Currently Empty\n')
        else:
            for row in lstTbl:
                print(row)
            print()
        continue
    
    elif strChoice == 'd':
        # 6. Delete an entry from the CD Inventory each time the user chooses to do so
        print('Deleting an entry from the CD Inventory...')
        print('What is the ID number of the entry you want to delete?')
        dum2 = int(input('Enter ID Number Here: '))
        if dum2 < 1:
            print('\nID Number Invalid...\nNo Entries Deleted\n')
        elif dum2 > len(lstTbl):
            print('\nID Number Invalid...\nNo Entries Deleted\n')
        else:
            lstTbl = list(filter(lambda i: i['ID'] != dum2, lstTbl))
            print('\nEntry Deleted')
            print('Relabeling ID Numbers...')
            i = 1
            for row in lstTbl:
                row['ID'] = i
                i += 1
            print('ID numbers have been updated\n')
        continue
    
    elif strChoice == 's':
        # 7. Save the data to a text file CDInventory.txt each time the user chooses to do so
        print('Saving Updated Inventory...')
        file = open(strFileName, 'w')
        for row in lstTbl:
            values = []
            items = row.items()
            for item in items:
                values.append(item[1])
            file.write('{},{},{}\n'.format(values[0],values[1],values[2]))
        file.close()
        print('Done\n')
        continue
    
    else:
        print('Invalid Input\nPlease choose either l, a, i, d, s or x\n')
