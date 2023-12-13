import logging
from flask import Flask, request, jsonify
from handler import ocr_handler, cap_handler


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


app = Flask(__name__)


@app.route('/ocr', methods=['POST'])
def respond():
    if request.method == 'POST':
        logger.info('[OCR]\treceived request...')
        if request.files:
            image = request.files['image'].read()
            lang = request.form.get('lang', 'ch')
            logger.info(f'[OCR]\tprocessing...')
            result, status = ocr_handler(image, lang)
            logger.info('[OCR]\tresponding...')
            return jsonify({'result': result}), status
        else:
            return jsonify({'error': 'No image received.'}), 404


@app.route('/cap', methods=['POST'])
def respond():
    if request.method == 'POST':
        logger.info('[CAP]\treceived request...')
        if request.files:
            image = request.files['image'].read()
            model = request.form.get('model', 'blip')
            logger.info(f'[CAP]\tprocessing...')
            result, status = cap_handler(image, model)
            logger.info('[CAP]\tresponding...')
            return jsonify({'result': result}), status
        else:
            return jsonify({'error': 'No image received.'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=14500, debug=False)
