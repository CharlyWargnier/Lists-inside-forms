import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar

st.header("Assigning 🐍 Python lists inside `st.form`")

en_words = [
    "streamlit",
    "has",
    "you",
    "covered",
]

es_words = [
    "streamlit",
    "tiene",
    "usted",
    "cubierto",
]

lang = st.radio("Choose language", ["🇬🇧 English", "🇪🇸 Spanish"])

words = []
if lang == "🇬🇧 English":
    words = en_words
elif lang == "🇪🇸 Spanish":
    words = es_words

word_choices = []

st.write("---")
st.markdown("## FORM")

with st.form(key="words_form_1", clear_on_submit=True):

    st.markdown(f"Choose some word options in {lang}")

    word_choices = st_tags(
        label="",
        text="Add labels - 3 max",
        value=words,
        maxtags=4,
    )

    st.form_submit_button("Apply")
