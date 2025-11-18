import pickle
from collections import Counter

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

counts = Counter(data["names"])
print("Names and encoding counts:")
print(counts)
