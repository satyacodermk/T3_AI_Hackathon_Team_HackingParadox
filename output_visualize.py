import streamlit as st
import time


def typeWritter(summary_text):
    summary_container = st.markdown(
        f"<div style='width:400px'>{''}</div>", unsafe_allow_html=True
    )
    typed = ""
    count = 0
    for char in summary_text:
        if count > 130 and (char == " "):
            count = 0
            char = "\n"

        count += 1
        typed += char
        summary_container.text(typed)
        time.sleep(0.02)  # Adjust the sleep duration for typing speed


def creditdebitsummary():
    data = {
        "Income Rate": 0.65,
        "Expenditure Rate": 0.35,
        "net loss/profit": 245.17,
        "Percentage Income to expenditure": 65,
        "Summary": "The income rate is 65%, expenditure rate is 35%, resulting in a net profit of 245.17. The percentage of income to expenditure is 65%. Suggested actions: Focus on increasing income through additional income sources and consider optimizing expenditure by identifying and reducing non-essential expenses.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass

    # Display Summary with Typewriter Effect
    st.subheader("Summary")

    typeWritter(data["Summary"])
    # Suggestions
    st.subheader("Suggestions")
    st.write("1. Explore additional income sources.")
    st.write("2. Identify and cut down non-essential expenses.")
    st.write("3. Consider optimizing expenditure for better financial health.")


# creditdebitsummary()
def categorysummary():
    data = {
        "Maximum Credit Catgory": "Pension Plans",
        "Minimum Credit Category": "Social Security",
        "Max Credit Expansion Category": "Consulting or Freelancing",
        "Summary": "The analysis indicates that Pension Plans contribute the maximum credited transactions, while Social Security has the minimum. Consulting or Freelancing plays a significant role in increasing income, being the category with the highest credited transactions.",
        "suggestion": "To further improve income based on the analysis:\n1. Focus on maximizing opportunities in Pension Plans for sustained income.\n2. Explore strategies to enhance transactions in Consulting or Freelancing for increased income.\n3. Evaluate and optimize the Social Security category to potentially boost income.\n4. Regularly assess and adapt your credit strategy to ensure a diversified and robust income stream.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass
    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])

    st.header("Suggestion")
    typeWritter(data["suggestion"])


# Create
def merchantanalysis():
    data = {
        "max_credit_merchant": "Electronics Store",
        "min_credit_merchant": "Travel Agency",
        "max_credit_expansion_merchant": "Electronics Store",
        "Summary": "Analysis indicates that the Electronics Store has the highest credited transaction, while the Travel Agency has the lowest. The Electronics Store significantly contributes to the maximum credited transactions, suggesting a potential opportunity for increased income. For optimization, focus on strategies to enhance income generation from the Electronics Store. Consider exploring new revenue streams or promotions.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass

    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])


def locationanalysis():
    data = {
        "total_transaction_amount": 7929.76,
        "average_transaction_amount": 792.98,
        "maximum_transaction_date": "2022-07-07",
        "minimum_transaction_date": "2022-07-02",
        "total_current_amount": 2467942.96,
        "average_current_amount": 246794.30,
        "maximum_current_amount_date": "2022-07-08",
        "minimum_current_amount_date": "2022-07-02",
        "Summary": "The total transaction amount for the month is 7929.76, with an average transaction amount of 792.98. The maximum transaction occurred on 2022-07-07, while the minimum transaction occurred on 2022-07-02. The total current amount is 2467942.96, with an average current amount of 246794.30. The maximum current amount was recorded on 2022-07-08, and the minimum on 2022-07-02.",
        "suggestion": "Analyze the transaction patterns on high and low days to identify potential trends. Consider strategies to increase transactions on lower days and optimize resources on higher transaction days for more efficient financial management.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass

    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])

    # Display Summary with Typewriter Effect
    st.subheader("Suggestions")
    typeWritter(data["suggestion"])


def transmodeanalysis():
    data = {
        "total_transaction_amount": 8480.71,
        "average_transaction_amount": 2826.90,
        "maximum_transaction_type": "Credit Card",
        "minimum_transaction_type": "UPI",
        "Summary": "The total transaction amount for the month is 8480.71, with an average transaction amount of 2826.90. The maximum transaction amount was recorded for Credit Card transactions, while the minimum was for UPI transactions.",
        "suggestion": "Given the higher usage of Credit Card transactions, consider exploring incentives or promotions to encourage more Credit Card usage. Monitor UPI transactions to identify opportunities for growth or optimization.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass
    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])

    # Display Summary with Typewriter Effect
    st.subheader("Suggestions")
    typeWritter(data["suggestion"])


