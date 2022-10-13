import pandas as pd

data = [['Boston University', 'Kevin Lang','Professor', '12402','4363','52','29'],\
['Harvard','Emily Breza','Professor','1867','1690','21','21'],\
['Princeton','Xiaosheng Mu','Assistant Professor','203','197','9','9']]


df = pd.DataFrame(data, columns = ["university","name","title","h_index","h_index2017","citations","citations2017"])
df[["h_index","h_index2017","citations","citations2017"]] = df[["h_index","h_index2017","citations","citations2017"]].apply(pd.to_numeric)


#grouping by the different titles, we take the average of the values
by_title = df.groupby("title").mean()

print(by_title)
print(by_title.plot.bar())
