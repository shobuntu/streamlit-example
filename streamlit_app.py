import streamlit as st

def main():
    st.title("My Resume")
    name = st.text_input("Name", "John Doe")
    profession = st.text_input("Profession", "Software Developer")

    st.header(name)
    st.subheader(profession)

    st.write("""
        Hello! I'm {} and I work as a {}.
        """.format(name, profession))

    st.subheader("Experience")
    exp1 = st.text_area("Experience 1", "Software Developer at XYZ Company (2019 - Present)")
    exp2 = st.text_area("Experience 2", "Internship at ABC Tech (2018)")
    st.write("""
        - {}
        - {}
        """.format(exp1, exp2))

    st.subheader("Education")
    edu = st.text_area("Education", "Bachelor's Degree in Computer Science, University of XYZ (2015 - 2019)")
    st.write("- {}".format(edu))

    st.subheader("Skills")
    skills = st.text_area("Skills", """
        - Programming Languages: Python, JavaScript, Java
        - Web Development: HTML, CSS, Flask, Django
        - Database: SQL, MongoDB
        - Tools & Technologies: Git, Docker, AWS
        """)
    st.write(skills)

if __name__ == "__main__":
    main()
