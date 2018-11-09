# -*- coding: utf-8 -*-

import os
import logging
from logging import Formatter, FileHandler
from flask import Flask, request, jsonify, render_template
import json

from ocr import process_image

app = Flask(__name__)
_VERSION = 1  # API version


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/v{}/ocr'.format(_VERSION), methods=["POST"])
def ocr():

    # Read the URL
    try:
        url = request.get_json()['image_url']
    except TypeError:
        print("Erro ao efetuar conversão get_json(). Tentando carregar como scring.")
        try:
            data = json.loads(request.data.decode('utf-8'), encoding='utf-8')
            url = data['img_url']
        except:
            return jsonify(
                {"error": "Não foi possível obter a propriedade 'image_url'.",
                 "data": request.data}
            )
    except:
        return jsonify(
            {"error": "Tipo errado tente fazer a requisição JSON assim: {'image_url': 'http://.....'}",
             "data": request.data }
        )

    # Process the image
    print("URL:", url)
    try:
        output = process_image(url,"por")
    except OSError:
        return jsonify({"error": "OOPPSS não encontrei uma imagem na URL.",
                        "url": url})
    except:
        return jsonify(
            {"error": "Não entendi este tipo de imagem.",
             "request": request.data}
        )
    app.logger.info(output)
    return jsonify({"output": output})


@app.errorhandler(500)
def internal_error(error):
    print("*** 500 ***\n{}".format(str(error)))  # ghetto logging


@app.errorhandler(404)
def not_found_error(error):
    print("*** 404 ***\n{}".format(str(error)))

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: \
            %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Iniciando app.py on port: {port}")
    app.run(host='0.0.0.0', port=port)
