import streamlit as st
from streamlit_option_menu import option_menu
import requests 
from streamlit_lottie import st_lottie
from PIL import Image

# page config
st.set_page_config(page_title="Chloe's Portfolio", layout="centered", initial_sidebar_state="auto", page_icon=":sparkles:")

# input animations from lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: 
        return None
    return r.json()

lottie_coder = load_lottieurl("https://lottie.host/73562ab9-4415-4dfa-97d0-d1288f0fd646/e5JeSHHGeZ.json")

# load project
image = Image.open("assets/student LA.png")
image2 = Image.open("assets/student LA.png")
image_3 = Image.open("assets/app.png")
image_4 = Image.open("assets/ml.png")
image_5 = Image.open("assets/market_basket.png")

# create title and header section
with st.container():
    col1, col2 = st.columns(2, gap="large") 
    with col1:
        st.image("./assets/circle2.png", use_column_width=True)
    with col2:
        st.subheader("Hey there! My name is")
        st.title('Chloe')
        st.write("""I'm a final year business analytics student, with a background in data analytics and data science. 
                Check out some of the projects that I have worked on!
                 
                 """)
        st.write("---")

# add line 
st.markdown("<br>", unsafe_allow_html=True)

# create option menu
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects'],
        icons=['person', 'code-slash'],
        orientation='horizontal'
    )

    # define condition for first option, about 
    if selected == 'About':

        # create education container
        with st.container():
                st.subheader("Education")
                st.write("""
                    <strong>Singapore University of Social Sciences (SUSS)</strong><br>
                    Bachelor of Science in Business Analytics with Minor in Cloud Computing<br>
                    Grade: 4.19/5.0
                """, unsafe_allow_html=True)
                st.write("---")

        # create skills container
        with st.container():
            col3, col4 = st.columns([1, 2])
            with col4:
                st.subheader("Hard Skills")
                st.write("""
                        - Programming: Python, SQL, Apache Spark
                        - Data Wrangling: Webscraping, Text Mining, Machine Learning with SPSS Modeler/Python
                        - Data Visualisation: PowerBI, Tableau, Python, Excel 
                        """)
                st.write("---")
            with col3: 
                st_lottie(lottie_coder)
        
        # create experiences container
        with st.container():
            st.subheader("Experiences")
            st.write("""
                    <strong>LVMH Perfume & Cosmetics, Guerlain</strong><br>
                    Regional Data Analyst Intern<br>
                """, unsafe_allow_html=True)
            st.write("""
            - Managed data extraction, analysis and user requests for APAC in Excel Database and Adobe Campaign. 
            - Developed and maintained PowerBI dashboards to track daily retail KPIs.
            - Built an association rule model and developed a web app to identify key associations in a basket for cross-selling.
            - Streamlined monthly data handling and automated workflow, data cleaning, processing and visualising.
            - Conducted research and analysis on consumer behavioral trends in travel retail and local markets.
            - Collaborated with internal stakeholders and teams to carry out marketing campaigns.
            """)

            st.write("---")
            st.write("""
                    <strong>CPF Board</strong><br>
                    Data Science Intern<br>
                    """, unsafe_allow_html=True)
            st.write("""
            - Converted SAS programs to functional statistical reports in PySpark as part of UDP migration initiative. 
            - Debugged scripts using PySpark, SQL and SAS in the Azure DataBricks environment.
            -Co-facilitated company-wide workshops on the use of Azure Purview, Databricks and PowerBI. 
            - Provided company-wide consulting, offering specialized support in PySpark queries and resolving related issues. 
            """)
            st.write("---")
            
            st.write("""
                    <strong>DL Technology Pte Ltd</strong><br>
                    Operations Manager<br>
                    """, unsafe_allow_html=True)
            st.write("""
            - Managed procurement, point of sales and accounting operations.
            - Spearheaded clientele projects, leading on-site assessments and installation of products. 
            - Liaised with clients and stakeholders to ensure effective communication and project alignment. 
            - Proposed and executed marketing campaigns, including the design of product infographics. 
            """)
            st.write("---")

    # define condition for second option, projects
    if selected == "Projects":

        # create project 1 container 
        with st.container():
            st.header("My Projects")
            st.write("##")
            col5, col6 = st.columns([1, 2], gap="large")
            with col5:
                st.image(image)
            with col6:
                st.subheader("Learning Analytics: Prediction of Students At-Risk of Dropout in MOOCs")
                st.write("""
                        [FYP] This project focuses on data mining, data processing and data modelling through machine learning algorithms. 
                        Predictive models built in Python:
                        - Random Forest 
                        - Decision Tree
                        - Logistic Regression
                         """)
                st.write("---")
        # create project 2 container 
        with st.container():
            st.write("##")
            col6, col7 = st.columns([1, 2], gap="large")
            with col6:
                st.image(image_4)
            with col7:
                st.subheader("Machine Learning: Prediction of Diabetes")
                st.write("""
                        This is an exploratory project where i tried out building ensemble models and Optuna, a package for hyperparameter optimization, as well as the development of webapp with streamlit to deploy my model. 
                        Check out the EDA on the dataset here: https://github.com/chloeongln/diabetes-predictor/blob/main/eda-dpd.ipynb
                        
                        Summarised takeaways of project:
                       - Although ensemble models increase model performance compared to individual models, if a dataset is imbalanced, the overall model performance may still not be as accurate.
                       - Hence, even if balancing is performed, the use of oversampling cannot be too extreme as well due to noise and overfitting. Thus, it is always best to strive for a balanced dataset during data collection.  
                         """)
        st.image(image_3)
        st.write("---")
        # create project 3 container 
        with st.container():
            st.write("##")
            col8, col9 = st.columns([1, 2], gap="large")
            with col8:
                st.image(image_5)
            with col9:
                st.subheader("Market Basket Analysis: Association for Cross-Selling")
                st.write("""
                        - Built a association rule model for Guerlain analytics team to identify associated products in a basket.
                        - Developed webapp with streamlit to deploy model for internal usage. 
                         """)
        st.write("---")
