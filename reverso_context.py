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

def top_n_translations(source_text, source_lang, target_lang):

    n = 3
    api = reverso_api.context.ReversoContextAPI(source_text, '', source_lang, target_lang)
    results = list(api.get_translations())
    try:
        top_n_results = [result[1] for result in results[:n]]
        output = ""
        for result in top_n_results:
            output += result + ', '
        output = output[:-2]
    except:
        output = None

    return output

translate = top_n_translations(
    input('source text:'),
    input('source lang:'),
    input('target lang:')
)

print(translate)