# -*- coding: utf-8 -*-

"""Translate text using Reverso Context.
Based on Manuel Schneider Google Translate extension.

Synopsis: <trigger> <src_lang> <dest_lang> <text>"""

import sys
#sys.path.insert(0, '/usr/bin/anaconda3/lib/python3.8/site-packages/')
sys.path.append('/usr/bin/anaconda3/lib/python3.8/site-packages/')
import reverso_api.context

from albert import *

__title__ = "Reverso Context"
__version__ = "0.0.2"
__triggers__ = "rev "
__authors__ = "adum"

iconPath = iconLookup('config-language') or ":python_module"

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

def handleQuery(query):
    if query.isTriggered:
        fields = query.string.split()
        item = Item(id=__title__, icon=iconPath)
        if len(fields) >= 3:
            src = fields[0]
            dst = fields[1]
            txt = " ".join(fields[2:])
            result = top_n_translations(txt, src, dst)
            item.text = result
#           item.subtext = "%s-%s translation of %s" % (src.upper(), dst.upper(), txt)
            item.subtext = ""
            item.addAction(ClipAction("Copy translation to clipboard", result))
            return item
        else:
            item.text = __title__
            item.subtext = "Enter a query in the form of \"&lt;srclang&gt; &lt;dstlang&gt; &lt;text&gt;\""
            return item
