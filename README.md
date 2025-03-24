1.# FastAPI-K8s
The evolution of  creating one FastAPI application from Scratch & etc ,play around with version Control,DB and whatever you know about programming step by step with all modern Technologies, Components such as :AWS,A8s,Docker,Terrafurm,Ansible and etc


Simple FastAPI App:
--------------------
Instruction for this app as following step by step:
this app has been delveloped in  Ubuntu :
Dependencies, packages &  All syntaxes guidline to develop :

Ubuntu Environment:Install Dependencies & Packages, On venv  instruction:
---------------------------------------------------------------------------
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt (your requirements.txt file should be in  " in your project directory")
   pip list
   /MyProjects/FastAPI-K8s/P1_FastAPI-K8s$ uvicorn man:app --reload

How to run:
-Activate your virtual in your porject directory where you can see  venv , requirements.txt 
   $ source ./venv/bin/activate
   MyProjects/FastAPI-K8s/P1_FastAPI-K8s$  uvicorn main:app --reload
   http://127.0.0.1:8000/

# steps:
step 1: create a simple FastAPi to fetch data from Brower
A new Developer,dev1 needed: create a  Dev1 branch 
A frontEnd wanted:
