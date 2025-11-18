# import streamlit as st
# from authenticate import recognize_face

# st.set_page_config(page_title="Secure Login", page_icon="🔐")
# st.title("🔐 Face Authentication Login")

# if "authenticated" not in st.session_state:
#     st.session_state["authenticated"] = False

# if not st.session_state["authenticated"]:
#     if st.button("Login with Face 👤"):
#         with st.spinner("Authenticating..."):
#             name = recognize_face()
#             if name != "Unknown":
#                 st.success(f"✅ Welcome, {name}")
#                 st.session_state["authenticated"] = True
#             else:
#                 st.error("❌ Unknown Face! Access Denied")
# else:
#     st.success("✅ You are logged in!")
#     st.write("👉 Now your chatbot page can open here...")





# import streamlit as st
# import cv2
# from PIL import Image
# from authenticate import recognize_face

# st.set_page_config(page_title="Secure Login", page_icon="🔐")
# st.title("🔐 Face Authentication Login")

# def capture_and_show_frame():
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         st.error("❌ Could not open webcam")
#         return None
#     ret, frame = cap.read()
#     cap.release()
#     if not ret:
#         st.error("❌ Failed to capture image from webcam")
#         return None
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     st.image(rgb_frame, caption="📸 Captured Face", channels="RGB")
#     return frame

# if "authenticated" not in st.session_state:
#     st.session_state["authenticated"] = False

# if not st.session_state["authenticated"]:
#     if st.button("Login with Face 👤"):
#         with st.spinner("📷 Capturing face..."):
#             frame = capture_and_show_frame()
#         if frame is not None:
#             with st.spinner("🔍 Recognizing face..."):
#                 name = recognize_face()
#                 if name != "Unknown":
#                     st.success(f"✅ Welcome, {name}")
#                     st.session_state["authenticated"] = True
#                 else:
#                     st.error("❌ Unknown Face! Access Denied")
# else:
#     st.success("✅ You are logged in!")
#     st.write("👉 Now your chatbot page can open here...")




#extra
# import streamlit as st
# import cv2
# import os
# import time
# from PIL import Image
# from authenticate import recognize_face

# # --- CONFIG ---
# TRAINING_PATH = "training-images"
# st.set_page_config(page_title="Secure Login", page_icon="🔐", layout="centered")

# # --- STYLING ---
# st.markdown("""
#     <style>
#     .big-title { font-size: 42px; font-weight: bold; color: #FFD700; text-align: center; }
#     .sub-title { font-size: 24px; color: #BBBBBB; text-align: center; margin-bottom: 30px; }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown('<p class="big-title">🔐 Face Authentication Login</p>', unsafe_allow_html=True)
# st.markdown('<p class="sub-title">Secure access with your face or create a new profile</p>', unsafe_allow_html=True)


# # --- Helper: Capture frame ---
# def capture_frame(show_preview=True):
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         st.error("❌ Could not open webcam")
#         return None
#     time.sleep(1)  # Camera warm-up
#     ret, frame = cap.read()
#     cap.release()
#     if not ret:
#         st.error("❌ Failed to capture image from webcam")
#         return None
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     if show_preview:
#         st.image(rgb_frame, caption="📸 Captured Face", channels="RGB")
#     return frame


# # --- Session for login state ---
# if "authenticated" not in st.session_state:
#     st.session_state["authenticated"] = False

# # --- LOGIN TAB ---
# tab1, tab2 = st.tabs(["👤 Login", "🆕 Sign Up"])

# with tab1:
#     st.subheader("Login with your face")
#     if not st.session_state["authenticated"]:
#         if st.button("Login with Face"):
#             with st.spinner("📷 Capturing face..."):
#                 frame = capture_frame()
#             if frame is not None:
#                 with st.spinner("🔍 Recognizing face..."):
#                     name = recognize_face()
#                     if name != "Unknown":
#                         st.success(f"✅ Welcome, {name}")
#                         st.session_state["authenticated"] = True
#                     else:
#                         st.error("❌ Unknown Face! Access Denied")
#     else:
#         st.success("✅ You are logged in!")
#         st.write("👉 Now your chatbot page can open here...")

