<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/156916372-d8c1bbdd-5fe9-40d1-a250-5a1d4d454832.png">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/161909107-3988cd74-ff76-4467-b670-ea04974ede98.png">
</div>

<h1 align="center">Plot Multiple Variables With Plotly</h1>
Plotly Express is a great library to plot and be able to interact with the graphic. Here's a quick code on how to plot multiple lines on the same figure. In summary, all you need to do is to list your data for the Y axis, as the X will be the same for the three plots.

Updating the parameters to customize some features is not as trivial as other libraries, but there's plenty of documentation and help online. It is worth it the work!

### Prerequisites
* `Python 3`
* `Plotly`

<!-- ### Source Code -->
```python3
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
```

## Output
<p align="center">
  <a href="Output/newplot.png"><img src="https://user-images.githubusercontent.com/85709371/161957517-220027a9-e295-4253-8a2d-e15e2b242eb6.png" alt="output"></a>
</p>
  
## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
