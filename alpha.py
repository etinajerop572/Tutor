import pandas as pd
df = pd.read_excel("TAM_ICO_4.xlsx", sheet_name="Hoja1")
# Suponiendo columnas del constructo: ['item1','item2','item3','item4','item5']
items = df[['item 23']]
cronbach_alpha = (len(items.columns)/(len(items.columns)-1)) * \
                 (1 - items.var().sum() / items.sum(axis=1).var())
print(cronbach_alpha)