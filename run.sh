#!/bin/bash
# this script installs dependencies and starts a jupyter notebook server
# note this script assumes you have
#	- a unix system
#	- a version of python 3.6
#	- an anaconda install
#	- a version of anaconda
conda create -n cs145project_904331855 python=3.6 anaconda
source activate cs145project_904331855
pip install gensim
jupyter notebook