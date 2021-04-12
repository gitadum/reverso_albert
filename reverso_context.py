#! /usr/bin/env python3

import reverso_api.context

def get_fisrt_translation(source_text, source_lang, target_lang):

    api = reverso_api.context.ReversoContextAPI(source_text, '', source_lang, target_lang)
    results = list(api.get_translations())
    try:
        first_result = results[0][1]
    except:
        first_result = None

    return first_result