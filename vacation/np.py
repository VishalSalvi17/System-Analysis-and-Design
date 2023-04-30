import numpy as np
def Naive(table,condition):
    length_table=len(table)
    length_row=len(table[0])
    last_row=table[:,length_row-1]
    unique_val,count=np.unique(table[:,length_row-1],return_counts=True)
#Step1
prob = []
int=count
for i in range(len(count)):
    prob.append(count[i]/length_table)
#Step2
count_in=[1]*len(count)
for i in range(len(condition)):
    col=table[:,i]
c1,c2=0,0
for j in range(length_table):
    if col[j] == condition[i]:
        if last_row[j] == unique_val[0]:
            c1 += 1
    elif last_row[j] == unique_val[1]:
        c2 += 1
count_in[0] = count_in[0] * (c1/ count[0])
count_in[1] = count_in[1] * (c2/ count[1])
#Step3
last_step = []
for i in range(len(count_in)):
    last_step.append(count_in[i]*prob[i])
    index_of_max=last_step.index(max(last_step))
print("buys_computer={0}".format(unique_val[index_of_max]))

if __name__ == '__main__':
    table = np.array([
["<=30","high","no","fair","no"],
["<=30","high","no","excellent","no"],
["31..40","high","no","fair","yes"],
[">40","medium","no","fair","yes"],
[">40","low","yes","fair","yes"],
[">40","low","yes","excellent","no"],
["31..40","low","yes","excellent","yes"],
["<=30","medium","no","fair","no"],
["<=30","low","yes","fair","yes"],
[">40","medium","yes","fair","yes"],
["<=30","medium","yes","excellent","yes"],
["31..40","medium","no","excellent","yes"],
["31..40","high","yes","fair","yes"],
[">40","medium","no","excellent","no"]
])
condition=["<=30","medium","yes","fair"]
Naive(table,condition)