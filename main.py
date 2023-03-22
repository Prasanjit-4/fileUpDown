# from typing import Annotated
import os
import pyrebase
from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

firebaseConfig = {
  "apiKey": "AIzaSyC4MwBj71vtYXgNha7cGAih8GJqlUNkbVQ",
  "databaseURL":"gs://storemyfiles-992b7.appspot.com",
  "authDomain": "storemyfiles-992b7.firebaseapp.com",
  "projectId": "storemyfiles-992b7",
  "storageBucket": "storemyfiles-992b7.appspot.com",
  "messagingSenderId": "19403315786",
  "appId": "1:19403315786:web:402009d00ca58b082164b3",
  "measurementId": "G-H32LGJZKRL"
}

firebase=pyrebase.initialize_app(firebaseConfig)


storage=firebase.storage()

@app.post('/upload')
async def uploadFile(file:UploadFile = File(...)):
  file_type = file.filename.split('.').pop()
  file_name = file.filename[:-len(file_type)-1]
  
  with open(file.filename,"wb") as buffer:
    shutil.copyfileobj(file.file,buffer)
  storage.child(file.filename).put(file.filename)
  os.remove(file.filename)
  return {"fileName":file.filename}
  
  