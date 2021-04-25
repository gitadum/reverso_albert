#! /bin/bash

if [ -d /usr/share/albert/org.albert.extension.python/modules/reverso_context ]
then
    cp reverso_albert.py /usr/share/albert/org.albert.extension.python/modules/reverso_context/__init__.py
else
    pushd .
    pushd /usr/share/albert/org.albert.extension.python/modules
    mkdir reverso_context
    popd
    cp reverso_albert.py /usr/share/albert/org.albert.extension.python/modules/reverso_context/__init__.py
    popd
fi