from utils.mailService import mailService

mailInstance = mailService(domain="gmail.com")
mailConnection = mailInstance.connect(user="assessoriaquantumseg@gmail.com", password="edwwkvtxfewlfrfu")

if mailConnection:
  sendInfo = mailInstance.sendMail(clientName="Quantum Assessoria", clientMail="eduardosilvamoraes23@gmail.com", subject="testando", body=f"""<p>Prezados, bom dia!</p>
        <p>Meu nome é Ana e escrevo em nome da empresa Quantum Assessoria. Somos especializados em Segurança do Trabalho e oferecemos diversos serviços relacionados a documentação, assessoria e treinamentos na área.</p>
        <p>Abaixo anexo uma pequena apresentação dos nossos serviços. Caso tenham interesse, podemos agendar uma reunião para conversarmos melhor.</p>
        <p>Estamos à disposição e ficamos no aguardo do interesse de vocês.</p>
        <p>Atenciosamente, <br/><strong>Ana Julia Moraes</strong><br/><strong>Representante Comercial</strong><br/><strong>(11) 97481-7269</strong></p><br/><img src="https://media.discordapp.net/attachments/1196685131725942914/1204970486556262440/Capture.png?ex=65d6ab37&is=65c43637&hm=a534b01a1f68f1e69ec49cd38697f9d221d620a1a9cb8dfb25f457d686a5bf79&=&format=webp&quality=lossless" style="width: 130px;" />""")
  
  print(sendInfo)