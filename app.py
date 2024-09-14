import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

# Web App Title
st.markdown('''
# **The EDA App**

This is the **EDA App** created in Streamlit using the **ydata-profiling** library.

**Credit:** App built in `Python` + `Streamlit` by [lalithxu](https://www.linkedin.com/in/lalith-adithya-u-47278920a/)

Explore your data like never before and make informed decisions with the EDA App!
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
    """)

# Function to load CSV data
@st.cache_resource
def load_csv(file):
    try:
        return pd.read_csv(file, encoding='utf-8')
    except UnicodeDecodeError:
        # Try another encoding if utf-8 fails
        return pd.read_csv(file, encoding='ISO-8859-1')

# Function to generate the profiling report
@st.cache_resource
def generate_profile_report(data):
    return ProfileReport(data, explorative=True, minimal=True, use_local_assets=True)

# Main section of the app
if uploaded_file is not None:
    try:
        # Load the CSV data
        df = load_csv(uploaded_file)
        
        # Display the DataFrame
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')

        # Generate and display the profiling report
        with st.spinner('Generating profiling report...'):
            profile_report = generate_profile_report(df)
            st.header('**Pandas Profiling Report**')

            # Display the profiling report directly in the app
            report_html = profile_report.to_html()
            html(report_html, height=1000, scrolling=True)
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
else:
    st.info('Awaiting CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_resource
        def load_example_data():
            return pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )

        # Load example dataset
        df = load_example_data()

        # Display the example DataFrame
        st.header('**Example Input DataFrame**')
        st.write(df)
        st.write('---')

        # Generate and display the profiling report for example dataset
        with st.spinner('Generating profiling report...'):
            profile_report = generate_profile_report(df)
            st.header('**Pandas Profiling Report**')

            # Display the profiling report directly in the app
            report_html = profile_report.to_html()
            html(report_html, height=1000, scrolling=True)
