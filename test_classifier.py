import pickle

with open("classifier.pkl", "rb") as f:
    data = pickle.load(f)

print("Type of data:", type(data))

try:
    print("Keys:", data.keys())
except AttributeError:
    print("❌ Error: Data is not a dictionary!")

print("Data preview:", data)
