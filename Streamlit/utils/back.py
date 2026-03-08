import re
import nltk
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
from nltk.corpus import stopwords


def limpiar_texto(texto: str) -> str:
    """Limpia y normaliza un texto en español."""
    # Minúsculas
    texto = texto.lower()
    # Elimina chars no alfabéticos (conserva letras con tilde y ñ)
    texto = re.sub(r'[^a-záéíóúüñ\s]', ' ', texto)
    # Tokeniza por palabra
    tokens = texto.split()
    # Filtra stopwords y palabras muy cortas
    tokens = [t for t in tokens if t not in set(stopwords.words('spanish')) and len(t) > 2]
    return ' '.join(tokens)



# Extraídos de https://sdgs.un.org/es/goals:

ods_list = {
    1: 'Fin de la pobreza',
    2: 'Hambre cero',
    3: 'Salud y bienestar',
    4: 'Educación de calidad',
    5: 'Igualdad de género',
    6: 'Agua limpia y saneamiento',
    7: 'Energía asequible y no contaminante',
    8: 'Trabajo decente y crecimiento económico',
    9: 'Industria, innovación e infraestructura',
    10: 'Reducción de las desigualdades',
    11: 'Ciudades y comunidades sostenibles',
    12: 'Producción y consumo responsables',
    13: 'Acción por el clima',
    14: 'Vida submarina',
    15: 'Vida de ecosistemas terrestres',
    16: 'Paz, justicia e instituciones sólidas',
    17: 'Alianzas para lograr los objetivos',
}


ods_images = {
    1: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-01-400x400.png',
    2: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-02-400x400.png',
    3: 'https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-03.png',
    4: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-04-400x400.png',
    5: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-05-400x400.png',
    6: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-06-400x400.png',
    7: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-07-400x400.png',
    8: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-08-400x400.png',
    9: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-09-400x400.png',
    10: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-10-400x400.png',
    11: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-11-400x400.png',
    12: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-12-400x400.png',
    13: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-13-400x400.png',
    14: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-14-400x400.png',
    15: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-15-400x400.png',
    16: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/09/S-WEB-Goal-16-400x400.png',
    17: 'https://www.un.org/sustainabledevelopment/wp-content/uploads/sites/3/2019/10/S_SDG_PRINT-17-400x400.jpg',
}