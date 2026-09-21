import pandas as pd 
df = pd.read_csv("nato_phonetic_alphabet.csv")
dict_df = {row.letter:row.code for (index, row) in df.iterrows()}
name = input("Enter the name:").upper()
lst = [dict_df[alpha] for alpha in name]
print(lst)