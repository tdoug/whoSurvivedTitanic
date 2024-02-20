import numpy as np
import pandas as pd

import os

for dirname, _, filenames in os.walk('./input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Load the data
train_data = pd.read_csv("./input/train.csv")
train_data.head()

test_data = pd.read_csv("./input/test.csv")
test_data.head()

# how many women survived?
women = train_data.loc[train_data.Sex == "female"]["Survived"]
rate_women = sum(women) / len(women)

print("% of women who survived:", rate_women)

# about 75%, wow.  Let's try some other modifiers
# let's what if they had children or were children?

womenWithChildren = train_data.loc[train_data.Sex == "female"].loc[train_data.Parch == True]["Survived"]
rate_womenWithChildren = sum(womenWithChildren) / len(womenWithChildren)

print("% of women with children who survived:", rate_womenWithChildren)

# a little better.  what if they were first class?

womenWithChildrenFirstClass = train_data.loc[train_data.Sex == "female"].loc[train_data.Parch == True].loc[train_data.Pclass == 1]["Survived"]
rate_womenWithChildrenFirstClass = sum(womenWithChildrenFirstClass) / len(womenWithChildrenFirstClass)

print("% of women in first class with children who survived:", rate_womenWithChildrenFirstClass)

# 100%.  well there you have it folks, rich mothers with money ftw!  No wardrobe door or whistle needed.  sorry jack, gg
