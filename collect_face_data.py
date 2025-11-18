# import cv2
# import os

# def collect_face_data(name, num_images=25):
#     save_dir = f"images/{name}"
#     os.makedirs(save_dir, exist_ok=True)

#     cap = cv2.VideoCapture(0)
#     count = 0

#     print(f"[INFO] Capturing face images for: {name}")

#     while count < num_images:
#         ret, frame = cap.read()
#         if not ret:
#             print("[ERROR] Failed to grab frame")
#             break

#         cv2.imshow("Face Capture - Press 'q' to quit", frame)

#         # Save every nth frame to avoid duplicates
#         if count % 2 == 0:
#             img_path = os.path.join(save_dir, f"{name}_{count}.jpg")
#             cv2.imwrite(img_path, frame)
#             print(f"[INFO] Saved image: {img_path}")
        
#         count += 1

#         if cv2.waitKey(100) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     print("[INFO] Face data collection complete.")



import cv2
import os

name = input("Enter your name: ")

dataset_path = "dataset"
person_path = os.path.join(dataset_path, name)
os.makedirs(person_path, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

print("Press 's' to save image, 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not detected.")
        break

    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        count += 1
        filename = os.path.join(person_path, f"{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

