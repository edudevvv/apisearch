import uvicorn
import json 

from fastapi import FastAPI, Request
from service.enterpiseService import enterpiseService

app = FastAPI(debug=True)
service = enterpiseService()

@app.get("/")
def homeRoute():
  return { "message": "Welcome to Basi Searchs.", "additionals": { "developer": "https://github.com/edudevvv", "lastUpdated": "01/03/2025" } }

@app.get("/search/{socialReason}/{cnpj}")
def searchByCnpj(socialReason: str, cnpj: str):
   searchResult = service.getEnterpise(socialReason=socialReason, cnpj=cnpj)
   return json.loads(searchResult)

@app.post("/search")
async def searchByTerm(req: Request):
   body = await req.json()

   searchResult = service.getListEnterprises(payload=body)
   return searchResult

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000, reload=True)