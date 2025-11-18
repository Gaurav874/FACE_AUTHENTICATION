# # # recognize_faces.py
# # import face_recognition
# # import cv2
# # import pickle

# # def recognize_face():
# #     known_faces = pickle.load(open("classifier.pkl", "rb"))

# #     video_capture = cv2.VideoCapture(0)
# #     recognized_name = "Unknown"

# #     while True:
# #         ret, frame = video_capture.read()
# #         if not ret:
# #             break

# #         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #         face_locations = face_recognition.face_locations(rgb_frame)
# #         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

# #         for face_encoding in face_encodings:
# #             matches = face_recognition.compare_faces(known_faces["encodings"], face_encoding)
# #             name = "Unknown"

# #             face_distances = face_recognition.face_distance(known_faces["encodings"], face_encoding)
# #             best_match_index = face_distances.argmin() if len(face_distances) else -1

# #             if best_match_index != -1 and matches[best_match_index]:
# #                 name = known_faces["names"][best_match_index]

# #             recognized_name = name
# #             break

# #         break  # Remove loop after 1 scan (optional for Streamlit)

# #     video_capture.release()
# #     cv2.destroyAllWindows()
# #     return recognized_name




# import face_recognition
# import cv2
# import pickle
# import numpy as np

# def recognize_face():
#     # ✅ Load encodings and names as tuple
#     known_encodings, known_names = pickle.load(open("classifier.pkl", "rb"))

#     video_capture = cv2.VideoCapture(0)
#     recognized_name = "Unknown"

#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             break

#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         for face_encoding in face_encodings:
#             # 🎯 Tight tolerance
#             matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.45)
#             face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            
#             name = "Unknown"

#             if len(face_distances) > 0:
#                 best_match_index = np.argmin(face_distances)
#                 if matches[best_match_index] and face_distances[best_match_index] < 0.45:
#                     name = known_names[best_match_index]

#             recognized_name = name
#             print("Predicted:", name)  # ✅ Print here if you want to see output
#             break

#         break

#     video_capture.release()
#     cv2.destroyAllWindows()
#     return recognized_name











# # import cv2
# # import face_recognition
# # import os
# # import time
# # import numpy as np

# # # ✅ Path where face images are stored
# # dataset_path = "training-images"

# # def load_known_faces():
# #     known_encodings = []
# #     known_names = []

# #     for person_name in os.listdir(dataset_path):
# #         person_folder = os.path.join(dataset_path, person_name)
# #         if not os.path.isdir(person_folder):
# #             continue

# #         for img_name in os.listdir(person_folder):
# #             img_path = os.path.join(person_folder, img_name)
# #             img = face_recognition.load_image_file(img_path)
# #             encodings = face_recognition.face_encodings(img)

# #             if encodings:
# #                 known_encodings.append(encodings[0])
# #                 known_names.append(person_name)

# #     return known_encodings, known_names

# # def recognize_faces(timeout=10):
# #     known_encodings, known_names = load_known_faces()

# #     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # ✅ Ensures Windows cameras open quickly

# #     if not cap.isOpened():
# #         raise Exception("Camera not detected. Please check your webcam.")

# #     start_time = time.time()
# #     recognized_names = set()

# #     while time.time() - start_time < timeout:
# #         ret, frame = cap.read()
# #         if not ret:
# #             continue  # Retry instead of breaking immediately

# #         small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # ✅ Speed boost
# #         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

# #         face_locations = face_recognition.face_locations(rgb_small_frame)
# #         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

# #         for encoding in face_encodings:
# #             matches = face_recognition.compare_faces(known_encodings, encoding)
# #             face_distances = face_recognition.face_distance(known_encodings, encoding)
# #             name = "Unknown"

# #             if len(face_distances) > 0:
# #                 best_match_index = np.argmin(face_distances)
# #                 if matches[best_match_index]:
# #                     name = known_names[best_match_index]

# #             recognized_names.add(name)

# #         # Optional: Break early if at least one known face recognized
# #         if any(name != "Unknown" for name in recognized_names):
# #             break

# #     cap.release()
# #     return list(recognized_names)





import face_recognition
import cv2
import pickle
import numpy as np
import time

def recognize_face():
    # ✅ Load encodings and names from pickle file
    try:
        known_encodings, known_names = pickle.load(open("classifier.pkl", "rb"))
    except Exception as e:
        print("❌ Error loading classifier.pkl:", e)
        return "Error"

    # ✅ Start webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("❌ Webcam not detected.")
        return "Camera Error"

    recognized_name = "Unknown"

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Frame not read.")
            break

        # ✅ Resize frame for speed & convert to RGB
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        ## face_locations = face_recognition.face_locations(rgb_frame)
        # face_locations = face_recognition.face_locations(rgb_frame, model="cnn")
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        start = time.time()
        face_locations = face_recognition.face_locations(rgb_frame, model="cnn")
        print("Detection time:", time.time() - start)


        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.45)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)

            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    recognized_name = known_names[best_match_index]
                    print(f"✅ Match Found: {recognized_name}")
                else:
                    print("😶 Face not recognized.")
            break  # Only detect first face and exit

        break

    cap.release()
    cv2.destroyAllWindows()
    return recognized_name





