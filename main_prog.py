# Programmer: SUVANKAR DAS
# Mentor: BIDYUT DAS
# Date: 28-03-2022



import pandas as pd
import numpy as np
from datetime import date



def allAbsent(dataset):
    np_dataset = dataset.to_numpy()
    new = []
    new.append(date.today().strftime("%d-%m-%Y"))
    if new[0] == np_dataset[0,-1]:
        np_dataset = np_dataset[:,:-1]

    for i in range(len(np_dataset)-1):
        new.append('A')
    new = np.array(new).reshape(len(new),1)
    
    np_dataset = np.append(np_dataset, new, axis = 1)
    return pd.DataFrame(np_dataset)



def allPresent(dataset):
    np_dataset = dataset.to_numpy()
    new = []
    new.append(date.today().strftime("%d-%m-%Y"))
    if new[0] == np_dataset[0,-1]:
        np_dataset = np_dataset[:,:-1]

    for i in range(len(np_dataset)-1):
        new.append('P')
    new = np.array(new).reshape(len(new),1)
    
    np_dataset = np.append(np_dataset, new, axis = 1)
    return pd.DataFrame(np_dataset)



def somePresent(dataset):
    np_dataset = dataset.to_numpy()
    new = []
    new.append(date.today().strftime("%d-%m-%Y")) 
    if new[0] == np_dataset[0,-1]:
        np_dataset = np_dataset[:,:-1]

    roll_dataset = []
    for i in list(np_dataset[1:,1]):
        roll_dataset.append(int(str(i)[-2:]))

    total = int(input("\nEnter the total number of students present today : "))
    present_list = []
    for i in range(total):
        present_list.append(input(f"Last 2 digits of Student {i+1} Roll NO. : "))
    present_list = [int(i) for i in present_list]

    for i in range(len(np_dataset)-1):
        new.append('-')

    for i in range(len(roll_dataset)):
        if roll_dataset[i] in present_list:
            new[i+1] = 'P'
        else: 
            new[i+1] = 'A'
    
    new = np.array(new).reshape(len(new),1)
    np_dataset = np.append(np_dataset, new, axis = 1)
    return pd.DataFrame(np_dataset)
    


def multipleInsert(dataset):
    np_dataset = dataset.to_numpy()
    new = []
    total_days = int(input("\n\nEnter how many days you want to input : "))

    for i in range(total_days):
        new.append(input(f"\nEnter date {i+1} (DD-MM-YYYY) : "))

        command = input('''Enter an option among these :
    1. All the students are absent.
    2. All the students are presnt.
    3. Some of the students are present.

Enter : ''')

        if command in ['1','2','3']:
            if command == '1':
                for i in range(len(np_dataset)-1):
                    new.append('A')
                new = np.array(new).reshape(len(new),1)
                np_dataset = np.append(np_dataset, new, axis = 1)
                new = []


            if command == '2':
                for i in range(len(np_dataset)-1):
                    new.append('P')
                new = np.array(new).reshape(len(new),1)
                np_dataset = np.append(np_dataset, new, axis = 1)
                new = []
        
            if command == '3':
                roll_dataset = []
                for i in list(np_dataset[1:,1]):
                    roll_dataset.append(int(str(i)[-2:]))

                total = int(input("\nEnter the total number of students present today : "))
                present_list = []
                for i in range(total):
                    present_list.append(input(f"Last 2 digits of Student {i+1} Roll NO. : "))
                present_list = [int(i) for i in present_list]

                for i in range(len(np_dataset)-1):
                    new.append('-')

                for i in range(len(roll_dataset)):
                    if roll_dataset[i] in present_list:
                        new[i+1] = 'P'
                    else: 
                        new[i+1] = 'A'
                
                new = np.array(new).reshape(len(new),1)
                np_dataset = np.append(np_dataset, new, axis = 1)
                new = []
        else:
            print("\nInvalid input. Run the program again.")
    
    return pd.DataFrame(np_dataset)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



print("\nWELCOME !!!\n")

# GET THE MAIN CSV FILE
main_dataset = pd.read_csv('MCA_2023_batch.csv')

command = input('''Enter an option among these :
    1. Just view the records.
    2. All the students are absent.
    3. All the students are presnt.
    4. Some of the students are present.
    5. Insert multiple columns. 

Enter : ''')

if command in ['1','2','3','4','5']:

    if command == '1': # TO READ THE FILE
        print("\n\nExisting dataset :\n\n", main_dataset)

    if command == '2': # WHEN ALL STUDENTS ARE ABSENT
        allAbsent(main_dataset).to_csv('MCA_2023_batch.csv', index = False)
        print("\n\n1 column inserted. Updated dataset :\n\n", pd.read_csv('MCA_2023_batch.csv'))

    if command == '3': # WHEN ALL STUDENTS ARE PRESENT
        allPresent(main_dataset).to_csv('MCA_2023_batch.csv', index = False)
        print("\n\n1 column inserted. Updated dataset :\n\n", pd.read_csv('MCA_2023_batch.csv'))

    if command == '4': #  WHEN SOME STUDENTS ARE PRESENT
        somePresent(main_dataset).to_csv('MCA_2023_batch.csv', index = False)
        print("\n\n1 column inserted. Updated dataset :\n\n", pd.read_csv('MCA_2023_batch.csv'))

    if command == '5': #  WHEN SOME STUDENTS ARE PRESENT
        multipleInsert(main_dataset).to_csv('MCA_2023_batch.csv', index = False)
        print("\n\n1 column inserted. Updated dataset :\n\n", pd.read_csv('MCA_2023_batch.csv'))

else:
    print("\nInvalid input. Run the program again.")

print("\nTHANK YOU !!!\nHit ENTER to exit.")
input() 