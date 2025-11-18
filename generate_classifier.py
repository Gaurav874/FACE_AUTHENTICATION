# import os
# import face_recognition
# import pickle

# # Folder jisme folders of faces hain
# base_path = "training-images"

# encodings = []
# names = []

# for person_name in os.listdir(base_path):
#     person_folder = os.path.join(base_path, person_name)

#     if not os.path.isdir(person_folder):
#         continue

#     for img_name in os.listdir(person_folder):
#         img_path = os.path.join(person_folder, img_name)
#         image = face_recognition.load_image_file(img_path)
#         face_encs = face_recognition.face_encodings(image)

#         if face_encs:
#             encodings.append(face_encs[0])
#             names.append(person_name)
#             print(f"✅ Encoded: {img_name} -> {person_name}")
#         else:
#             print(f"⚠️ No face found in {img_name}, skipping...")

# # Save as dictionary (✅ correct structure)
# data = {"encodings": encodings, "names": names}
# with open("classifier.pkl", "wb") as f:
#     pickle.dump(data, f)

# print("✅ classifier.pkl file saved in correct format (dict with 'encodings' & 'names')")



# face_locations = face_recognition.face_locations(img, model="cnn")


# import os
# import face_recognition
# import pickle

# # Folder jisme folders of faces hain
# base_path = "training-images"

# encodings = []
# names = []

# for person_name in os.listdir(base_path):
#     person_folder = os.path.join(base_path, person_name)

#     if not os.path.isdir(person_folder):
#         continue

#     for img_name in os.listdir(person_folder):
#         img_path = os.path.join(person_folder, img_name)
#         image = face_recognition.load_image_file(img_path)
#         # face_encs = face_recognition.face_encodings(image)

#         # cnn model
#         face_locations = face_recognition.face_locations(image, model="cnn")
#         face_encs = face_recognition.face_encodings(image, face_locations)


#         if face_encs:
#             encodings.append(face_encs[0])
#             names.append(person_name)
#             print(f"✅ Encoded: {img_name} -> {person_name}")
#         else:
#             print(f"⚠️ No face found in {img_name}, skipping...")

# # ✅ Save as tuple (encodings, names)
# with open("classifier.pkl", "wb") as f:
#     pickle.dump((encodings, names), f)

# print("✅ classifier.pkl saved as tuple (encodings, names)")




#extra
import os
import cv2
import face_recognition
import pickle

dataset_path = 'training-images'
encoding_file = 'classifier.pkl'

# ✅ Load previous encodings if they exist
if os.path.exists(encoding_file):
    with open(encoding_file, 'rb') as f:
        known_encodings, known_names = pickle.load(f)
    print("✅ Previous encodings loaded.")
else:
    known_encodings = []
    known_names = []

# ✅ Encode only folders that are not already encoded
for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue

    # ⛔ Skip if person is already encoded
    if person_name in known_names:
        print(f"⏭️ Skipping already encoded: {person_name}")
        continue

    print(f"🔄 Encoding images for: {person_name}")

    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)

        image = cv2.imread(image_path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb_image, model='cnn')

        encodings = face_recognition.face_encodings(rgb_image, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)
            print(f"✅ Encoded {image_path}")

# ✅ Save all encodings
with open(encoding_file, 'wb') as f:
    pickle.dump((known_encodings, known_names), f)

print("\n🎉 Encoding complete!")

