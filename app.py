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
                    Regional Data Analyst<br>
                """, unsafe_allow_html=True)
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
