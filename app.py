import os
os.environ["STREAMLIT_WATCHED_MODULES"] = ""

import streamlit as st
from generator.ai_generator import generate_materi
from generator.ppt_creator import buat_ppt
import os

st.set_page_config(page_title="Generator PPT", page_icon="📊")

st.title("📊 AI Assistant for Generating Educational Presentations")

name = st.text_input("🧑 Name")
topic = st.text_input("📚 Topic")

if st.button("🚀 Buat PPT"):
    if name and topic:
        with st.spinner("🔄 Loading..."):
            summary = generate_materi(topic)

            if not os.path.exists("output"):
                os.makedirs("output")
            ppt_path = buat_ppt(judul=topic, nama=name, isi=summary)

        st.success("✅ PPT already created!")
        st.subheader("📄 Summary:")
        st.write(summary)

        with open(ppt_path, "rb") as file:
            st.download_button(
                label="📥 Unduh PPT",
                data=file,
                file_name=f"materi_{topic.lower().replace(' ', '_')}.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
    else:
        st.warning("Please fill the name and topic")
