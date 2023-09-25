
import streamlit as st

st.markdown("""
    <div style='text-align:center; font-size: 40px;'>
        المرحوم قويدر علاونه
    </div>
""", unsafe_allow_html=True)
audio_url = "https://dl2.sura.pw/dl/reciter/1/32/001.mp3?h=tpbF6zaHPnBUmdu54vcwoQ&expires=1695739962&dl=true"
#audio_url='https://ia801400.us.archive.org/34/items/duaa-ommy_001/002.mp3'

image_url = "https://j.top4top.io/p_2824pxkzj1.jpg"

audio_html = f"""
    <audio autoplay controls style="display: none">
        <source src="{audio_url}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    """
st.markdown(audio_html, unsafe_allow_html=True)

image_html = f"""
    <img src="{image_url}" style="width: 500px; height: auto">
    """
st.markdown(image_html, unsafe_allow_html=True)
