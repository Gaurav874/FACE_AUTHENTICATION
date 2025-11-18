# import face_recognition
# import os
# import argparse
# import pickle

# # Argument parser
# parser = argparse.ArgumentParser()
# parser.add_argument('--name', required=True, help='Name of the person')
# parser.add_argument('--path', required=True, help='Path to folder of images')
# args = parser.parse_args()

# name = args.name
# folder_path = args.path

# # Load existing encodings if available
# if os.path.exists("encodings.pkl"):
#     with open("encodings.pkl", "rb") as f:
#         known_data = pickle.load(f)
# else:
#     known_data = {"encodings": [], "names": []}

# # Encode new images
# new_encodings = []
# for img_name in os.listdir(folder_path):
#     img_path = os.path.join(folder_path, img_name)
#     image = face_recognition.load_image_file(img_path)
#     face_locations = face_recognition.face_locations(image, model="hog")
#     encodings = face_recognition.face_encodings(image, face_locations)
#     for encode in encodings:
#         new_encodings.append(encode)

# # Merge
# known_data["encodings"].extend(new_encodings)
# known_data["names"].extend([name] * len(new_encodings))

# # Save updated encodings
# with open("encodings.pkl", "wb") as f:
#     pickle.dump(known_data, f)

# print(f"[✅] Added {len(new_encodings)} encodings for '{name}' and saved to encodings.pkl")


import face_recognition
import os
import argparse
import pickle

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--name', required=True, help='Name of the person')
parser.add_argument('--path', required=True, help='Path to folder of images')
args = parser.parse_args()

name = args.name
folder_path = args.path

# Load existing encodings if available
if os.path.exists("encodings.pkl"):
    with open("encodings.pkl", "rb") as f:
        known_data = pickle.load(f)
else:
    known_data = {"encodings": [], "names": []}

# Encode new images using CNN model
new_encodings = []
img_count = 0
face_count = 0

for img_name in os.listdir(folder_path):
    img_path = os.path.join(folder_path, img_name)
    image = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(image, model="cnn")  # CNN used here
    encodings = face_recognition.face_encodings(image, face_locations)
    
    if len(encodings) == 0:
        print(f"[⚠️] No face found in image: {img_name}")
    else:
        img_count += 1
        face_count += len(encodings)
        new_encodings.extend(encodings)

# Merge with existing data
known_data["encodings"].extend(new_encodings)
known_data["names"].extend([name] * len(new_encodings))

# Save updated encodings
with open("encodings.pkl", "wb") as f:
    pickle.dump(known_data, f)

print(f"[✅] Processed {img_count} images and added {face_count} face encodings for '{name}'.")

