import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2
data = yf.download('AAPL',start=start_date, end=end_date, 
progress=False)
1
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
import yfinance as yf
# Get Apple's stock data from yahoo finance
stock = yf.Ticker("AAPL")
data = stock.history(period="1y")
print(data.head())
#ouput
 Open High Low Close 
Date 
2022-01-21 00:00:00-05:00 163.471266 165.370249 161.363504 161.472870 
2022-01-24 00:00:00-05:00 159.096635 161.363477 153.807326 160.687393 
2022-01-25 00:00:00-05:00 158.062630 161.820817 156.113949 158.858017 
2022-01-26 00:00:00-05:00 162.556536 163.441400 156.909320 158.768524 
2022-01-27 00:00:00-05:00 161.512596 162.894575 157.366661 158.301239 
 Volume Dividends Stock Splits 
Date 
2022-01-21 00:00:00-05:00 122848900 0.0 0.0 
2022-01-24 00:00:00-05:00 162294600 0.0 0.0 
2022-01-25 00:00:00-05:00 115798400 0.0 0.0 
2022-01-26 00:00:00-05:00 108275300 0.0 0.0 
2022-01-27 00:00:00-05:00 121954600 0.0 0.0 
Now let’s implement the momentum strategy in Algorithmic 
Trading using Python:
# Calculation of momentum
data['momentum'] = data['Close'].pct_change()
# Creating subplots to show momentum and buying/selling markers
figure = make_subplots(rows=2, cols=1)
figure.add_trace(go.Scatter(x=data.index, y=data['Close'], 
name='Close Price'))
figure.add_trace(go.Scatter(x=data.index, y=data['momentum'], 
name='Momentum', yaxis='y2'))
# Adding the buy and sell signals
figure.add_trace(go.Scatter(x=data.loc[data['momentum'] > 0].index, 
y=data.loc[data['momentum'] > 0]['Close'], mode='markers', 
name='Buy', 
marker=dict(color='green', symbol='triangle-up')))
figure.add_trace(go.Scatter(x=data.loc[data['momentum'] < 0].index,
y=data.loc[data['momentum'] < 0]['Close'], 
mode='markers', name='Sell', 
marker=dict(color='red', symbol='triangle-down')))
figure.update_layout(title='Algorithmic Trading using Momentum 
Strategy',
xaxis_title='Date', yaxis_title='Price')
figure.update_yaxes(title="Momentum", secondary_y=True)
figure.show(
