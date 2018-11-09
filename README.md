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
file:///ltcfp_server/tests/ocr-alfabeto.gif
file:///ltcfp_server/tests/teste-ocr.png
file:///ltcfp_server/tests/RG.png
```

Saida esperada para o test-amil:
```
A saída bruta do LTCFP sem processamento é:
-----------------BEGIN-----------------
b'This is a lot of 12 point text to test the\nocr code and see if it works on all types\nof file format.\n\nThe quick brown dog jumped over the\nlazy fox. The quick brown dog jumped\nover the lazy fox. The quick brown dog\njumped over the lazy fox. The quick\nbrown dog jumped over the lazy fox.'
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