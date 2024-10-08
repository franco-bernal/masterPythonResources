import seaborn as sns
import pn as pd
import matplotlib.pyplot as plt

data = {'Grupo': ['A', 'B', 'C'],
        'Valores': [5, 10, 15]}

df = pd.DataFrame(data)

sns.barplot(x='Grupo', y='Valores', data=df)
plt.xlabel('Grupo')
plt.ylabel('Valores')
plt.title('Gráfica de barras')
plt.show()