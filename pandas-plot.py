import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('edindia.csv')
data['positive'] = data['label'] == "POSITIVE"
df = data['positive'].value_counts()
print "Negative Sentiments"
print(df[0]) #Number of Negative Comments
print "Positive Sentiments"
print(df[1]) #Number of Positive Comments

slices = [df[0], df[1]]
activites = ['negative', 'positive']
colors = ['r', 'g']
plt.pie(slices, labels=activites, colors=colors)
plt.xlabel('x')
plt.ylabel('y')
plt.title('EducationInIndia')
plt.legend()
plt.show()
