import plotly.figure_factory as ff
import pandas as pd
import csv 
import plotly.graph_objects as go
import random
import statistics

df=pd.read_csv("data.csv")
data=df["responses"].to_list()
##fig=ff.create_distplot([data],["temp"],show_hist=False)
##fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
        population_mean=statistics.mean(dataset)
    return population_mean

def show_fig(mean_list):
    df=mean_list 
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["interference"],show_hist=False) 
    ##fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN")) 
    fig.show()
    
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_mean=random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    population_mean=statistics.mean(mean_list)
    print("mean of sampling distribution:",population_mean)

##population_mean = statistics.mean(data)
##print("population mean:- ", population_mean)


# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

   