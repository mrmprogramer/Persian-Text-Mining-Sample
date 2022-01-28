from typing import List
from flask import Flask
from flask_cors import CORS
from flask import request
import webbrowser
import os
import json
from queryhandeler import responsequery

class api():
    app = Flask(__name__)
    CORS(app)
    def __init__(self):
        self.name='api'

    def run(self):
        webbrowser.open('file://' + os.path.realpath('index.html'))
        self.app.run()

    
    @app.route("/Search", methods=['GET', 'POST'])
    # @cross_origin()
    def Search():
        query = request.args.get('query')
        return json.dumps(responsequery(query), ensure_ascii=False)







if __name__ == "__main__":
    api().run()