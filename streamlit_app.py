import streamlit as st

# st.set_page_config(
#     page_title="My Resume",
#     page_icon=":sunglasses:",
#     layout="wide",
#     initial_sidebar_state="auto",
#     theme="dark"
# )

def main():
    st.title("Shobhit's Resume")

    # Display your image
    st.image("IMG_6043.JPG", width=200)

    # Buttons to toggle visibility
    with st.expander("Personal Information", expanded=True):
        st.subheader("Shobhit Srivastava")
        st.write("Technology Analyst")

    with st.expander("Experience"):
        st.write("""
            - Software Developer at XYZ Company (2019 - Present)
            - Internship at ABC Tech (2018)
        """)

    with st.expander("Education"):
        st.write("""
            - Bachelor's Degree in Computer Science, University of XYZ (2015 - 2019)
        """)

    with st.expander("Skills"):
        st.write("""
            - Programming Languages: Python, JavaScript, Java
            - Web Development: HTML, CSS, Flask, Django
            - Database: SQL, MongoDB
            - Tools & Technologies: Git, Docker, AWS
        """)
    st.markdown("[Download Resume PDF](myFile.pdf)", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
