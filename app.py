import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="EduManage AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduManage AI")
st.subheader("College Student Management Dashboard")

# Demo student data
data = [
    {
        "Registration No": "EA001",
        "Student Name": "Rahul Sharma",
        "Category": "OBC",
        "Scholarship": "Approved"
    },
    {
        "Registration No": "EA002",
        "Student Name": "Priya Verma",
        "Category": "SC",
        "Scholarship": "Pending"
    },
    {
        "Registration No": "EA003",
        "Student Name": "Amit Patel",
        "Category": "ST",
        "Scholarship": "Approved"
    },
    {
        "Registration No": "EA004",
        "Student Name": "Sneha Gupta",
        "Category": "Open",
        "Scholarship": "Not Applied"
    }
]

df = pd.DataFrame(data)

st.markdown("### 📊 Student Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric(
    "Approved Scholarships",
    len(df[df["Scholarship"] == "Approved"])
)
col3.metric(
    "Pending Applications",
    len(df[df["Scholarship"] == "Pending"])
)

st.divider()

st.markdown("### 👨‍🎓 Student Records")

category = st.selectbox(
    "Select Category",
    ["All", "SC", "ST", "OBC", "Open"]
)

if category != "All":
    filtered_df = df[df["Category"] == category]
else:
    filtered_df = df

st.dataframe(filtered_df, use_container_width=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Excel-Compatible CSV",
    data=csv,
    file_name="student_records.csv",
    mime="text/csv"
)

st.caption("EduManage AI | Demo Version 1.0")
