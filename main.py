from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World 17.03.2025  this is  from dev1 added to this code to be merged with master"}

# DISCLAIMER !!! FRONTEND WANTED !
#  dev1 added
#  dev1  coded
#  dev1  coded
#  dev1  coded
#  dev1  coded
#  dev1  coded

# Master asks for a FrontEnd. this is just for practising Control version between several Developers and git branched,
# next week there will be  new  Frontedn join to our team !
# Message from Sine:Okay, Done . Got to work .....!
