import random
import datetime
import pandas as pd
categories = ["Health", "Entertainment", "Utilities", "Savings", "Debt Repayment", "Investments"]

transactions= []
def amount(cat):
    if cat=='Health'or cat=='Debt Repayment':
        return round(random.uniform(300, 10000),3)
    elif cat=='Entertainment':
        return round(random.uniform(100, 800),3)
    elif cat=='Utilities':
        return round(random.uniform(100, 750),3)
    elif cat=='Savings':
        return round(random.uniform(500, 2000),3)
    elif cat=='Rent':
        return round(random.uniform(4000, 10000),3)
    elif cat=="Investments":
        return round(random.uniform(1500,7000),3)
    
# for _ in range(10000): 
#     transaction = {
#         "date": datetime.date(2023, random.randint(1, 12), random.randint(1, 28)),
#         "category": random.choice(categories),  # Random category
#         "payment_method": random.choice(["Credit Card", "Debit Card", "Cash","UPI"]) , # Random payment method
#         "amount": amount(transactions[_]["category"])  # Random amount between 1 and 500
#     }
#     transactions.append(transaction)
transactions=[]
for month in range(1,12):
    # transaction={
    #     "category":"Rent",
    #     "date": datetime.date(2023, month, random.randint(1, 28)),
    #     "payment_method": random.choice(["Credit Card", "Debit Card", "Cash","UPI"]) , # Random payment method
    #     "amount": amount("Rent")  # Random amount between 1 and 500
    # }

    # transactions.append(transaction)
    # for day in range(1,28):
    #     for iter in range(random.randint(2,7)):
    #         cat=random.choice(categories)
    #         transaction={
    #         "category":cat,
    #         "date": datetime.date(2023, month, day),
    #         "payment_method": random.choice(["Credit Card", "Debit Card", "Cash","UPI"]) , # Random payment method
    #         "amount": amount(cat)  # Random amount between 1 and 500
    #         }
    #         transactions.append(transaction)
    
    transaction={
        
    }





        # append the data to the dataaet
df=pd.DataFrame(transactions)
df.to_csv("Sample.csv")



