import uvicorn
import json 

from fastapi import FastAPI
from utils.enterpiseService import enterpiseService

app = FastAPI(debug=True)

@app.get("/")
def homeRoute():
  return { "message": "Welcome to API!" }

@app.get("/search/{socialReason}/{cnpj}")
def searchByCnpj(socialReason: str, cnpj: str):
   searchResult = enterpiseService().getEnterpise(socialReason=socialReason, cnpj=cnpj)
   return json.loads(searchResult)

@app.get("/search/{term}")
def searchByTerm(term: str):
   searchResult = enterpiseService().getListEnterprises(term=term)
   return searchResult


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)

# if __name__ == "__main__":
#   # enterpiseInstance = enterpiseService()
  
#   # listEnterpises = enterpiseInstance.getListEnterprises()
#   # print(listEnterpises)