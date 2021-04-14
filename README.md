With this extension for albert launcher, you can translate terms between these 14 languages :

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

![english_to_french](https://github.com/gitadum/reverso_albert/blob/master/reverso-albert.png?raw=true)

# Installation

## Prerequisite

* `reverso_api`

This extension is based on the Reverso Context translator API for Python. You can install it by running:
`pip install reverso_api` on your terminal.

## Installation steps

To install this extension, just move the script `reverso_albert.py` to `/usr/share/albert/org.extension.python/modules/reverso_albert/__init__.py`
! IMPORTANT : if you use several interpreters add the `¶everso_api` module location to path within the script by inserting 
`import sys`
`sys.path.append('/path/to/reverso_api_module/')`
