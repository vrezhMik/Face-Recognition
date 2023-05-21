import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D']
percentages = [25, 30, 15, 30]
explode = [0, 0.1, 0, 0]
colors = ['red', 'blue', 'green', 'orange']

plt.pie(percentages, explode=explode, labels=categories, colors=colors, shadow=True)
plt.title('Percentage Distribution')
plt.legend(categories)
plt.show()