# # --- SIGNUP TAB ---
# with tab2:
#     st.subheader("Create a new profile")
#     username = st.text_input("Enter a unique username:")

#     if st.button("Create Account"):
#         if username.strip() == "":
#             st.error("❌ Username cannot be empty.")
#         else:
#             new_user_path = os.path.join(TRAINING_PATH, username)
#             if os.path.exists(new_user_path):
#                 st.warning("⚠️ This username already exists. Please choose another.")
#             else:
#                 os.makedirs(new_user_path)
#                 st.success(f"✅ Account created for '{username}'. Now capture some photos.")

#                 # Capture multiple photos
#                 st.info("Click 'Capture Photo' to take your pictures (3-5 recommended).")
#                 photos = []
#                 if st.button("📸 Capture Photo"):
#                     frame = capture_frame()
#                     if frame is not None:
#                         photo_path = os.path.join(new_user_path, f"{int(time.time())}.jpg")
#                         cv2.imwrite(photo_path, frame)
#                         st.success(f"✅ Saved: {photo_path}")
#                         photos.append(photo_path)






# import streamlit as st
# import cv2
# import os
# import time
# from PIL import Image
# from authenticate import recognize_face

# # --- CONFIG ---
# TRAINING_PATH = "training-images"
# st.set_page_config(page_title="Secure Login", page_icon="🔐", layout="centered")

# # --- STYLING ---
# st.markdown("""
#     <style>
#     .big-title { font-size: 42px; font-weight: bold; color: #FFD700; text-align: center; }
#     .sub-title { font-size: 24px; color: #BBBBBB; text-align: center; margin-bottom: 30px; }
#     </style>
# """, unsafe_allow_html=True)

# st.markdown('<p class="big-title">🔐 Face Authentication Login</p>', unsafe_allow_html=True)
# st.markdown('<p class="sub-title">Secure access with your face or create a new profile</p>', unsafe_allow_html=True)


# # --- Helper: Capture frame ---
# def capture_frame(show_preview=True):
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         st.error("❌ Could not open webcam")
#         return None
#     time.sleep(1)  # Camera warm-up
#     ret, frame = cap.read()
#     cap.release()
#     if not ret:
#         st.error("❌ Failed to capture image from webcam")
#         return None
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     if show_preview:
#         st.image(rgb_frame, caption="📸 Captured Face", channels="RGB")
#     return frame


# # --- Session for login & signup state ---
# if "authenticated" not in st.session_state:
#     st.session_state["authenticated"] = False
# if "current_user" not in st.session_state:
#     st.session_state["current_user"] = None

# # --- LOGIN TAB ---
# tab1, tab2 = st.tabs(["👤 Login", "🆕 Sign Up"])

# with tab1:
#     st.subheader("Login with your face")
#     if not st.session_state["authenticated"]:
#         if st.button("Login with Face"):
#             with st.spinner("📷 Capturing face..."):
#                 frame = capture_frame()
#             if frame is not None:
#                 with st.spinner("🔍 Recognizing face..."):
#                     name = recognize_face()
#                     if name != "Unknown":
#                         st.success(f"✅ Welcome, {name}")
#                         st.session_state["authenticated"] = True
#                     else:
#                         st.error("❌ Unknown Face! Access Denied")
#     else:
#         st.success("✅ You are logged in!")
#         st.write("👉 Now your chatbot page can open here...")

# # --- SIGNUP TAB ---
# with tab2:
#     st.subheader("Create a new profile")
#     username = st.text_input("Enter a unique username:")

