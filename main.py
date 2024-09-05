# Libraries

import streamlit as st
from datetime import date
import pandas as pd
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import numpy as np

np.float_ = np.float64

# Constants 
TODAY = date.today().strftime("%Y-%m-%d")
PREDICTION_MIN = 1
PREDICTION_MAX = 5

# Functions

# Plots the stock data graph
def plot_graph(text_box, data) : 
    figure = go.Figure()
    figure.add_trace(go.Scatter(x=data["Date"],y=data["Close"],name = "Close prices"))
    figure.layout.update(title_text = get_name(text_box) + " Stock Data Graph", xaxis_rangeslider_visible = True)
    st.plotly_chart(figure)


# This function is cached to improve efficiency and will load the stock data as a dataframe
@st.cache_data
def load_data(name) :
    data = pd.DataFrame()
    if name : 
        data =yf.download(name, end=TODAY)
        data.reset_index(inplace=True)
    return data


# Cached and will return the name of the stock that is being analyzed
@st.cache_data
def get_name(name) : 
    stock = yf.Ticker(name)
    stock_name = stock.info.get("longName")
    return stock_name


# Cached and uses Prophet ML model to take dataframe of stock prices over time;
# returns dataframe with predictions of {period} years in the future.
@st.cache_data
def get_predictions(df, period) : 
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods = period)

    forecast = model.predict(future)

    st.subheader('Prediction Data')

    fig1 = plot_plotly(model, forecast)
    st.plotly_chart(fig1, theme=None)

    st.write('Yearly and Weekly Trends')
    fig2 = model.plot_components(forecast)
    st.write(fig2)


#-------------------------------------------------------------------------------
def main() : 
    st.title("Stock Predictor")
    text_box = st.text_input("Enter Stock Ticker")

    # Validate that an input is given and the stock ticker exists
    if not load_data(text_box).empty and get_name(text_box): 
        num_of_years = st.slider("Years to predict:", PREDICTION_MIN, PREDICTION_MAX)
        period = num_of_years * 365

        data = load_data(text_box)

        plot_graph(text_box, data)

        df_train = data[["Date", "Close"]] # Specifically get the Date and Close
                                           # prices as a dataframe
        df_train = df_train.rename(columns={"Date" : "ds", "Close": "y"})
                                # ^ Prophet() requires columns named "ds" and "y"
        get_predictions(df_train, period)
        
    else : # If invalid input is given...    vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv         
        st.markdown('<span style="color:red">Please input a correct stock ticker (E.G. MSFT, V, GME)</span>', unsafe_allow_html=True)
           #                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
main()
