import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr
from statsmodels.tsa.arima.model import ARIMA
from numpy.random import default_rng
import numpy_financial as npf
from numpy.ma.extras import average
import genPrompt
tsaobj=genPrompt.TransPrompt()
from genAiUtils import gptLLM
#Enter your API Key Here
gpt=gptLLM('')

# 1. Trend Analysis
def trend_analysis(x_col, y_col):
    model = LinearRegression()
    x_col = pd.to_datetime(x_col)
    x_col = x_col.apply(lambda x: x.timestamp())

    # Reshape X to a 2D array
    X = x_col.values.reshape(-1, 1)
    model.fit(X, y_col)
    slope = model.coef_[0]
    return slope

# 2. Correlation Analysis
def correlation_analysis( x_col, y_col):
    correlation,_= pearsonr(x_col[:list(min(x_col.shape,y_col.shape))[0]], y_col[:list(min(x_col.shape,y_col.shape))[0]])
    return correlation

# 3. Forecasting Future Expenses (ARIMA)
def forecast_expenses(data, target_col):
    model = ARIMA(target_col, order=(5,1,0))
    results = model.fit()
    forecast = results.get_forecast(steps=12)  # Adjust steps as needed
    pm=forecast.predicted_mean

    return "Minimum = "+ str(min(pm)) +"\n"+ "Maximum = "+ str(max(pm))+"\n" +"Average = "+ str(average(pm))  

# 4. Risk Assessment
def risk_assessment(data, target_col):
    std_dev = np.std(target_col)
    variance = np.var(target_col)
    return std_dev, variance

# 5. Monte Carlo Simulation
def monte_carlo_simulation(data, target_col):
    rng = default_rng()
    simulated_data = rng.normal(target_col.mean(), target_col.std(), 1000)
    return simulated_data

# 6. Optimization for Investment (Simple Example)
def optimize_investment(data, asset_col, return_col):
    
    asset_col = pd.Series(asset_col)
    return_col = pd.Series(return_col)

    # Ensure lengths match and trim if necessary
    min_length = min(len(asset_col), len(return_col))
    asset_col = asset_col[:min_length]
    return_col = return_col[:min_length]

    total_assets = asset_col.sum()
    weights = asset_col / total_assets
    returns = return_col.reset_index(drop=True) * weights.reset_index(drop=True)
    optimal_return = returns.sum()

    return optimal_return

# 7. Cash Flow Projection
def cash_flow_projection(data, inflow_col, outflow_col):
    min_length=min(len(inflow_col),len(outflow_col))
    inflow_col=inflow_col[:min_length]
    outflow_col=outflow_col[:min_length]
    net_cash_flow = inflow_col.reset_index(drop=True) - outflow_col.reset_index(drop=True)
    present_value = npf.npv(0.05, net_cash_flow)  # Assuming discount rate of 5%
    return net_cash_flow,present_value

