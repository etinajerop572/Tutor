import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Pregunta': ['SA'],
    '1 Totalmente en desacuerdo':[0],
    '2 En desacuerdo':[4.35],
    '3 Ni de acuerdo ni en desacuerdo':[0],
    '4 En acuerdo':[39.13],
    '5 Totalmente de acuerdo':[56.52]
}

df = pd.DataFrame(data)

# Mismos datos de ejemplo
df_plot = df.set_index('Pregunta')[['1 Totalmente en desacuerdo','2 En desacuerdo','3 Ni de acuerdo ni en desacuerdo','4 En acuerdo','5 Totalmente de acuerdo']]

# Colores
colors = ['#d73027', '#f46d43', '#fdae61', '#abd9e9', '#4575b4']

ax = df_plot.plot(kind='barh', stacked=True, color=colors, figsize=(10,6))

# Etiquetas con %
for c in ax.containers:
    labels = [f'{v:.0f}%' if v > 5 else '' for v in [v.get_width() for v in c]]
    ax.bar_label(c, labels=labels, label_type='center', color='white', fontsize=9, fontweight='bold')

ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', title='Respuesta')
ax.set_xlabel('Porcentaje (%)')
ax.set_title('Variable accesibilidad del sistema (SA)')
ax.grid(axis='x', linestyle='--', alpha=0.3)

# Invertir para que la pregunta quede arriba
ax.invert_yaxis()

plt.tight_layout()
plt.show()