#     if st.button("Create Account"):
#         if username.strip() == "":
#             st.error("❌ Username cannot be empty.")
#         else:
#             new_user_path = os.path.join(TRAINING_PATH, username)
#             if os.path.exists(new_user_path):
#                 st.warning("⚠️ This username already exists. Please choose another.")
#             else:
#                 os.makedirs(new_user_path)
#                 st.session_state["current_user"] = username  # Save username in session
#                 st.success(f"✅ Account created for '{username}'. Now capture some photos.")

#     # If user account already created, allow capturing photos
#     if st.session_state["current_user"]:
#         current_user_path = os.path.join(TRAINING_PATH, st.session_state["current_user"])
#         st.info(f"Capturing photos for: {st.session_state['current_user']} (3-5 recommended)")

#         if st.button("📸 Capture Photo"):
#             frame = capture_frame()
#             if frame is not None:
#                 photo_path = os.path.join(current_user_path, f"{int(time.time())}.jpg")
#                 cv2.imwrite(photo_path, frame)
#                 st.success(f"✅ Saved: {photo_path}")
#                 st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="Captured Photo", channels="RGB")




import streamlit as st
import cv2
import os
import time
from PIL import Image
from authenticate import recognize_face

# --- CONFIG ---
TRAINING_PATH = "training-images"
st.set_page_config(page_title="Secure Login", page_icon="🔐", layout="centered")

# --- STYLING ---
st.markdown("""
    <style>
    .big-title { font-size: 42px; font-weight: bold; color: #FFD700; text-align: center; }
    .sub-title { font-size: 24px; color: #BBBBBB; text-align: center; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🔐 Face Authentication Login</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Secure access with your face or create a new profile</p>', unsafe_allow_html=True)


# --- Helper: Capture frame ---
def capture_frame():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("❌ Could not open webcam")
        return None
    time.sleep(1)  # Camera warm-up
    ret, frame = cap.read()
    cap.release()
    if not ret:
        st.error("❌ Failed to capture image from webcam")
        return None
    return frame  # Sirf frame return karega, image yaha nahi show karega


# --- Session for login & signup state ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "current_user" not in st.session_state:
    st.session_state["current_user"] = None

# --- LOGIN TAB ---
tab1, tab2 = st.tabs(["👤 Login", "🆕 Sign Up"])

with tab1:
    st.subheader("Login with your face")
    if not st.session_state["authenticated"]:
        if st.button("Login with Face"):
            with st.spinner("📷 Capturing face..."):
                frame = capture_frame()
            if frame is not None:
                st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="📸 Captured Face", channels="RGB")
                with st.spinner("🔍 Recognizing face..."):
                    name = recognize_face()
                    if name != "Unknown":
                        st.success(f"✅ Welcome, {name}")
                        st.session_state["authenticated"] = True
                    else:
                        st.error("❌ Unknown Face! Access Denied")
    else:
        st.success("✅ You are logged in!")
        st.write("👉 Now your chatbot page can open here...")

# --- SIGNUP TAB ---
with tab2:
    st.subheader("Create a new profile")
    username = st.text_input("Enter a unique username:")

    if st.button("Create Account"):
        if username.strip() == "":
            st.error("❌ Username cannot be empty.")
        else:
            new_user_path = os.path.join(TRAINING_PATH, username)
            if os.path.exists(new_user_path):
                st.warning("⚠️ This username already exists. Please choose another.")
            else:
                os.makedirs(new_user_path)
                st.session_state["current_user"] = username
                st.success(f"✅ Account created for '{username}'. Now capture some photos.")

    if st.session_state["current_user"]:
        current_user_path = os.path.join(TRAINING_PATH, st.session_state["current_user"])
        st.info(f"Capturing photos for: {st.session_state['current_user']} (3-5 recommended)")

        if st.button("📸 Capture Photo"):
            frame = capture_frame()
            if frame is not None:
                photo_path = os.path.join(current_user_path, f"{int(time.time())}.jpg")
                cv2.imwrite(photo_path, frame)
                st.success(f"✅ Saved: {photo_path}")
                st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption="Captured Photo", channels="RGB")
