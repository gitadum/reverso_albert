![english_to_french](https://github.com/gitadum/reverso_albert/blob/master/reverso-albert.png?raw=true)

Translates words between 15 languages within your albert launcher.

# Installation

## Prerequisites

* `albert`
* `reverso_api`

If you haven't already, install albert by following these steps: https://albertlauncher.github.io/installing/

This extension is based on the Reverso Context translator API for Python. You can install it by running:
`pip install reverso_api` on your terminal.

## Installation steps

1. To install this extension, just copy the script `reverso_albert.py` to `/usr/share/albert/org.extension.python/modules/reverso_albert/__init__.py`

! IMPORTANT : if you use several Python interpreters on your local machine, make sure that the `reverso_api` module is accessible to the interpreter used by albert. To do so, add the module location to sys.path within the script by inserting

```
import sys
sys.path.append('/path/to/reverso_api_module/')
```

2. Start albert launcher and go to Settings > Extensions > Python (if you haven't already, tick the checkbox to enable the use of Python extensions within the launcher)
3. Tick the 'Reverso Context' checkbox

# Use

To translate words between two languages, type queries that follow this pattern:
```
rev <source_language_letter_code> <target_language_letter_code> <words_to_translate>
```
15 languages are available:

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
