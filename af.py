import streamlit as st
from PIL import Image, ImageDraw
import os


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
