import matplotlib.pyplot as plt

years = [2010, 2012, 2014, 2016, 2018, 2020]
population = [8.5, 9.1, 9.8, 10.5, 11.2, 11.9]

plt.plot(years, population, marker='o', linestyle='--', color='green')
plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.title('Population Growth Over Years')
plt.show()

