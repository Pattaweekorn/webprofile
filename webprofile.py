import streamlit as st

# Page configuration
st.set_page_config(page_title="Pattaweekorn", page_icon="🔰")

# Title
st.title("🔰Hello!")

# Introduction
st.subheader("I'm Pattaweekorn Piriyayothakul (Oat)")
st.write("""
- 2021 - Roblox developer
- 2021 - Debsirin band percussion elite personal [Debsirin band Bangkok](https://www.debsirinband.com/)
- 2021 - Student in Mini English Programs [Debsirin Bangkok](https://debsirin.ac.th/)
- 2024 - Student in Intensive English Programs [Debsirin Bangkok](https://debsirin.ac.th/)
""")

# Current Activities
st.subheader("🧑‍💻 What I'm Doing Now")
st.write("""
- 💻 Studying Computer Science
- 🔰 Studying Intensive English Programs at Debsirin school
- 🚩 Developing a Roblox map
- 🔰 Debsirin band percussion elite personal
""")

# Tech Stack & Skills
st.subheader("📚 Tech Stack & Skills")

# Debsirin stuff 🔰
with st.expander("🔰 Debsirin school"):
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTY6ff38zHikTUy7C2_MxGYfiIcGRFjnx5Ycg&s", use_column_width=True)
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSmpeRrcpqhosat9l4E_maLgOrn6cRMmQijA&s", use_column_width=True)
    st.image("https://yt3.googleusercontent.com/ytc/AIdro_nr0O2fhCGlAbaMVyj5TiLq6vC918IkDv1pAWvbVa0Vrw=s900-c-k-c0x00ffffff-no-rj", use_column_width=True)

# Spacial skill
with st.expander("Spacial skill"):
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqhzVzcgNgd53IBtmjz56WNWPU5FwqzDuP_g&s", use_column_width=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Roblox_Studio_logo_-_2022.svg", use_column_width=True)

# Roblox developing
with st.expander("Roblox developing"):
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Roblox_Studio_logo_-_2022.svg", use_column_width=True)
    st.image("https://play-lh.googleusercontent.com/WNWZaxi9RdJKe2GQM3vqXIAkk69mnIl4Cc8EyZcir2SKlVOxeUv9tZGfNTmNaLC717Ht", use_column_width=True)
    st.image("https://pbs.twimg.com/profile_images/1036953347943743488/1dbRCWDq_400x400.jpg", use_column_width=True)
    st.image("https://loudbench.com/wp-content/uploads/2023/02/Python-logo-1024x576.png", use_column_width=True)

# Dev Tools
with st.expander("🐥 Dev Tools"):
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Roblox_Studio_logo_-_2022.svg", use_column_width=True)
    st.image("https://loudbench.com/wp-content/uploads/2023/02/Python-logo-1024x576.png", use_column_width=True)

# My Skills
st.subheader("🐥 My Skills")
st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Roblox_Studio_logo_-_2022.svg", use_column_width=True)

# Future Plans
st.subheader("🔮 What in Future")
st.write("""
- [ ] Study computer science in university (2026-2030)
- [ ] Start my own company/youtube channel(2024-future)
- [ ] Start developing my own Roblox map (2020-future)
""")

# Contact Information
st.subheader("📩 Contact")
st.write("""
- 📩 pattaweekorn52@gmail.com/s50216@debsirin.ac.th
- 📖 [Youtube](https://www.youtube.com/channel/UCWJvfd3Tdad2Xv-cJfM_Wyw)
""")

# GitHub Stats
st.subheader("GitHub Stats")
st.image("https://github-readme-stats.vercel.app/api?username=Pattaweekorn", use_column_width=True)

# Footer
st.write("Thank you krub for reading :) ")