def parametersForAPI():
    trend_slope = trend_analysis(df[df["Credit/Debit"]=="Debit"]['Transaction_Date'],df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"])
    correlation_coefficient = correlation_analysis(df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"], df[df["Credit/Debit"]=="Credit"]["Transaction_Amount"])
    # print(correlation_coefficient)
    future_expenses_forecast = forecast_expenses(df, df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"])
    std_dev, variance = risk_assessment(df, df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"])
    simulated_data = monte_carlo_simulation(df, df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"])
    optimal_return = optimize_investment(df, df[df["Credit/Debit"]=="Credit"]["Transaction_Amount"], df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"])
    net_cash_flow, present_value = cash_flow_projection(df, df[df["Credit/Debit"]=="Credit"]["Transaction_Amount"], df[df["Credit/Debit"]=="Debit"]["Transaction_Amount"])
    return {
        'incomeVsExpenditureTrendSlope':trend_slope,
        'incomeVsExpenditureCorrelationCoefficient':correlation_coefficient,
        'futureExpenseForecast':future_expenses_forecast,
        'montoCarloSimulationOnExpenditure':simulated_data,
        'optimalReturnValue':optimal_return,
        'stdDevAndVarianceOfExpenditure':[std_dev,variance],
        'cashFlowProjection':[net_cash_flow,present_value]   
    }

st.set_page_config(
    page_title=" TIAA T3 Hackathon", page_icon="	:bar_chart:", layout="wide"
)


st.title(" 	:bar_chart: TIAA T3 Hackathon")
st.markdown(
    "<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True
)

fl = st.file_uploader(
    ":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"])
)
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding="ISO-8859-1")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    st.write(gpt.generate_response(tsaobj.getStatAnalysisPrompt(parametersForAPI())))

    # parametersForAPI()
    credit_df = df[df["Credit/Debit"] == "Credit"]
    debit_df = df[df["Credit/Debit"] == "Debit"]

    total_debit_amount = debit_df["Transaction_Amount"].sum()
    total_credit_amount = credit_df["Transaction_Amount"].sum()

    # 2. Compare Average Amount
    average_debit_amount = debit_df["Transaction_Amount"].mean()
    average_credit_amount = credit_df["Transaction_Amount"].mean()

    # 3. Compare Transaction Counts
    debit_count = len(debit_df)
    credit_count = len(credit_df)

    st.title("Income vs. Expenditure Analysis")
    # Calculate income and expenditure
    income = credit_df["Transaction_Amount"].sum()
    expenditure = debit_df["Transaction_Amount"].sum()
    
    data = pd.DataFrame(
        {"Type": ["Income", "Expenditure"], "Amount": [income, expenditure]}
    )
    
    _,__,___=st.columns(3)
    with __:
        fig = px.pie(data, names="Type", values="Amount", title="Income vs. Expenditure")
        st.plotly_chart(fig)
        
    category_data = (
        credit_df.groupby("Transaction_Category")["Transaction_Amount"]
        .sum()
        .reset_index()
    )
    numberOfIncomeSources=len(category_data)
    cd={'credit': {
    'total_credit_amount': {total_credit_amount},
    'num_credit_transactions': {credit_count},
    'avg_credit_amount': {average_credit_amount},
    'income_from_sources': {numberOfIncomeSources}
    }           
    }
    dd={
    'debit': {
    'total_debit_amount': {total_debit_amount},
    'num_debit_transactions': {debit_count},
    'avg_debit_amount': {average_debit_amount},
    'expenditure_for_month': {total_debit_amount}
    }
    }
    prompt_for_income_VS_Expenditure=tsaobj.getCreditDebitSummaryPrompt(credit_details=cd,debit_details=dd)
    st.write(gpt.generate_response(prompt_for_income_VS_Expenditure))
        
    tab1, tab2 = st.tabs(["Income Analysis", "Expenditure Analysis"])
    with tab1:
        st.title("Income Analysis")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Total Credit Amount")
            st.subheader(f":green {total_credit_amount}")

        with col2:
            st.header("Average Credit Amount")
            st.subheader(f"{average_credit_amount}")

        with col3:
            st.header("Number of Transactions")
            st.subheader(f"{credit_count}")

        st.write("\n")
        st.write("\n")
        st.write("\n")

        with st.expander("Time Series Analysis"):
            time_series_data = credit_df.groupby("Transaction_Date").sum()
            _,__,___=st.columns(3)
            with __:
                fig = px.line(
                    time_series_data, x=time_series_data.index, y="Transaction_Amount"
                )
                st.plotly_chart(fig)     
                

        with st.expander("Merchant Analysis"):
            merchant_credit = (
                credit_df[credit_df["Credit/Debit"] == "Credit"]
                .groupby("Merchant")["Transaction_Amount"]
                .sum()
            )
            _,__,___=st.columns(3)
            with __:
                fig = px.bar(
                    merchant_credit, x=merchant_credit.index, y="Transaction_Amount"
                )
                st.plotly_chart(fig)
            st.subheader("Generative AI Summary: ")
            st.write(gpt.generate_response(tsaobj.getMerchantAnalysisPrompt(1,merchant_credit,'credit')))



        with st.expander("Location wise analysis"):
            st.header("Credit Transactions by Location")
            location_debits = (
                credit_df.groupby("Location")["Transaction_Amount"].sum().reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                fig_location = px.bar(
                    location_debits,
                    x="Location",
                    y="Transaction_Amount",
                    title="Credit Transactions by Location",
                )
                st.plotly_chart(fig_location)
            st.subheader("Generative AI Summary: ")
            st.write(gpt.generate_response(tsaobj.getLocAnalysisPrompt(1,location_debits,'credit')))
            
            
            
        with st.expander("Payment Method Analysis"):
            st.header("Payment Method Analysis")
            # Group the data by payment method and calculate the total credit amount
            payment_data = (
                credit_df.groupby("Transaction_Type")["Transaction_Amount"]
                .sum()
                .reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                fig = px.bar(
                    payment_data,
                    x="Transaction_Type",
                    y="Transaction_Amount",
                    text="Transaction_Amount",
                )
                fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
                fig.update_layout(title="Credit Amount by Payment Method")
                st.plotly_chart(fig)
            st.subheader("Generative AI Summary: ")
             
            st.write(gpt.generate_response(tsaobj.getPaymentMethodAnalysisPrompt(1,payment_data,'credit')))


        with st.expander("Transaction Category Analysis"):
            st.header("Transaction Category Analysis")
            # Group the data by transaction category and calculate the total credit amount
            category_data = (
                credit_df.groupby("Transaction_Category")["Transaction_Amount"]
                .sum()
                .reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                # Create a Plotly pie chart showing credit amount by transaction category
                fig = px.pie(
                    category_data,
                    names="Transaction_Category",
                    values="Transaction_Amount",
                )
                fig.update_layout(title="Credit Amount by Transaction Category")
                st.plotly_chart(fig)
            st.subheader("Generative AI Summary: ")
             
            st.write(gpt.generate_response(tsaobj.getCategoryAnalysisPrompt(1,category_data,'credit')))
            



    with tab2:
        st.title("Expenditure Analysis")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Total Debit Amount")
            st.subheader(f"{total_debit_amount}")

        with col2:
            st.header("Number of Transactions")
            st.subheader(f"{debit_count}")

        with col3:
            st.header("Maximum Debit Amount")
            st.subheader(debit_df["Transaction_Amount"].max())

        # 2. Debit Transactions by Merchant
        st.write("\n")
        st.write("\n")
        st.write("\n")
        with st.expander("Debit Transactions by Merchant"):
            dm1, dm2 = st.columns(2)
            merchant_debits = (
                debit_df.groupby("Merchant")["Transaction_Amount"].sum().reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                fig_merchant = px.bar(
                    merchant_debits,
                    x="Merchant",
                    y="Transaction_Amount",
                    title="Debit Transactions by Merchant",
                )
                st.plotly_chart(fig_merchant)
            st.subheader("Generative AI Summary: ")
             
            st.write(gpt.generate_response(tsaobj.getMerchantAnalysisPrompt(1,merchant_debits,'debit')))

        # 3. Debit Transactions by Location
        with st.expander("Debit Transactions by Location"):
            lda1,lda2=st.columns(2)
            location_debits = (
                debit_df.groupby("Location")["Transaction_Amount"].sum().reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                fig_location = px.bar(
                    location_debits,
                    x="Location",
                    y="Transaction_Amount",
                    title="Debit Transactions by Location",
                )
                st.plotly_chart(fig_location)
            st.subheader("Generative AI Summary: ")
             
            st.write(gpt.generate_response(tsaobj.getLocAnalysisPrompt(1,location_debits,'debit')))

        # 4. Debit Transactions by Payment Method
        with st.expander("Debit Transactions by Payment Method"):
            pa1,pa2=st.columns(2)
            payment_method_debits = (
                debit_df.groupby("Transaction_Type")["Transaction_Amount"]
                .sum()
                .reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                fig_payment_method = px.pie(
                    payment_method_debits,
                    names="Transaction_Type",
                    values="Transaction_Amount",
                    title="Debit Transactions by Payment Method",
                )
                st.plotly_chart(fig_payment_method)
            st.subheader("Generative AI Summary: ")
             
            st.write(gpt.generate_response(tsaobj.getPaymentMethodAnalysisPrompt(1,payment_method_debits,'debit')))

        # 5. Debit Transactions by Category
        with st.expander("Debit Transactions by Category"):
            ca1,ca2=st.columns(2)
            category_debits = (
                debit_df.groupby("Transaction_Category")["Transaction_Amount"]
                .sum()
                .reset_index()
            )
            _,__,___=st.columns(3)
            with __:
                fig_category = px.pie(
                    category_debits,
                    names="Transaction_Category",
                    values="Transaction_Amount",
                    title="Debit Transactions by Category",
                )
                st.plotly_chart(fig_category)
            st.subheader("Generative AI Summary: ")
             
            st.write(gpt.generate_response(tsaobj.getCategoryAnalysisPrompt(1,category_debits,'debit')))

        # # 6. Time-based Analysis
        # st.header("Time-based Analysis")
        # debit_df["Transaction_Date"] = pd.to_datetime(
        #     debit_df["Transaction_Date"], format="%Y-%m-%d"
        # )
        # debit_df["Year"] = debit_df["Transaction_Date"].dt.year
        # debit_df["Month"] = debit_df["Transaction_Date"].dt.month

        # monthly_debits = (
        #     debit_df[debit_df["Credit/Debit"] == "Debit"]
        #     .groupby(["Year", "Month"])["Transaction_Amount"]
        #     .sum()
        #     .reset_index()
        # )
        # fig_time_series = px.line(
        #     monthly_debits,
        #     x="Month",
        #     y="Transaction_Amount",
        #     line_group="Year",
        #     labels={"Transaction_Amount": "Total Debit Amount"},
        #     title="Monthly Debit Trends",
        # )
        # st.plotly_chart(fig_time_series)

        
        # # 8. Transaction Notes Analysis
        # st.header("Transaction Notes Analysis")
        
        # # 9. Visualizations (e.g., Histogram of Debit Amounts)
        # st.header("Visualizations")
        # st.subheader("Histogram of Debit Amounts")
        # fig_histogram = px.histogram(
        #     debit_df[debit_df["Credit/Debit"] == "Debit"],
        #     x="Transaction_Amount",
        #     title="Distribution of Debit Amounts",
        # )







