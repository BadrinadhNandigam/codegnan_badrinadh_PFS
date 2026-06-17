'''
Matplotlib
----------

> This is a library in python for data visualization, allowing users to create
a variety of plots

Basic Structure of matplotlib

> figures
>grid
>title
>Legend


import matplotlib.pyplot as plt
sales = ['A','B','C']
values = [25,30,45]
plt.bar(sales,values,color = 'red',edgecolor = 'black')
plt.xlabel('sales')
plt.ylabel('values')
plt.title('bmw sales')
plt.show()
'''

'''
import matplotlib.pyplot as plt
sales = ['A', 'B', 'C']
values = [25, 30, 45]
plt.plot(sales, values, color='red', marker='o')
plt.xlabel('sales')
plt.ylabel('values')
plt.title('BMW sales')
plt.show()

'''
'''
import matplotlib.pyplot as plt

overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
runs = [6, 15, 25, 40, 55, 70, 85, 102, 120, 145]

plt.plot(overs, runs, marker='o', color='blue')

plt.title("Cricket Team Score Progress")
plt.xlabel("Overs")
plt.ylabel("Runs")
plt.grid(True)

plt.show()

'''

'''
import matplotlib.pyplot as plt
subjects = ["Python", "Java", "SQL", "HTML"]
marks = [40, 30, 20, 10]
plt.pie(marks,labels=subjects,autopct="%1.1f%%",  startangle=90)
plt.legend(subjects, title="Subjects", loc="upper right")
plt.title("Student Marks Distribution")
plt.show()
'''


'''
import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 60, 70, 80, 90]
plt.scatter(hours, marks, color="yellow", marker="o", s=100)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
'''

import matplotlib.pyplot as plt
marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
plt.hist(marks, bins=5, color="skyblue", edgecolor="black")
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

