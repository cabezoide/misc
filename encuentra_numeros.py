import pandas as pd

df1 = pd.read_csv("archivo1.csv")
df2 = pd.read_csv("archivo2.csv")

print(df1.head(5))
print(df2.head(5))

interseccion = pd.merge(df1, df2, how='inner', left_on=['numeros1'], right_on=['numeros2'])



print(interseccion)