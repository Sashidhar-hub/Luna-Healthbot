import streamlit as st
from chatbot import chatbot_response
from database import create_db, add_user, verify_user

# Initialize DB
create_db()

st.set_page_config(page_title="Luna Health Assistant", page_icon="💊")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# ---------------- SIGNUP PAGE ----------------
def signup_page():
    st.title("📝 Sign Up - Luna Health Assistant")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Sign Up"):
        if username and password:
            try:
                add_user(username, password)
                st.success("Account created successfully! Please login.")
                st.session_state.page = "login"
                st.experimental_rerun()
            except:
                st.error("Username already exists!")
        else:
            st.warning("Please fill all fields.")


# ---------------- LOGIN PAGE ----------------
def login_page():
    st.title("🔐 Login - Luna Health Assistant")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = verify_user(username, password)

        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid login credentials")


# ---------------- CHATBOT PAGE ----------------
def chatbot_page():
    st.title("💊 Luna Health Assistant")
    st.subheader("AI Health Assistant — SDG 3 (Good Health & Well-being)")

    st.write(f"Welcome, **{st.session_state.username}** 👋")

    user_input = st.text_input("Enter your health issue:")

    if st.button("Get Advice"):
        if user_input.strip():
            response = chatbot_response(user_input)
            st.success(response)
        else:
            st.warning("Please enter a health issue.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.experimental_rerun()


# ---------------- MAIN ROUTER ----------------
if st.session_state.logged_in:
    chatbot_page()
else:
    if st.session_state.page == "signup":
        signup_page()
    else:
        login_page()
        st.write("Don't have an account?")
        if st.button("Create Account"):
            st.session_state.page = "signup"
            st.experimental_rerun()
