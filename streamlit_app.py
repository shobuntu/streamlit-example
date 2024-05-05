import streamlit as st

def main():
    st.title("Shobhit's Resume")

    # Display your image
    st.image("IMG_6043.jpg", use_column_width=True)

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

if __name__ == "__main__":
    main()
