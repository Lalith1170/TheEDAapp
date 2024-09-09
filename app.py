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

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    pr.to_file("profile_report.html")

    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')

    # Use Streamlit components to render the HTML file
    with open("profile_report.html", "r") as f:
        html_data = f.read()

    st.components.v1.html(html_data, height=1000, scrolling=True)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        pr.to_file("profile_report.html")

        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')

        # Use Streamlit components to render the HTML file
        with open("profile_report.html", "r") as f:
            html_data = f.read()

        st.components.v1.html(html_data, height=1000, scrolling=True)
