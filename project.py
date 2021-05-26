import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go 
gender=[]
mathscore=[]

for i in range(0,1000):

    d1=random.randint(1,6)
    d2=random.randint(1,6)
    mathscore.append(d1+d2)
    gender.append(i)
print(f"mean of the data is {statistics.mean(mathscore)}")
print(f"median of the data is {statistics.median(mathscore)}")
print(f"mode of the data is {statistics.mode(mathscore)}")
print(f"standarddeviation of this data{statistics.stdev(mathscore)}")

mean=statistics.mean(gender)
mode=statistics.mode(gender)
median=statistics.median(gender)
sd=statistics.stdev(gender)
firstSDstart,firstSDend=mean-sd,mean+sd
secSDstart,secSDend=mean-(2*sd),mean+(2*sd)
thirdSDstart,thirdSDend=mean-(3*sd),mean+(3*sd)
listOfdatawithin1SD=[result for result in gender if result>firstSDstart and result< firstSDend]
listOfdatawithin2SD=[result for result in gender if result>secSDstart and result< secSDend]
listOfdatawithin3SD=[result for result in gender if result>thirdSDstart and result< thirdSDend]
print("{} % of data lies between 1 standarddeviation".format(len(listOfdatawithin1SD)*100/len(gender)))
print("{} % of data lies between 2 standarddeviation".format(len(listOfdatawithin2SD)*100/len(gender)))
print("{} % of data lies between 3 standarddeviation".format(len(listOfdatawithin3SD)*100/len(gender)))
