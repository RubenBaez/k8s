#!/bin/bash
sudo easy_install virtualenv

virtualenv -p python3 tests_enviroment

source tests_enviroment/bin/activate

pip install -r requirements.txt 
