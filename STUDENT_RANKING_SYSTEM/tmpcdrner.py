# import numpy as np
# import pandas as pd
# import csv
# import matplotlib.pyplot as plt
import pandas as pd

print("**********************************************************************")
print("******************************WELCOME*********************************")
print("**********************************************************************")

print('\n')
od = pd.read_csv('student_data.csv')
df = pd.DataFrame(od)
#print(pd)


#Code for Faculty review
facrev = []
for i in df['Faculty review']:
    i=int(i)
    if 7.5<i<=10:
        facrev.append(i*1.25)
    elif 5<i<=7.5:
        facrev.append(i*1.25)
    elif 2.5<i<=5:
        facrev.append(i*1.25)
    elif 0<i<=2.5:
        facrev.append(i*1.25)
    else:
        facrev.append(0)

#code for time invested
time_inv = []
for i in df['Time Invested']:
    i=int(i)
    if 12<i<=15:
        time_inv.append(12.5)
    elif 9<i<=12:
        time_inv.append((5/6)*12.5)
    elif 9<i<=12:
        time_inv.append((4/6)*12.5)
    elif 6<i<=9:
        time_inv.append((3/6)*12.5)
    elif 3<i<=6:
        time_inv.append((2/6)*12.5)
    else:
        time_inv.append(3)

# Total points of extracurricular
exCur=[]
for i,j in zip(facrev,time_inv):
    exCur.append(i+j) 

#Code for GPA
Gpa = []
for i in df['GPA']:
    if i==4:
        Gpa.append(25)
    elif 3.75<=i<4:
        Gpa.append((6/7)*25)
    elif 3.5<=i<3.75:
        Gpa.append((5/7)*25)
    elif 3.25<=i<3.5:
        Gpa.append((4/7)*25)
    elif 3<=i<3.25:
        Gpa.append((3/7)*25)
    elif 2.75<=i<3:
        Gpa.append((2/7)*25)
    elif 2.5<=i<2.75:
        Gpa.append((1/7)*25)
    else:
        Gpa.append(0)

#Code for internships
internships = []
for i in df['Internships']:
    i=int(i)
    if i==4:
        internships.append(25)
    elif i==3:
        internships.append(0.75*25)
    elif i==2:
        internships.append(0.5*25)
    elif i==1:
        internships.append(0.25*25)

# Code for skills
libasic,liint,liadv=[],[],[]
def basicSkills(basic_count):
    if basic_count==3:
        libasic.append(33)
    elif basic_count==2:
        libasic.append(22)
    elif basic_count==1:
        libasic.append(11)
    else:
        libasic.append(0)

def interSkills(inter_count):
    if inter_count==5:
        liint.append(33)
    elif inter_count==4:
        liint.append(26.4)
    elif inter_count==3:
        liint.append(19.8)
    elif inter_count==2:
        liint.append(13.2)
    elif inter_count==1:
        liint.append(6.6)
    else:
        liint.append(0)

def advSkills(adv_count):
    if adv_count==5:
        liadv.append(33)
    elif adv_count==4:
        liadv.append(26.4)
    elif adv_count==3:
        liadv.append(19.8)
    elif adv_count==2:
        liadv.append(13.2)
    elif adv_count==1:
        liadv.append(6.6)
    else:
        liadv.append(0)


basic=['C++','Java','Python']
inter=['Appdev','Webdev','DBMS','Cloud','Cyber']
adv=['MLN','NLP','Fuzzylogic','Expertsystem','Datascience']
for i,j,k in zip(df['Basic'], df['Intermediate'], df['Advanced']):
    basic_count=sum(skill1 in i for skill1 in basic)
    inter_count=sum(skill2 in j for skill2 in inter)
    adv_count=sum(skill3 in k for skill3 in adv)
    basicSkills(basic_count)
    interSkills(inter_count)
    advSkills(adv_count)

Skills=[]
for i,j,k in zip(libasic,liint,liadv):
    Skills.append(i+j+k)
# print('Skills:\n',Skills)
# print('Academics:\n',Gpa)
# print('Extra curricular:\n',exCur)
# print('Internships:\n',internships)

# Total 
#percentages: 
# Skills-35  Academics-25  Internships-25  Extracurricular-15
TotalRating=[]
# for i,j,k,l in zip(Skills,Gpa,exCur,internships):
#     TotalRating.append((i*0.35)+(j)+(k)+(l*0.6))
# print('Total Rating:\n',TotalRating)

#  User input for percentage of different components of rating system
skper=float(input('Enter percentage for Skills\n'))
gpaper=float(input('Enter percentage for Academics\n'))
internper=float(input('Enter percentage for Internships\n'))
excurper=float(input('Enter percentage for Extraurricular activities\n'))
for i,j,k,l in zip(Skills,Gpa,exCur,internships):
    TotalRating.append((i*(skper/100))+(j*(gpaper/25))+(k*(internper/25))+(l*(excurper/25)))
df['Rating']=pd.DataFrame(TotalRating)
print('Top students in CE')
topCE=pd.DataFrame(df['Name'].where(df.Branch=='CE').dropna())
topCE['Rating']=df['Rating'].where(df.Branch=='CE').dropna()
print(topCE.sort_values(by='Rating',ascending=False).head(5))