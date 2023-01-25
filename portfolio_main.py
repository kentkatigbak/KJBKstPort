import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import webbrowser

st.set_page_config(page_title="Portfolio-KentKatigbak",
                layout="wide"
                )

# Remove header and footer
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

colA1, colA2 = st.columns([1,0.7])
with colA1:
    socials = option_menu(
        menu_title=None,
        options=["Hi! I am Kent. I am an Industrial Engineer. Get to know me more!", "Linkedin", "Facebook", "Instagram", "Twitter", "Download Resume"],
        icons=["None" ,"linkedin", "facebook", "instagram", "twitter", "stickies"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "lightgray"},
            "icon": {"color": "black", "font-size": "40px"}, 
            "nav-link": {"font-size": "40px", "text-align": "left", "margin":"0px", "--hover-color": "darkgray"},
            "nav-link-selected": {"background-color": "#c1502e"},
        }
    )

    if socials == "Linkedin":
        webbrowser.open_new_tab("https://www.linkedin.com/in/kentjk/")
    if socials == "Facebook":
        webbrowser.open_new_tab("https://www.facebook.com/kntktgbk")
    if socials == "Instagram":
        webbrowser.open_new_tab("https://www.instagram.com/kentjk_/")
    if socials == "Twitter":
        webbrowser.open_new_tab("https://twitter.com/kentjk_")
    if socials == "Download Resume":
        st.subheader("You are about to save a PDF copy of my resume")
        resume = open("Resume - Katigbak, Kent Jym.pdf", "rb")
        st.download_button("Proceed to download", resume, file_name="KentJymKatigbak_Resume.pdf", mime="pdf")

with colA2:
    st.image("2x2.jpeg")

# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Skills", "Education", "Certifications", "Other Achievements"],
    icons=["person-badge", "book", "shield-check", "trophy"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "lightgray"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "darkgray"},
        "nav-link-selected": {"background-color": "#c1502e"},
    }
)

#Skills
if selected == "Skills":
    st.markdown("#### I am an Industrial Engineer, Safety Officer 2, and Certified Lean Six Sigma Yellow Belt. I am also a beginner Python Programmer and Data Analyst")

    #Skills
    st.header("Skills")
    skill1, spaceS1, progress1, spaceP1, years1 = st.columns([4,1,10,1,5])
    with skill1:
        st.subheader("Microsoft Word")
    with progress1:
        st.write("")
        st.progress(100)
    with years1:
        st.markdown("#### 10+ years")

    skill2, spaceS2, progress2, spaceP2, years2 = st.columns([4,1,10,1,5])
    with skill2:
        st.subheader("Microsoft Excel")
    with progress2:
        st.write("")
        st.progress(100)
    with years2:
        st.markdown("#### 10+ years")

    skill3, spaceS3, progress3, spaceP3, years3 = st.columns([4,1,10,1,5])
    with skill3:
        st.subheader("Powerpoint")
    with progress3:
        st.write("")
        st.progress(100)
    with years3:
        st.markdown("#### 10+ years")
        
    skill4, spaceS4, progress4, spaceP4, years4 = st.columns([4,1,10,1,5])
    with skill4:
        st.subheader("Adobe Photoshop")
    with progress4:
        st.write("")
        st.progress(50)
    with years4:
        st.markdown("#### 2 years")
        
    skill5, spaceS5, progress5, spaceP5, years5 = st.columns([4,1,10,1,5])
    with skill5:
        st.subheader("Minitab")
    with progress5:
        st.write("")
        st.progress(50)
    with years5:
        st.markdown("#### 2 years")

    skill6, spaceS6, progress6, spaceP6, years6 = st.columns([4,1,10,1,5])
    with skill6:
        st.subheader("Tableau")
    with progress6:
        st.write("")
        st.progress(30)
    with years6:
        st.markdown("#### 1 year")

    skill7, spaceS7, progress7, spaceP7, years7 = st.columns([4,1,10,1,5])
    with skill7:
        st.subheader("Python Scripting")
    with progress7:
        st.write("")
        st.progress(20)
    with years7:
        st.markdown("#### Less than 1 year")

    skill8, spaceS8, progress8, spaceP8, years8 = st.columns([4,1,10,1,5])
    with skill8:
        st.subheader("Postgre SQL")
    with progress8:
        st.write("")
        st.progress(20)
    with years8:
        st.markdown("#### Less than 1 year")

#Education
if selected == "Education":
    colB1, colB2 = st.columns([1,1.5])
    with colB1:
        st.image("logo-bsu.png")
    with colB2:
        st.title("")
        st.title("")
        st.title("")
        st.header("Bachelor of Science in Industrial Engineering")
        st.subheader("Batangas State University")
        st.subheader("The National Engineering University")
        st.subheader("2018-2022")

