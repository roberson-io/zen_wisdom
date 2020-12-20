#! /bin/bash

export LC_ALL=en_US.utf-8 && export LANG=en_US.utf-8
echo -e "\nisort: "
isort app tests
echo -e "\nBlack: "
black --fast --line-length 79 app tests
echo -e "\nFlake8: "
flake8 --tee --output-file=flake8.log app
echo -e "\nMyPy: "
mypy --ignore-missing-imports app
echo -e "\nBandit: "
bandit --ini .bandit -r -f txt
echo -e "\nSafety: "
safety check
