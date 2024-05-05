import streamlit as st

def main():
    st.title("My Resume")

    with st.beta_expander("About Me"):
        st.write("""
            Hello! I'm a software developer passionate about creating useful and efficient software solutions. 
            I have experience in various programming languages and technologies, and I'm always eager to learn new things.
        """)

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
