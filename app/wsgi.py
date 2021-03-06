""" hello.py """

from flask import Flask, jsonify

application = Flask(__name__)

@application.route('/')
def hello():
    return jsonify({
        'hello': 'world'
    })

if __name__ == '__main__':
    application.run(host='0.0.0.0')
