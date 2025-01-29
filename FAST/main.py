from fastapi import FastAPI

app= FastAPI()

#Endponit home

@app.get('/')
def home():
    return {'hello':'world FastAPI'}