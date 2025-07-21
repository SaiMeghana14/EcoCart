import streamlit as st

def show():
    st.header("🔐 Login to EcoCart")

    if 'user_id' not in st.session_state:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            # ✅ Simple hardcoded login (for demo)
            if username == "ecouser" and password == "eco123":
                st.session_state.user_id = username
                st.success(f"✅ Welcome {username}!")
                st.experimental_rerun()
            else:
                st.error("❌ Invalid credentials!")
    else:
        st.success(f"✅ Logged in as {st.session_state.user_id}")
        if st.button("Logout"):
            del st.session_state.user_id
            st.success("✅ Logged out successfully.")
            st.experimental_rerun()
