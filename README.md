![english_to_french](https://github.com/gitadum/reverso_albert/blob/master/reverso-albert.png?raw=true)

With this python extension for the albert launcher, you can translate terms between 14 languages!

# Installation

## Prerequisites

* `albertlauncher`
* `reverso_api`

This extension is based on the Reverso Context translator API for Python. You can install it by running:
`pip install reverso_api` on your terminal.

## Installation steps

1. To install this extension, just copy the script `reverso_albert.py` to `/usr/share/albert/org.extension.python/modules/reverso_albert/__init__.py`

! IMPORTANT : if you use several Python interpreters on your local machine, make sure that the `rerverso_api` module is accessible to the interpreter used by albert. To do so, add the module location to sys.path within the script by inserting

```
import sys
sys.path.append('/path/to/reverso_api_module/')
```

2. Start albert launcher and go to Settings > Extensions > Python and tick the 'Reverso Context' checkbox

# Use

To translate terms between two languages, type queries that follow this pattern :
```
rev <source_language_letter_code> <target_language_letter_code> <term_or_text_to_translate>
```
14 languages are available :

* Arabic (`ar`)
* Chinese (`zh`)
* Dutch (`nl`)
* English (`en`)
* French (`fr`)
* German (`de`)
* Hebrew (`he`)
* Italian (`it`)
* Japanese (`ja`)
* Polish (`pl`)
* Portuguese (`pt`)
* Romanian (`ro`)
* Russian (`ru`)
* Spanish (`es`)
* Turkish (`tr`)

Enjoy!
