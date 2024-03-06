import pandas

print("Start csv read application")

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for r, rij in df.iterrows():
    print(rij["Attack"])
    print(rij["Name"])