# --------------------------------------------------------------------------------------------------------------------------------
# Debit Analysis Summary Codes


def categorysummary_debit():
    data = {
        "max_debit_category": "Entertainment and Leisure",
        "min_debit_category": "Insurance",
        "max_debit_expansion_category": "Debt Payments",
        "Summary": "The analysis indicates that Entertainment and Leisure have the highest debited transactions, while Insurance has the lowest. Debt Payments significantly contribute to the maximum debited transactions, suggesting a potential area of increased expenditure.",
        "suggestion": "To manage expenses based on the analysis:\n1. Monitor and control Entertainment and Leisure transactions to mitigate high debits.\n2. Evaluate and optimize expenses associated with Debt Payments for potential savings.\n3. Implement cost-effective measures when dealing with Entertainment and Leisure to ensure financial efficiency.\n4. Regularly assess category-wise transactions to identify areas for cost optimization.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "      ", data[k])
        else:
            pass
    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])

    st.header("Suggestion")
    typeWritter(data["suggestion"])


# Create
def merchantanalysis_debit():
    data = {
        "max_debit_merchant": "ATM Withdrawal",
        "min_debit_merchant": "Coffee Shop",
        "max_debit_expansion_merchant": "Rent Payment",
        "Summary": "Analysis indicates that ATM Withdrawal has the highest debited transactions, while Coffee Shop has the lowest. Rent Payment significantly contributes to the maximum debited transactions, suggesting a potential area of increased expenditure.",
        "suggestion": "To optimize expenses based on the analysis:\n1. Monitor and manage ATM Withdrawal transactions to control high debits.\n2. Evaluate and optimize expenses associated with Rent Payment for potential savings.\n3. Implement cost-effective measures when dealing with Rent Payment to ensure financial efficiency.\n4. Regularly assess merchant transactions to identify areas for cost optimization.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass

    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])


def locationanalysis_debit():
    data = {
        "max_debit_city": "thane",
        "min_debit_city": "satara",
        "average_debit_city": "pune",
        "Summary": "Analysis indicates that Thane has the highest debited transactions, while Satara has the lowest. Pune represents the city with an average debit transaction amount.",
        "suggestion": "To optimize expenses based on the analysis:\n1. Evaluate and manage debited transactions in Thane to control high expenses.\n2. Identify opportunities for cost optimization in Satara to maintain financial efficiency.\n3. Implement strategies to maintain a balance in debited transactions in Pune for effective budgeting.\n4. Regularly assess location-wise transactions to identify areas for cost optimization.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass

    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])

    # Display Summary with Typewriter Effect
    st.subheader("Suggestions")
    typeWritter(data["suggestion"])


def transmodeanalysis_debit():
    data = {
        "max_debit_payment_method": "Mobile Payments",
        "min_debit_payment_method": "Online Banking",
        "most_suitable_payment_method": "Online Banking",
        "Summary": "Analysis indicates that Mobile Payments have the highest debited transactions, while Online Banking has the lowest. Online Banking is identified as the most suitable payment method based on transaction patterns.",
        "suggestion": "To improve transactions and optimize the usage of payment methods:\n1. Explore strategies to manage and control debits associated with Mobile Payments.\n2. Evaluate and optimize transactions through Online Banking for potential efficiency.\n3. Encourage and promote the use of Online Banking for a streamlined and user-friendly experience.\n4. Regularly assess payment method usage to identify areas for improvement and user preference.",
    }

    st.subheader("Insights 💡")
    for k in data.keys():
        if k != "Summary" and k != "suggestion":
            st.write(k, "   -   ", data[k])
        else:
            pass
    # Display Summary with Typewriter Effect
    st.subheader("Summary")
    typeWritter(data["Summary"])

    # Display Summary with Typewriter Effect
    st.subheader("Suggestions")
    typeWritter(data["suggestion"])


if __name__ == "__main__":
    # transmodeanalysis()
    pass
