import sys
import os

sys.path.append('../data_analysis_project')

from utils.fuctions import clean_comments_text, remove_stopwords



stop_words_spanish = [
    'a', 'al', 'algo', 'alguien', 'algún', 'alguna', 'algunas', 'algunos', 'ambos', 'ante', 'antes', 'aki', 'abajo', 
    'bien', 'como', 'comó', 'con', 'cmo', 'cual', 'cuando', 'cuándo', 'donde', 'dónde', 'durante', 'el', 'él', 'ella', 
    'ellas', 'ellos', 'en', 'entre', 'era', 'eras', 'éramos', 'eran', 'es', 'esa', 'esas', 'ese', 'esos', 'esta', 
    'estaba', 'estabas', 'estaban', 'estamos', 'estar', 'este', 'esto', 'estos', 'estoi', 'toy', 'fue', 'fui', 
    'fuese', 'fuesen', 'fueron', 'siendo', 'sino', 'son', 'soy', 'tal', 'tambn', 'tambien', 'también', 'tan', 'tanta', 
    'tantas', 'tanto', 'tantos', 'te', 'ti', 'tienes', 'tiene', 'tienen', 'tu', 'tú', 'tus', 'un', 'uno', 'unos', 
    'una', 'unas', 'veses', 'veces', 'y', 'ya', 'io', 'yo', 'mi', 'mí', 'mios', 'míos', 'tuyo', 'tuyos', 'suyo', 
    'suyos', 'mio', 'nos', 'nosotros', 'vosotros', 'su', 'sí', 'si', 'les', 'los', 'nuestras', 'nuestras', 'nuestros', 
    'otros', 'otra', 'otras', 'o', 'os', 'se', 'sé', 'asi', 'así', 'alli', 'allá', 'aka', 'aquí', 'ora', 'ahora', 
    'apenas', 'ante', 'aun', 'aún', 'además', 'aunque', 'como', 'cómo', 'contra', 'cual', 'cuales', 'cuando', 
    'cuándo', 'desde', 'de', 'despues', 'después', 'dice', 'dijo', 'dixo', 'dicho', 'donde', 'dónde', 'dos', 'durante', 
    'e', 'él', 'ella', 'ellas', 'ellos', 'en', 'entre', 'era', 'eras', 'eran', 'es', 'esa', 'esas', 'ese', 'eso', 
    'esos', 'esta', 'estan', 'están', 'estar', 'este', 'esto', 'estos', 'toy', 'toi', 'fue', 'fui', 'fueron', 
    'fueron', 'fuesen', 'fui', 'hago', 'izo', 'hizo', 'hemos', 'asta', 'hasta', 'hay', 'iba', 'iban', 'iwal', 'igual', 
    'incluso', 'ir', 'está', 'estabamos', 'estamos', 'estan', 'iban', 'igual', 'incluso', 'ir', 'acia', 'hacia', 'ha', 
    'había', 'había', 'asta', 'hice', 'izo', 'hizo', 'la', 'las', 'lo', 'los', 'más', 'mas', 'menos', 'me', 'mí', 
    'misma', 'mismas', 'mismo', 'mismos', 'muy', 'mucho', 'muxo', 'muchos', 'nada', 'ni', 'no', 'nos', 'nosotros', 
    'o', 'otra', 'otras', 'otros', 'para', 'pero', 'poco', 'por', 'porq', 'porque', 'porqué', 'cual', 'cuál', 
    'cuales', 'cuáles', 'cuando', 'cuándo', 'que', 'qué', 'se', 'sin', 'sobre', 'soy', 'sólo', 'solo', 'su', 'sus', 
    'también', 'tambn', 'tan', 'tanta', 'tantas', 'tanto', 'tantos', 'tiene', 'tu', 'tuya', 'tuyas', 'tuyo', 'tuyos', 
    'un', 'una', 'unas', 'uno', 'unos', 'ya'
]