#Certifications
if selected == "Certifications":
    #Analytics Manager Pathway and Operational Analytics
    colC1, colC2, spaceC, colC3, colC4 = st.columns([2,4,1,2,4])
    with colC1:
        st.image("logo-dap.png")
    with colC2:
        st.subheader("Analytics Manager Pathway")
        st.markdown("##### Development Academy of the Philippines")
    with colC3:
        st.image("logo-dap.png")
    with colC4:
        st.subheader("Operational Analytics Microspecialization")
        st.markdown("##### Development Academy of the Philippines")
        
    #Data Visualization and Urban Planning
    colE1, colE2, spaceE, colE3, colE4 = st.columns([2,4,1,2,4])
    with colE1:
        st.image("logo-dap.png")
    with colE2:
        st.subheader("Data Visualization Microspecialization")
        st.markdown("##### Development Academy of the Philippines")
    with colE3:
        st.image("logo-dap.png")
    with colE4:
        st.subheader("Urban Planning Microspecialization")
        st.markdown("##### Development Academy of the Philippines")
        
    #Lean Six Sigma and CIFC
    colH1, colH2, spaceH, colH3, colH4 = st.columns([2,4,1,2,4])
    with colH1:
        st.image("logo-askLex.png")
    with colH2:
        st.subheader("Certified Lean Six Sigma Yellow Belt")
        st.markdown("##### AskLex PH Academy")
    with colH3:
        st.image("logo-askLex.png")
    with colH4:
        st.subheader("Data Science Fundamentals")
        st.markdown("##### AskLex PH Academy")

    #DSFC and PMFC
    colI1, colI2, spaceI, colI3, colI4 = st.columns([2,4,1,2,4])
    with colI1:
        st.image("logo-askLex.png")
    with colI2:
        st.subheader("Continuous Improvement Fundamentals")
        st.markdown("##### AskLex PH Academy")
    with colI3:
        st.image("logo-askLex.png")
    with colI4:
        st.subheader("Planning Management Fundamentals")
        st.markdown("##### AskLex PH Academy")

    #Safety Officer 2
    colG1, colG2, spaceG, colG3, colG4 = st.columns([2,4,1,2,4])
    with colG1:
        st.image("logo-bosh.png")
    with colG2:
        st.subheader("Safety Officer 2")
        st.markdown("##### FRREAL Occupational Health and Safety Training Services")

#Other Achievements
if selected == "Other Achievements":
    st.header("Lean Six Sigma and Continuous Improvement")
    colL1, colL2, colL3 = st.columns([1,1,1])
    with colL1:
        st.image("Screenshots/Time Management - Your Chill Pill for Time Stealers.png", caption="Time Management - Your Chill Pill for Time Stealers")
        st.image("Screenshots/Speak With POWER!.png", caption="Speak With POWER!")
        st.image("Screenshots/Graphical Analysis Using Minitab.png", caption="Graphical Analysis Using Minitab")
        st.image("Screenshots/Collaborating With Employees in Improving Culture and Processes.png", caption="Collaborating With Employees in Improving Culture and Processes")

    with colL2:
        st.image("Screenshots/Foundation of Risk Management - A Primer.png", caption="Foundation of Risk Management - A Primer")
        st.image("Screenshots/Honing Your Leadership Skills.png", caption="Honing Your Leadership Skills")
        st.image("Screenshots/Lean Product Development.png", caption="Lean Product Development")
        st.image("Screenshots/Presenting With Impact.png", caption="Presenting With Impact")
        
    with colL3:
        st.image("Screenshots/Good Manufacturing Practices (GMP) Primer.png", caption="Good Manufacturing Practices (GMP) Primer")
        st.image("Screenshots/How Lean Six Sigma Practitioners Think?.png", caption="Lean Six Sigma Practitioners")
        st.image("Screenshots/Introduction to Project Management.png", caption="Introduction to Project Management")
        st.image("Screenshots/Lean Six Sigma White Belt.png", caption="Lean Six Sigma White Belt")

    st.header("Data Analytics")
    colM1, colM2, colM3 = st.columns([1,1,1])
    with colM1:
        st.image("Screenshots/Automation with MS Excel VBA.png", caption="Automation with MS Excel VBA")
        st.image("Screenshots/Operational Analytics.png", caption="Operational Analytics")
        st.image("SS/Getting Grounded on Analytics.png", caption="Getting Grounded on Analytics")
        st.image("SS/Data Management Fundamentals.png", caption="Data Management Fundamentals")
        st.image("SS/Analytics Applications in Operations.png", caption="Analytics Applications in Operations")
        st.image("SS/Data Visualization Using Tableau and Python.png", caption="Data Visualization Using Tableau and Python")
        st.image("SS/Urban Planning in the Fourth Industrial Revolution.png", caption="Urban Planning in the Fourth Industrial Revolution")
        
    with colM2:
        st.image("Screenshots/The ALPHA of Data Science.png", caption="The ALPHA of Data Science")
        st.image("Screenshots/Big Data Applications.png", caption="Big Data Applications")
        st.image("SS/Computing in Python.png", caption="Computing in Python")
        st.image("SS/Enterprise Data Governance.png", caption="Enterprise Data Governance")
        st.image("SS/Storytelling Using Data.png", caption="Storytelling Using Data")
        st.image("SS/Essential Excel Skills for Data Preparation and Analysis.png", caption="Essential Excel Skills for Data Preparation and Analysis")

    with colM3:
        st.image("Screenshots/Analytics 101 for Businesses.png", caption="Analytics 101 for Businesses")
        st.image("Screenshots/THE DEEP TRUTH - Introduction to Deep Learning and AI.png", caption="Introduction to Deep Learning and AI")
        st.image("SS/SQL for Data Engineering.png", caption="SQL for Data Engineering")
        st.image("SS/Data-Driven Research Fundamentals.png", caption="Data-Driven Research Fundamentals")
        st.image("SS/Dashboards and Drill-Down Analytics.png", caption="Dashboards and Drill-Down Analytics")
        st.image("SS/Livable and Sustainable Cities in e-Governance.png", caption="Livable and Sustainable Cities in e-Governance")

