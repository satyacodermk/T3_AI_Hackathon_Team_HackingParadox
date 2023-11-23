import streamlit as st
import yfinance as yf

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM,Dense,Dropout

from tensorflow import keras
import tensorflow as tf
from kerastuner.tuners import RandomSearch
from keras import layers

import datetime
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import plotly.graph_objects as go

st.markdown("""
<style>
body {
    background-color: #1E1E1E;
    color: white;
}
</style>
""", unsafe_allow_html=True)


class StockMarketPredictor:
    def __init__(self,start=None,end=None,company=None) -> None:
        if start==None or end==None or company==None:
            print("No details provided")
        else:
            self.company_ticker=company
            self.startDate=start
            self.endDate=end

            # final model

            # flag to avoid the issue related to data
            self.flag=False

            self.data=yf.download(self.company_ticker,self.startDate,self.endDate)

            if self.data.empty:
                self.flag=True
                # print(f"Warning: Data for {self.company_ticker} is empty or not availabe")
            else:
                self.data.reset_index(inplace=True)

                # drop null values
                self.data.dropna(inplace=True)

    def isAnyDatasetIssue(self):
        if not self.flag:
            return "Warning: data is not available"
        if self.data.shape[0]<200:
            return "Warning: To small dataset to train DL model"
        else:
            return "No"

               
    def display_trend_for_n_days(self, n_days=100):
        ma_n_days = self.data['Close'].rolling(n_days).mean()

        # Streamlit app
        # st.title(f'Stock Market Price Trend for {n_days*10} Days')

        # Plot the moving average and original Close prices
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(ma_n_days, 'r', label=f'MA {n_days*10} Days')
        ax.plot(self.data['Close'], 'g', label='Close Price')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.legend(loc='upper left')
        ax.set_title('Stock Market Price Trend')

        # Display the plot using Streamlit
        st.pyplot(fig)
    
    def preprocessData(self):
        self.data_train=pd.DataFrame(self.data.Close[0:int(len(self.data)*0.80)])
        self.data_test=pd.DataFrame(self.data.Close[int(len(self.data)*0.80):len(self.data)])

        self.scalar=MinMaxScaler(feature_range=(0,1))
        
        data_train_scale=self.scalar.fit_transform(self.data_train)
        self.data_train_scale=data_train_scale

        x=[]
        y=[]
        for i in range(100,data_train_scale.shape[0]):
            x.append(data_train_scale[i-100:i])
            y.append(data_train_scale[i,0])

        
        self.x_train,self.y_train=np.array(x),np.array(y)
        
        # validation dataset
        data_test_scale=self.scalar.transform(self.data_test)
        self.data_test_scale=data_test_scale
        
    def train_model(self):

        x,y=[],[]
        for i in range(100,self.data_test_scale.shape[0]):
            x.append(self.data_test_scale[i-100:i])
            y.append(self.data_test_scale[i,0])
        
        x_val,y_val=np.array(x),np.array(y)

        # use keras tuner
        def build_lstm_model(hp):
            model = keras.Sequential()

            # First LSTM layer
            model.add(layers.LSTM(units=hp.Int('units_1', min_value=32, max_value=512, step=32),
                                activation='relu',
                                return_sequences=True,
                                input_shape=(self.x_train.shape[1], self.x_train.shape[2])))
            model.add(layers.Dropout(hp.Float('dropout_1', min_value=0.2, max_value=0.5, step=0.1)))

            # Second LSTM layer
            model.add(layers.LSTM(units=hp.Int('units_2', min_value=32, max_value=512, step=32),
                                activation='relu',
                                return_sequences=True))
            model.add(layers.Dropout(hp.Float('dropout_2', min_value=0.2, max_value=0.5, step=0.1)))

            # Third LSTM layer
            model.add(layers.LSTM(units=hp.Int('units_3', min_value=32, max_value=512, step=32),
                                activation='relu',
                                return_sequences=True))
            model.add(layers.Dropout(hp.Float('dropout_3', min_value=0.2, max_value=0.5, step=0.1)))

            # Fourth LSTM layer
            model.add(layers.LSTM(units=hp.Int('units_4', min_value=32, max_value=512, step=32),
                                activation='relu'))
            model.add(layers.Dropout(hp.Float('dropout_4', min_value=0.2, max_value=0.5, step=0.1)))

            # Output layer
            model.add(layers.Dense(1, activation='linear'))

            # Compile the model
            model.compile(optimizer=keras.optimizers.Adam(learning_rate=hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='LOG')),
                        loss='mean_squared_error',
                        metrics=['mean_absolute_error'])

            return model

        tuner = RandomSearch(
            build_lstm_model,
            objective='val_loss',
            max_trials=5,  # Adjust as needed
            executions_per_trial=1,  # Adjust as needed
            directory='my_dir',  # Change to a directory that suits your needs
            project_name='lstm_hyperparameter_tuning')

        # Assuming X_train, y_train, X_val, y_val are your training and validation data
        tuner.search(self.x_train, self.y_train,
                    epochs=10,  # Adjust as needed
                    validation_data=(x_val, y_val))

        # Get the best hyperparameters
        best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

        # Build the model with the best hyperparameters and train it on the entire dataset
        final_model = tuner.hypermodel.build(best_hps)
        final_model.fit(self.x_train, self.y_train, epochs=100, validation_data=(x_val, y_val))

        self.final_model=final_model
    
    def loadPredictModel(self,nDays=100):
        # load model using keras
        model=keras.models.load_model(r'C:\Users\asus\OneDrive\Ked data\VS Code\Python\TIAA\Sock Predictions Model.h5')
        
        # predict the ouput based on past nDays
        pas_nDays=self.data_train.tail(nDays)
        data_test=pd.concat([pas_nDays,self.data_test],ignore_index=True)        
        
        # data scaling
        data_test_scale=self.scalar.fit_transform(data_test)

        # predict results
        x, y=[], []
        for i in range(100,data_test_scale.shape[0]):
            x.append(data_test_scale[i-100:i])
            y.append(data_test_scale[i,0])
        
        x,y=np.array(x),np.array(y)

        # predict price train
        y_predict=model.predict(x)

        scale=1/self.scalar.scale_

        y_predict=y_predict*scale

        y=y*scale

        # Streamlit app
        st.title('Stock Price Prediction Result')

        # Plot the predicted and original prices
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(y_predict, 'r', label='Predicted Value')
        ax.plot(y, 'g', label='Original Price')
        ax.set_xlabel('Time')
        ax.set_ylabel('Price')
        ax.legend()
        ax.set_title('Stock Price Prediction Result')

        # Display the plot using Streamlit
        st.pyplot(fig)


