import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Step 1: Dataset
data = {
    "cgpa": [5, 6, 7, 8, 9, 6.5, 7.5, 8.5],
    "skills": [1, 2, 2, 3, 4, 2, 3, 4],
    "placed": [0, 0, 0, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Step 2: Features & Target
X = df[["cgpa", "skills"]]
y = df["placed"]

# Step 3: Train Model
model = LogisticRegression()
model.fit(X, y)

# Step 4: Save Model
pickle.dump(model, open("model.pkl", "wb"))

print("✅ Model trained & saved!")