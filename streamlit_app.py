import streamlit as st

def main():
    st.title("My Resume")

    # Buttons to toggle visibility
    with st.beta_expander("Personal Information", expanded=True):
        st.subheader("John Doe")
        st.write("Software Developer")

    with st.beta_expander("Experience"):
        st.write("""
            - Software Developer at XYZ Company (2019 - Present)
            - Internship at ABC Tech (2018)
        """)

    with st.beta_expander("Education"):
        st.write("""
            - Bachelor's Degree in Computer Science, University of XYZ (2015 - 2019)
        """)

    with st.beta_expander("Skills"):
        st.write("""
            - Programming Languages: Python, JavaScript, Java
            - Web Development: HTML, CSS, Flask, Django
            - Database: SQL, MongoDB
            - Tools & Technologies: Git, Docker, AWS
        """)

if __name__ == "__main__":
    main()
