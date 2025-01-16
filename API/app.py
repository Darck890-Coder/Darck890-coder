import os

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
        rows = ["Amin","Marce","Miranda"]
        return rows

@app.get("/superheroesDC")
def get_superheroesD():
        rows = ["Superman","Batman","Flas","Mujer Maravilla","Linterna Verde"]
        return rows