from fastapi import FastAPI
import subprocess
import os


app = FastAPI(title="Logicboard")


@app.get("/")
def root():
	return {
	"status": "online",
	"message": "Backend Active"
	}