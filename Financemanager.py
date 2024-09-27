import csv
import gspread
import time

month = "august"

file = f"scotia_{month}.csv"
transaction_list = []

def scotiaFin(file):
    with open(file,mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            category = "OTHER"
            name = row[1]

            for words in name:
                if "AMZN" in name or "AMAZON.CA" in name:
                    name = "AMAZON PURCHASE"
                    category = "GENERAL"
                
                elif "LYFT" in name:
                    name = "LYFT"
                    category = "TRANSPORTATION"
                
                elif "UBER" in name:
                    ran_list = name.split(" ")
                    if "*TRIP" in ran_list or "TRIP" in ran_list or "UBR*" in ran_list or "CANADA/UBERTRIP" in ran_list:
                        name = "UBER RIDE"
                        category = "TRANSPORTATION"
                    elif "*EATS" in ran_list or "CANADA/UBEREATS" in ran_list or "UBER*" in ran_list:
                        name = "UBER EATS"
                        category = "FOOD"
                
                elif "COCA" in name or "ADA*VENDING" in name:
                    name = "VENDING MACHINE"
                    category = "FOOD"
                    
                elif "BOOSTER" in name:
                    name = "BOOSTER JUICE"
                    category = "FOOD"
                
                elif "TRAINLINE" in name:
                    if name == "TRAINLINE                LONDON AMT             4.99 (APPLE PAY) ":
                        name = "TRAIN COST"
                        category = "TRANSPORTATION"

                elif "Zara.com" in name or "SAUCE THE PLUG" in name or "G* GOAT231#13462" in name:
                    if "Zara.com" in name:
                        name = "ZARA"
                    elif "G*" in name:
                        name = "GOAT"
                    elif "SP" in name:
                        name = "NO SAUCE THE PLUG"
                    category = "CLOTHES"

                elif "FROM" in name:
                    if name == "          FROM - *****05*3553 ":
                        name = "CHECKINGS ACCOUNT"

                    elif name == "          FROM - *****11*4986 ":
                        name = "SAVINGS ACCOUNT"
                    
                    else:
                        name = "SECONDARY ACCOUNT"
                    category = "MONEY DEPOSITED"

                elif "Prime" in name or "APPLE.COM/BILL" in name or "FREEDOM" in name or "APOLLO" in name:
                    if "APPLE.COM/BILL" in name: 
                        name = "APPLE BILL"
                    
                    elif name == "Amazon.ca Prime Member   amazon.ca/priBC ":
                        name = "AMAZON PRIME"
                    
                    elif name == "FREEDOM MOBILE           877-946-3184 ON ":
                        name = "FREEDOM PHONE BILL"

                    elif name == "APOLLO INSURANCE         VANCOUVER    BC " or "FINSHORE" in name:
                        name = "APOLLO INSURANCE"

                    category = "SUBSCRIPTION"
                
                elif "Microsoft*Xbox" in name or "MICROSOFT*XBOX" in name:
                    name = "XBOX PAYMENT"
                    category = "SUBSCRIPTION"
                
                elif "CHATGPT" in name:
                    name = "CHATGPT SUBSCRIPTION"
                    category = "SUBSCRIPTION"
                
                elif "Go" in name:
                    name = "GO TRANSIT"
                    category = "TRANSPORTATION"

                elif "APPLE.COM/BILL" in name:
                    name = "APPLE PAYMENT"
                    category = "SUBSCRIPTION"
                
                elif "DOMINOS" in name:
                    name = "DOMINOS PIZZA"
                    category = "FOOD"

                elif "MANDARIN" in name:
                    name = "MANDARIN"
                    category = "FOOD"
                
                elif "MCMASTER" in name:
                    name = "MCMASTER STORE"
                    category = "GENERAL"
                
                elif "PRESTO" in name:
                    name = "PRESTO MOBILE APP"
                    category = "TRANSPORTATION"
                
                elif "QUIK" in name:
                    name = "QUIK CHIC"
                    category = "FOOD"

                elif "PlayStation" in name:
                    name = "PLAYSTATION PAYMENT"
                    category = "SUBSCRIPTION"
                
            amount = float(row[2])
            transaction = (date,name,amount,category)
            print(transaction)
            transaction_list.append(transaction)
        
        return transaction_list

# file format is  [DATE, NAME OF TRANSACTION, PRICE] 

sa = gspread.service_account()
sh = sa.open("Personal Finances")
wks = sh.worksheet(f"{month}")

rows = scotiaFin(file)
for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2]],7)
    time.sleep(2)
