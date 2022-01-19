import pandas as pd
import plotly.express as px 

df = pd.read_csv("main.py")
fig = px.scatter(df,x="data",y="cases",color="Country")
fig.show()