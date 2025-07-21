import streamlit as st
import pandas as pd

def get_badge(points):
    if points < 10:
        return "🌱 Eco Beginner"
    elif points < 30:
        return "🌿 Eco Warrior"
    else:
        return "🌍 Sustainability Champion"

def show(sheet):
    st.header("🏆 EcoCart Leaderboard Dashboard")

    data = sheet.get_all_records()
    if not data:
        st.info("Leaderboard is currently empty.")
        return

    df = pd.DataFrame(data)

    # Add Badges
    df["Badge"] = df["Points"].apply(get_badge)

    # Sort
    df = df.sort_values(by="Points", ascending=False)

    # Display Leaderboard
    st.subheader("📊 Leaderboard (with Badges)")
    st.dataframe(df, use_container_width=True)

    # Search by Username
    st.subheader("🔎 Search by Username")
    username = st.text_input("Enter username:")
    if username:
        user_row = df[df['Username'].str.lower() == username.lower()]
        if not user_row.empty:
            points = user_row.iloc[0]['Points']
            badge = user_row.iloc[0]['Badge']
            st.success(f"✅ {username} has **{points} EcoPoints** ({badge})")
        else:
            st.error("❌ Username not found.")

    # Points Filter
    st.subheader("🎚️ Filter by Minimum Points")
    min_points = st.slider("Minimum Points", min_value=0, max_value=int(df["Points"].max()), value=0)
    filtered_df = df[df["Points"] >= min_points]
    st.dataframe(filtered_df, use_container_width=True)

    # Optional Bar Chart
    if st.checkbox("📈 Show Bar Chart"):
        st.bar_chart(filtered_df.set_index("Username")["Points"])

    # Download CSV
    st.subheader("⬇️ Download Leaderboard Data")
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("Download as CSV", data=csv, file_name="leaderboard.csv", mime="text/csv")
