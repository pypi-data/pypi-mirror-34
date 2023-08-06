#!/usr/bin/env bash

curl -s -L http://pypi.baidu.com/static/pyenv/pyenv-installer | bash
pyenv virtualenv 3.6.5 venv
pyenv activate venv

pip install pybuilder
pyb -v