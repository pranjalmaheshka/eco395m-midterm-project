import pandas as pd
from main import get_h_index
import matplotlib.pyplot as plt


data = pd.read_csv('../artifacts/scores.csv')

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


# shows how many of each title the universities have
final0 = df.groupby(["university", "title"]).size()

# average indexes by university
final1 = (
    df.groupby(["university"])
    .mean(numeric_only=True)
    .sort_values(by=["h_index"], ascending=False)
)

# average indexes by title
final2 = (
    df.groupby(["title"])
    .mean(numeric_only=True)
    .sort_values(by=["h_index"], ascending=False)
)

# average indexes by both uni and title
final3 = (
    df.groupby(["university", "title"])
    .mean(numeric_only=True)
    .sort_values(by=["h_index"], ascending=False)
)

# barplot showing average indexes by uni and title
final3["h_index"].unstack().plot(
    kind="bar", rot=30, title="Avg. H-Index Score by School & Title"
)
plt.show()
