import os

def get_system_language():
    lang = os.getenv('LANG')

    if lang:
        lang_code = lang.split('.')[0].split('_')[0]
        return lang_code
    else:
        return None

# Exemple d'utilisation
system_language = get_system_language()