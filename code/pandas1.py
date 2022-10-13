import pandas as pd
from main import get_h_index

# data = get_h_index()

data = [
    ["Boston University", "Kevin Lang", "Professor", "12402", "4363", "52", "29"],
    ["Harvard", "Emily Breza", "Professor", "1867", "1690", "21", "21"],
    ["Princeton", "Xiaosheng Mu", "Assistant Professor", "203", "197", "9", "9"],
]


df = pd.DataFrame(
    data,
    columns=[
        "university",
        "name",
        "title",
        "h_index",
        "h_index2017",
        "citations",
        "citations2017",
    ],
)
df[["h_index", "h_index2017", "citations", "citations2017"]] = df[
    ["h_index", "h_index2017", "citations", "citations2017"]
].apply(pd.to_numeric)


# grouping by the different titles, we take the average of the values
# print(df.groupby("title").mean())

print("For each uni, this is the number of profs who have each title.")
print(df.groupby(["university", "title"]).size())

print("Average value for each index by University and Job Title")
print(
    df.groupby(["university", "title"])
    .mean(numeric_only=True)
    .sort_values(by=["h_index"], ascending=False)
)
