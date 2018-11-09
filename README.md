## Python LTCFP OCR - com Docker

Este branch tem como base o tutorial 
[RealPython Tutorial](https://realpython.com/blog/python/setting-up-a-simple-ocr-server/).

O resultado é um aplicativo simples faz OCR podendo ser executado em container Docker usando o Tesseract.

* cli.py - um aplicativo python em linha de comando que utiliza uma URL e retorna o texto extraído da imagem. ;)
* app.py - um pequeno aplicativo python com Flask que faz a mesma coisa, mas no navegador. =)


### Utilizamos:
* Python3 & unicode.
* tesseractshadow/tesseract4re Docker container.
* pode ser efetuadas chamadas com file:/// URLs. (Relativa ao container!_)

### Alternatives
* [tesseract-ocr-re](https://github.com/tesseract-shadow/tesseract-ocr-re)
* [tleyden/open-ocr](https://github.com/tleyden/open-ocr) Full-featured queued service. Written in Go.

### Como utilizar
Install Docker

Instale o docker [Docker - Get Started.](https://docs.docker.com/get-started/).

#### Start: CLI
Executando o aplicativo cli na Docker container.

```
docker container run --publish 80:5000 --interactive --tty flask-ltcfp-ocr python3 cli.py
```

Aparecerá:
```
.##.......########..######..########.########.......#######...######..########.
.##..........##....##....##.##.......##.....##.....##.....##.##....##.##.....##
.##..........##....##.......##.......##.....##.....##.....##.##.......##.....##
.##..........##....##.......######...########......##.....##.##.......########.
.##..........##....##.......##.......##............##.....##.##.......##...##..
.##..........##....##....##.##.......##........###.##.....##.##....##.##....##.
.########....##.....######..##.......##........###..#######...######..##.....##

Um Simples OCR
Informe a URL da imagem que você quer analisar:
```

Tente utilizar algumas das seguintes opções de endereço:
```
file:///ltcfp_server/tests/619121.jpg
file:///ltcfp_server/tests/1234567890.jpg
file:///ltcfp_server/tests/alfabeto-1.jpg
file:///ltcfp_server/tests/alfabeto-2.jpg
file:///ltcfp_server/tests/alfabeto-3.jpg
file:///ltcfp_server/tests/test-amil.png
file:///ltcfp_server/tests/RG.png
```

Saida esperada para o test-amil:
```
A saída bruta do LTCFP sem processamento é:
-----------------BEGIN-----------------
b'e 1\nam i [ Solicitag\xc3\xa9o de Reembolso de Despesa M\xc3\xa9dico-Hospitalar (CLIENTE)\n\nNGmero do Protocolo: 32630520181107068309\n\nBANCO SAFRA S/A\n\n077817000\n\n963942026 - ALINE DE MOURA TERRA\n\n063892928 - BENJAMIN SILVA TERRA\n\nBLUE 600 PLUS NAC QP PUCE Valor Apresentada: RS 300,00\nQtde de Recibos: 2 Valor Reaembolsado: R$ 0,00\nLecalCadastramento: Reemboiso Modalidads de Reembolso / Data Provavel Pgto.:\nData Solicttacg&o: 07/21/2018 Consultas - 22/21/2018\nTelefona da Contato:\nOpcSes de Receblmento: Dap\xc3\xa9sito / Tronsfer\xc3\xa9ncia\nFavorecido: 963942026 -ALINE DE MOURA TERRA\nBanca: BANCO ITAU S.A,\nAgancla: 7056\nObservacde:\n\nDeclaramos para cs devidos efeitos fiscals que o associado nos entregou nesta dota os recibos e comprovantes de pagamentos referentes\n\xc3\xa9s despesas discriminadas que serdo reembotsados de acorde com as condicgbtes estabelecidas em seu contrato,\n\nge\nDeta, Assinatura @ Corimbo do Agante de Atendimento\n\n \n\nese SNCTceecencescsvonssreneanerssreeevenreceseseecsssessiosecepspuppsttssoeseeseosossesecec\n\n \n\neee ees\n\n \n\n \n\n \n\n \n\nhsb eerees nee,\n\n \n\nam i Solicitacdo de Reembolso de Despesa M\xc3\xa9dico-Hospitalar (CREEMB)\n\nNGmero do Protecolo: 32630520181107068309\n\nBANCO SAFRAS/A\n077817000\n963942024 - ALINE DE MOURA TERRA\nBenefici\xc3\xa9ric: 963892926 - BENJAMIN SILVA TERRA\nPlane: BLUE 600 PLUS NAC QP PICE Valor Apresentado: R$ 300,00\nGtde de Recibos: 2 Valor Reembotsado: R$ 0,00\nLocal Cadastramento: Reembolso Modalidade de Reambolso / Data Prov\xc3\xa9vel Pgto.:\nData Solicitagdo: 07/13/2018 Consuitas ~ 22/11/2018\nTelefone de Contato:\n\nOpcdes de Recebimente: Dep\xc3\xa9dsito / Transfer\xc3\xa9ncia\nFavorecide: 963942026 ~ ALINE DE MOURA TERRA\nBanco:BANCC ITAU S.A.\n\nAg\xc3\xa9ncia: 7056\n\nObservacdo:'
------------------END------------------
```

#### Start: Web App
Runs another app from the same container, pulled from DockerHub:
```
docker container run -d --name flask-ltcfp-ocr-web -p 80:5000 flask-ltcfp-ocr
```
Abra um navegador no seguinte endereço `http://localhost` e utilize qualquer das seguintes opções ou caso o seu container tenha acesso a internet pode incluir um endereço web.
Exemplo: `file:///ltcfp_server/tests/advertisement.jpg`  e clique em enviar para efetuar uma nova analise clique no link Novo Envio 

```

#### Fazer a imagem Docker:
execute:
```docker image build --tag flask-ltcfp-ocr .```

:)