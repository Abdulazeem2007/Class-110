import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].tolist()

population_mean = statistics.mean(data)
print("Population Mean -", population_mean)
population_stdev = statistics.stdev(data)
print ("Standarad Deviation of Population - ", population_stdev )

def random_set_of_mean(counter):
    dataset= []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_figure(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["average"], show_hist= False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0,10], mode = "lines", name= "Mean"))
    fig.show()

def setup():
    mean_list=[]
    for i in range (0,1000):
        set_of_mean= random_set_of_mean(10)
        mean_list.append(set_of_mean)
    show_figure(mean_list)

    mean= statistics.mean(mean_list)
    print("Mean of Sapling Deviation - ", mean)

setup()

def StandardDeviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(10)
        mean_list.append(set_of_means)
    
    st_dev = statistics.stdev(mean_list)
    print("This is the Standard Deviation of Sampled Distribution - ", st_dev)

StandardDeviation()

