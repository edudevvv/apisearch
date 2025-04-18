import json 

from lxml import html
from tls_client import Session
from utils.replacePayload import replacePayload

class enterpiseService:
  def __init__(self):
    self.session = Session(random_tls_extension_order=True, client_identifier="chrome_130")
    self.headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" }

  def getListEnterprises(self, payload):
    self.headers.update({ "Content-Type": "application/json" })
    payloadReplaced = replacePayload(payload)

    response = self.session.post("https://api.casadosdados.com.br/v2/public/cnpj/search", json=payloadReplaced)
    responseParsed = json.loads(response.text)
    if responseParsed["success"] == True:
      return { "list": responseParsed["data"]["cnpj"], "count": responseParsed["data"]["count"] }
    else: 
      return { "list": [], "count": 0 }

  def getEnterpise(self, socialReason: str, cnpj: str):
    socialReasonFormated = socialReason.lower().replace(" ", "-").replace(".", "").replace("&", "and") + f"-{cnpj}"
    
    response = self.session.get(f"https://casadosdados.com.br/solucao/cnpj/{socialReasonFormated}")
    responseParsedHtml = html.fromstring(response.text)
    print(response.status_code)
    lastUpdated = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[1]/p')
    if lastUpdated: 
      lastUpdated = lastUpdated[0].text_content()

    mail = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[19]/p/a')
    if mail:
      mail = mail[0].text_content().lower()
    
    typeM = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[7]/p')
    if typeM: 
      typeM = typeM[0].text_content().lower()

    shareCapital = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[10]/p')
    if shareCapital:
      shareCapital = shareCapital[0].text_content().lower()
      
    number = responseParsedHtml.xpath('//*[@id="__nuxt"]/div/section[4]/div[2]/div[1]/div/div[20]/p')
    numberFormated = []

    if number:
      numberParsed = [element.text_content() for element in number]

      for _, text in enumerate(numberParsed, 1):
        numberFormated.append(text.replace("Whatsapp", "").replace(" ", "").replace("\u00a0", ""))

    return json.dumps({ 
      "lastUpdated": lastUpdated, 
      "informations": {
        "type": typeM,
        "shareCapital": shareCapital,
        "address": {}
      },
      "mail": mail,
      "number": numberFormated
    })