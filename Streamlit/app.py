import streamlit as st
import joblib
import os
import sys
import numpy as np

# Agregar la ruta base para asegurar que pueda cargar el módulo 'back'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.back import limpiar_texto, ods_images

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Identificador de ODS",
        page_icon="🌍",
        layout="centered"
    )

    # Reducir el espacio en blanco de la parte superior
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)

    # Título principal
    st.title("Identifica el ODS de tu texto")
    
    st.markdown("""
        Ingresa un texto relacionado con alguna temática o problema, y nuestro modelo de Machine Learning
        analizará su contenido para identificar a cuál **Objetivo de Desarrollo Sostenible (ODS)** se alinea mejor.
    """)

    # Cargar el modelo
    @st.cache_resource
    def cargar_modelo():
        ruta_modelo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'modelo', 'modelo_clasificador_ODS.pkl')
        try:
            modelo = joblib.load(ruta_modelo)
            return modelo
        except Exception as e:
            st.error(f"Error al cargar el modelo: {e}")
            return None

    modelo = cargar_modelo()

    # Caja de texto para el usuario
    texto_usuario = st.text_area("Ingresa tu texto aquí:", height=100, placeholder="Escribe o pega tu texto aquí...")

    # Botón de enviar
    if st.button("Enviar", type="primary", use_container_width=True):
        if not texto_usuario.strip(): 
            st.warning("⚠️ Por favor ingresa un texto antes de enviar.")
        else:
            if modelo is not None:
                with st.spinner("Analizando el texto..."):
                    # 1. Limpiar el texto usando la función del back
                    texto_limpio = limpiar_texto(texto_usuario)
                    
                    try:
                        # 2. Pasar el texto al modelo (el modelo espera un texto directo, o lista de un elemento según la implementación del pipeline)
                        # Nota: scikit-learn pipelines usualmente esperan un iterable (lista/array) de strings, 
                        # incluso si es un solo texto. Agregamos manejo para ambos casos posibles.
                        try:
                            prediccion = modelo.predict(texto_limpio)
                        except ValueError:
                            # Si falla porque espera un array 1D
                            prediccion = modelo.predict([texto_limpio])
                        
                        # Obtener el ID del ODS (asumiendo que devuelve el ID directamente o en una lista)
                        id_ods = prediccion[0] if isinstance(prediccion, (list, tuple, np.ndarray)) else prediccion
                        
                        # 3. Obtener la imagen del ODS desde el diccionario
                        # Intentar castear a int por si el modelo devuelve un string '1' o un tipo numpy
                        try:
                            id_ods_int = int(id_ods)
                            imagen_ods = ods_images.get(id_ods_int)
                        except (ValueError, TypeError):
                            imagen_ods = ods_images.get(id_ods)
                        
                        # Mostrar el resultado
                        st.success("¡Análisis completado!")
                        
                        col1, col2 = st.columns([3, 1])
                        
                        with col1:
                            # Mostrar el resultado en una tarjeta con flexbox para la imagen a la derecha
                            st.markdown(f"""
                            <div style="padding: 20px; border-radius: 10px; background-color: #f0f2f6; border-left: 5px solid #0068c9; margin-top: 10px; height: 100%; display: flex; flex-direction: column; justify-content: center;">
                                <h3 style="margin-top:0; color: #31333F;">Resultado del Modelo:</h3>
                                <p style="font-size: 18px; margin-bottom: 0;"><strong>Clasificación:</strong> ODS {id_ods}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        with col2:
                            if imagen_ods:
                                st.image(imagen_ods, use_container_width=True)
                            else:
                                st.warning(f"No se encontró imagen para el ODS {id_ods}")
                        
                        # Opcional: mostrar texto limpio en un expander para depuración
                        with st.expander("Ver texto procesado internamente"):
                            st.write(texto_limpio)

                        st.markdown("<br><br>", unsafe_allow_html=True)
                            
                    except Exception as e:
                        st.error(f"Error durante la predicción: {e}")
            else:
                st.error("El modelo no está disponible. Revisa la carga del archivo .pkl.")
                
    # Footer Fijo
    st.markdown("""
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f8f9fa;
                color: #6c757d;
                text-align: center;
                padding: 10px 0;
                font-size: 12px;
                border-top: 1px solid #dee2e6;
                z-index: 999;
            }
        </style>
        <div class="footer">
            Desarrollado por: <strong>German Pinzon y Diego Klinger</strong> | MAIA-2026
        </div>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
