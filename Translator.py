import streamlit as st
from deep_translator import GoogleTranslator as gt
st.title("🌏 Language Translator")
st.write("Translate from 1 language to another")

LANGUAGES  = {
    "English": "en", "Spanish": "es", "French": "fr", "German": "de",
    "Italian": "it", "Hindi": "hi", "Chinese": "zh-CN", "Arabic": "ar",
    "Portuguese": "pt", "Japanese": "ja", "Korean": "ko", "Russian": "ru",
    "Tamil": "ta", "Telugu": "te", "Bengali": "bn", "Urdu": "ur"
}

text=st.text_area("Enter text to be translated here:",height=150)

col1,col2=st.columns(2)
lang=LANGUAGES.keys()
code=LANGUAGES.values()
with col1:
    source_lang=st.selectbox("Source Language",options=lang,index=0)
with col2:
    target_lang=st.selectbox("Target Language",options=lang,index=1)

if st.button("Translate"):
    if text.strip():
        code1=LANGUAGES[source_lang]
        code2=LANGUAGES[target_lang]

        trans_text=gt(source=code1,target=code2).translate(text)
        st.success(f"Translation:\n{trans_text}")

    else:
        st.warning("⚠️ Please enter text to translate")
