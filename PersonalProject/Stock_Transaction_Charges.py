Turnover = input("Enter the Turnover Amount: ")
Brokerage_Amount = 0.01
print(f'Borkerage amount = {Brokerage_Amount}')
Security_Transaction = int(Turnover) * (0.1/100)
NSE_Transaction_Charges = round((int(Turnover) * 0.00325/100), 3)
GST = (Brokerage_Amount + NSE_Transaction_Charges) * 18/100
SEBI_Charges = (15/10000000) * int(Turnover)
print(f'Security Transaction = {Security_Transaction}')
print(f'NSE Transaction Charges = {NSE_Transaction_Charges}')
print(f'GST Charges = {GST}')
print(f'SEBI Charges: {round(SEBI_Charges, 4)}')
Total_Tax = round((Brokerage_Amount + Security_Transaction +
                   NSE_Transaction_Charges + GST + SEBI_Charges), 2)
print(f'Total Tax = {Total_Tax}')
Total_Debit = print(f'Total Debit = {Total_Tax + int(Turnover)}')
