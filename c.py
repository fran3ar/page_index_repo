import streamlit as st
from PIL import Image, ImageDraw
import os



# --- CSS para header fijo, botones y responsivo ---
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
        flex-wrap: wrap;
    }

    .custom-header a {
        color: white;
        font-weight: bold;
        text-decoration: none;
        background-color: #2e7d32;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 18px;
    }

    .custom-header a:hover {
        background-color: #1b5e20;
    }

    .block-container {
        padding-top: 100px;
    }

    .anchor-offset {
        display: block;
        height: 90px; /* Igual o un poco más que el header */
        margin-top: -90px;
        visibility: hidden;
    }

    /* Responsive: reducir tamaño de botones en móviles */
    @media (max-width: 600px) {
        .custom-header a {
            padding: 6px 12px;
            font-size: 14px;
            margin: 2px;
        }
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

home_container = st.container()

with home_container:    
    # --- Contenido principal ---
    st.markdown("---")  # separador visual
    # Ruta de la imagen
    image_path = os.path.join("files_folder", "profile_photo.jpg")  # o "image1.png"

    # Función para redondear esquinas de una imagen
    def round_corners(img, radius=50):
        # Asegura que la imagen tenga alpha
        img = img.convert("RGBA")
        # Crear máscara
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0) + img.size, radius=radius, fill=255)
        # Aplicar máscara
        img.putalpha(mask)
        return img

    # Usamos columnas: izquierda para texto, derecha para imagen
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Data Analyst")
        st.title("Hi, I'm Francisco")
        st.write(
            """
            I'm a passionate Data Analyst with experience in Python, SQL, Power BI and Streamlit.  
            I love turning data into insights and creating interactive dashboards that help teams make informed decisions.
            """
        )

    with col2:
        # Cargar y redondear imagen
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img_rounded = round_corners(img, radius=50)  # ajusta el radius según prefieras
            st.image(img_rounded)
        else:
            st.warning(f"Image not found: {image_path}")


for i in range(5):
    st.write(f"Línea Home {i+1}")

# Skills
st.markdown('<div id="skills" class="anchor-offset"></div>', unsafe_allow_html=True)
st.header("Skills")
st.write("Contenido de Skills...")
for i in range(5):
    st.write(f"Línea Skills {i+1}")

# Projects
st.markdown('<div id="projects" class="anchor-offset"></div>', unsafe_allow_html=True)
st.header("Projects")
st.write("Contenido de Projects...")
for i in range(5):
    st.write(f"Línea Projects {i+1}")