# Main Streamlit app
def main():

    #st.set_page_config(page_title="Stock Price Predictor", page_icon="📈", layout="wide", initial_sidebar_state="expanded")
    st.title('Stock Price Predictor')

    # Choose a company ticker
    selected_company = st.selectbox('Select a Company', [('Google', 'GOOG'), ('Apple', 'AAPL'), ('Microsoft', 'MSFT')])

    # Date selection
    start_date = st.date_input('Select Start Date', datetime.now() - timedelta(days=365))
    end_date = st.date_input('Select End Date', datetime.now())
    

    # create object of Predictor class
    stk=StockMarketPredictor(start=start_date,end=end_date,company=selected_company[1])

    # preprocessData
    stk.preprocessData()
    
    nDays=st.number_input("Enter number of Days",min_value=10,value=10)
    st.subheader(f'Stock Data Visualization for {nDays} days')
    stk.display_trend_for_n_days(nDays)

    # check any issue
    resp=stk.isAnyDatasetIssue()
    if resp=="No":
        pass
    else:
        st.subheader(f'Issue occured: {resp}')
    # Prediction dropdown
    st.subheader('Prediction Options')
    prediction_option = st.selectbox('Choose Prediction Option', ['Predict Trend'])

    # Prediction button
    if st.button('Predict'):
        # Perform prediction based on the selected option
        st.subheader('Prediction Results')
        if prediction_option == 'Predict Trend':
            # Replace this with your actual prediction result
            # st.write('Result for Option 1')
            stk.loadPredictModel()

        elif prediction_option == 'Option 2':
            # Replace this with your actual prediction result
            st.write('Result for Option 2')
        elif prediction_option == 'Option 3':
            # Replace this with your actual prediction result
            st.write('Result for Option 3')

if __name__ == '__main__':
    main()