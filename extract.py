import pandas as pd
print("Extract data from mysql")

data = {
    "id": [1,2,3],
    "name": ["A", "B", "C"],
    "age": [10, 20, 30]

}

df = pd.Dataframe(data)
print(df)