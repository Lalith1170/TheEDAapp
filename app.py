import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

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
@st.cache_data
def load_csv(file):
    try:
        return pd.read_csv(file, encoding='utf-8')
    except Exception as e:
        st.error(f"Error reading the CSV file: {e}")
        return None

# Function to generate the profiling report
@st.cache_data
def generate_profile_report(data):
    return ProfileReport(data, explorative=True, minimal=True)

# Main section of the app
if uploaded_file is not None:
    df = load_csv(uploaded_file)

    if df is not None:
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')

        # Generate and display the profiling report
        with st.spinner('Generating profiling report...'):
            profile_report = generate_profile_report(df)
            st.header('**Pandas Profiling Report**')

            # Use streamlit's `st.components.v1.html` for displaying the report in the app
            st.components.v1.html(profile_report.to_html(), height=1000, scrolling=True)
else:
    st.info('Awaiting CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_example_data():
            return pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )

        df = load_example_data()

        st.header('**Example Input DataFrame**')
        st.write(df)
        st.write('---')

        with st.spinner('Generating profiling report...'):
            profile_report = generate_profile_report(df)
            st.header('**Pandas Profiling Report**')

            # Use streamlit's `st.components.v1.html` for displaying the report in the app
            st.components.v1.html(profile_report.to_html(), height=1000, scrolling=True)
