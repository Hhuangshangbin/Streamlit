import streamlit as st
import pandas as pd

st.set_page_config(page_title="① ON patients vs. BP patients", page_icon="📈")

st.markdown("# ① ON patients vs. BP patients")
st.write(
    """This is the result of the population survival curves of ON patients and BP patients, which shows that the log-rank is statistically significant, but the significant relationship, after using multifactorial cox analysis, is still relevant for comparative studies between ON patients and BP patients.
"""
)

from PIL import Image
st.image(Image.open("fig10.png"))
st.markdown("### Download [Test Cases](https://pan.baidu.com/) here")
st.markdown("#### :blue[Example:]")

data = pd.read_csv('process_heart.csv')
st.write(data)
uploader_file = st.file_uploader(label = "##### upload the dataset")

st.button('**Submit the data**')
