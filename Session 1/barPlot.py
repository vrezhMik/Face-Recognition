import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [350, 480, 290, 520]

plt.bar(products, sales, color=['red', 'blue', 'green', 'orange'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.legend(['Sales'])
plt.show()

