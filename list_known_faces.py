import pickle
import os

if not os.path.exists("encodings.pkl"):
    print("⚠️ encodings.pkl file not found.")
    exit()

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

unique_names = list(set(data["names"]))
print(f"\n✅ Total unique people encoded: {len(unique_names)}")
print("👤 People added for face recognition:")
for name in unique_names:
    print(f" - {name}")
