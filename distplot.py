import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].tolist()

fig = ff.create_distplot([data], ["average"], show_hist= False)
fig.show()