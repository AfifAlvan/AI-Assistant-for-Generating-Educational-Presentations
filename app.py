import streamlit as st
from generator.ai_generator import generate_materi
from generator.ppt_creator import buat_ppt
import os

st.set_page_config(page_title="Generator PPT", page_icon="📊")

st.title("📊 Generator PPT Materi Belajar Otomatis")

name = st.text_input("🧑 Nama Anda")
topic = st.text_input("📚 Topik Materi")

if st.button("🚀 Buat PPT"):
    if name and topic:
        with st.spinner("🔄 Sedang membuat ringkasan dan menyusun PPT..."):
            summary = generate_materi(topic)

            if not os.path.exists("output"):
                os.makedirs("output")
            ppt_path = buat_ppt(judul=topic, nama=name, isi=summary)

        st.success("✅ PPT berhasil dibuat!")
        st.subheader("📄 Ringkasan Materi:")
        st.write(summary)

        with open(ppt_path, "rb") as file:
            st.download_button(
                label="📥 Unduh PPT",
                data=file,
                file_name=f"materi_{topic.lower().replace(' ', '_')}.pptx",
                mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
            )
    else:
        st.warning("Mohon isi nama dan topik terlebih dahulu.")
