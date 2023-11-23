import openai

# client = openai
# client.api_key = "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"

from genPrompt import TransPrompt
import pandas as pd


ts = TransPrompt()

df = pd.read_csv(
    r"C:\Users\asus\OneDrive\Ked data\VS Code\Python\TIAA\SampleDataset.csv"
)
credit_df = df[df["Credit/Debit"] == "Credit"][:20]
debit_df = df[df["Credit/Debit"] == "Debit"][:20]
type = "Debit"
# # print(credit_df.head())
# merch_analy=credit_df[credit_df["Credit/Debit"] == "Credit"].groupby("Merchant")["Transaction_Amount"].sum()
payment_method_debits = (
    debit_df.groupby("Transaction_Type")["Transaction_Amount"].sum().reset_index()
)
pmt = f"""
        Below numerical data represent the payment method used while doing transaction happend that involved in process of transaction for one month,
        {payment_method_debits}
        
        provide the insights for above details by analyzing given data, includes only following formatted output, do not explain it in more depth just predict it and provide 
        for {type} transactions: [maximum transaction {type}ed by which payment method?, minimum transaction {type}ed by which payment method?, which payment method is most suitable for user?]
        and at end provide 2-4 lines suggestion about payment method usage to improve transactions
        """

with open("responses.txt", "w") as txtfile:
    txtfile.write(pmt)

print(pmt)
