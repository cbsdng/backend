#!/bin/sh


set -e


export BIN_DIR=`dirname $0`
export PROJECT_ROOT="${BIN_DIR}/.."
export FLASK_ENV="testing"
. "${PROJECT_ROOT}/name.py"
. ${BIN_DIR}/common.sh
setup


if [ "${SYSPKG}" = "no" ]; then
  if [ "${OFFLINE}" != "yes" ]; then
    pip install -U -r requirements_dev.txt
  fi
else
  sudo pkg install -y py37-flake8 py37-pytest-flask py37-pytest-factoryboy py37-pytest-cov
fi


CI=${1}
if [ "${CI}" = "ci" ]; then
  cp local_config_ci.py local_config.py
fi


rm -rf `find . -name __pycache__`
rm -rf .pytest_cache
flake8 .
py.test --cov="${app_name}" --cov-report=term-missing:skip-covered --cov-report=xml
