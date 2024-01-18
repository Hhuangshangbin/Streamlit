import streamlit as st
import pandas as pd

st.set_page_config(page_title="② NA patients vs. BP patients and NC patients vs. BP patients", page_icon="📈")

st.markdown("# ② NA patients vs. BP patients and NC patients vs. BP patients")
st.write(
"""
NA patients VS BP patients log-rank was non-significant but the difference was more pronounced before 10 days.NC patients VS BP patients log-rank was strongly significant and mortality rate was higher in NC patients (27.2%) than in BP patients (19.4%).
"""
)

from PIL import Image
st.image(Image.open("fig11.png"))
st.markdown("### Download [Test Cases](https://pan.baidu.com/) here")
st.markdown("#### :blue[Example:]")

data = pd.read_csv('process_heart.csv')
st.write(data)
uploader_file = st.file_uploader(label = "##### upload the dataset")

st.button('**Submit the data**')
