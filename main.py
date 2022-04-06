''' 
PLOT MULTIPLE VARIABLES WITH PLOTLY
* Plotly Express is a library to build interactive graphics using low code.
* Here is how we can plot multiple variables on the same figure.
'''

#Data
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
data1 = [10, 13, 14, 18, 16, 15, 16, 17, 19, 19, 20]
data2 = [20, 23, 24, 19, 26, 25, 24, 29, 29, 26, 30]
data3 = [10, 15, 16, 17, 19, 23, 25, 24, 27, 28, 33]
data4 = [11, 18, 12, 25, 19, 10, 15, 17, 21, 24, 14]

#Create the figure
fig = px.line(x=months, y=[data1,data2,data3,data4])

#Update the size of the figure
fig.update_layout(height=600,width=900)

#Update the line width
fig.update_traces(line=dict(width=4))

#Change the var names on the legend
names={'wide_variable_0':'Phones','wide_variable_1':'Tablets','wide_variable_2':'Laptops','wide_variable_3':'Computers'}
fig.for_each_trace(lambda t: t.update(name = names[t.name]))

#Show
fig.show()
