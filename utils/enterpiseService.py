import json 

from lxml import html
from tls_client import Session

class enterpiseService:
  def __init__(self):
    self.session = Session(random_tls_extension_order=True, client_identifier="chrome_130")
    self.headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }

  def getListEnterprises(self, term: str):
    payload = json.dumps({
        "query": {
              "termo": [term],
              "atividade_principal": [],
              "natureza_juridica": [],
              "uf": ["SP"],
              "municipio": ["SAO PAULO"],
              "bairro": [],
              "situacao_cadastral": "ATIVA",
              "cep": [],
              "ddd": [],
          },
          "range_query": {
              "data_abertura": { "lte": None, "gte": None },
              "capital_social": { "lte": None, "gte": None },
          },
          "extras": {
              "somente_mei": False,
              "excluir_mei": True,
              "com_email": True,
              "incluir_atividade_secundaria": False,
              "com_contato_telefonico": True,
              "somente_fixo": False,
              "somente_celular": True,
              "somente_matriz": False,
              "somente_filial": False,
            },
          "page": 1
    })
    
    self.headers.update({ "Content-Type": "application/json" })
    response = self.session.post("https://api.casadosdados.com.br/v2/public/cnpj/search", json=payload)

    responseParsed = json.loads(response.text)
    return responseParsed["data"]["cnpj"]

  def getEnterpise(self, socialReason: str, cnpj: str):
    socialReasonFormated = socialReason.lower().replace(" ", "-").replace(".", "").replace("&", "and") + f"-{cnpj}"
    
    response = self.session.get(f"https://casadosdados.com.br/solucao/cnpj/{socialReasonFormated}")
    responseParsedHtml = html.fromstring(response.text)

    lastUpdated = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[1]/p')[0].text_content()
    mail = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[19]/p/a')[0].text_content().lower()
    
    number = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[20]/p')
    numberParsed = [element.text_content() for element in number]
    numberFormated = []

    for _, text in enumerate(numberParsed, 1):
      numberFormated.append(text.replace("Whatsapp", "").replace(" ", "").replace("\u00a0", ""))

    return json.dumps({ 
      "lastUpdated": lastUpdated, 
      "mail": mail,
      "number": numberFormated
    })