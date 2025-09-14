import streamlit as st

# --- CSS para header fijo y enlaces ---
st.markdown(
    """
    <style>
    header {visibility: hidden;}

    .custom-header {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 80px;
        background-color: #4CAF50;
        color: white;
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 30px;
    }

    .custom-header a {
        color: white;
        font-weight: bold;
        text-decoration: none;
        background-color: #2e7d32;
        padding: 10px 20px;
        border-radius: 5px;
    }

    .custom-header a:hover {
        background-color: #1b5e20;
    }

    .block-container {
        padding-top: 100px;
    }

    /* Div invisible para offset de ancla */
    .anchor-offset {
        display: block;
        height: 90px; /* Igual o un poco más que el header */
        margin-top: -90px;
        visibility: hidden;
    }
    </style>

    <div class="custom-header">
        <a href="#home">🏠 Home</a>
        <a href="#skills">🛠️ Skills</a>
        <a href="#projects">🚀 Projects</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- SECCIONES CON OFFSET ---
# Home
st.markdown('<div id="home" class="anchor-offset"></div>', unsafe_allow_html=True)
st.title("Home")
st.write("Contenido de Home...")
for i in range(50):
    st.write(f"Línea Home {i+1}")

# Skills
st.markdown('<div id="skills" class="anchor-offset"></div>', unsafe_allow_html=True)
st.header("Skills")
st.write("Contenido de Skills...")
for i in range(50):
    st.write(f"Línea Skills {i+1}")

# Projects
st.markdown('<div id="projects" class="anchor-offset"></div>', unsafe_allow_html=True)
st.header("Projects")
st.write("Contenido de Projects...")
for i in range(50):
    st.write(f"Línea Projects {i+1}")
