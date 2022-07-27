import csv
rawData = []
expenseData = []
incomeData = []
expenseOutput = []
LookupTable = {}
from pathlib import Path
import os
from pathlib import Path
from .models import Transaction

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class citiReader:

    def __init__(self):
#reads the lookUpTable file and establishes it
        workpathLT = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(workpathLT, "LUTable/LookUpTable.csv"), mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                for key, value in row.items():
                    LookupTable[value] = key

    def citiParse(self, filepath):
        #reads the csv file
        workpath = os.path.dirname(os.path.abspath(__file__))
        with open(str(BASE_DIR)+filepath, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                row.pop('Status')
                row.pop('Member Name')

                # strips the white spaces and converts the numerical values into floats
                for key in row:
                    row[key] = row[key].strip()
                if row['Debit'] == '':
                    row['Debit'] = None
                else:
                    row['Debit'] = float(row['Debit'])

                if row['Credit'] == '':
                    row['Credit'] = None
                else:
                    row['Credit'] = float(row['Credit'])
                rawData.append(row)

        # splits the different data types into expenses or income
        for item in rawData:
            if not item.get("Credit"):
                expenseData.append(item)
            else:
                incomeData.append(item)

        #formats the expense data to the proper output
        for item in expenseData:
            cat = {}
            if LookupTable.get(item['Description']) == None:
                cat['Category'] = ''
            else:
                cat['Category'] = LookupTable.get(item['Description'])
            #item['Date'] = item['Date'].replace('/', '-')
            transaction = Transaction(date = item['Date'], amount = item['Debit'], desc = item['Description'], category = cat['Category'], bank = 'Citibank Credit')
            transaction.save()
            formattedItem = [item['Date'], item['Debit'], item['Description'], cat['Category'], 'Citibank Credit']
            expenseOutput.append(formattedItem)

        workpath = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(workpath, 'output.csv'), 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            for item in expenseOutput:
                spamwriter.writerow(item)