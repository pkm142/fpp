from flask import Flask, jsonify
import json

app = Flask(__name__)


news_json_file_path = 'news.json'
with open(news_json_file_path, 'r', encoding='utf-8') as json_file:
    news_data = json.load(json_file)

scheme_json_file_path = "scheme.json"
with open(scheme_json_file_path, 'r', encoding='utf-8') as json_file:
    scheme_data = json.load(json_file)


@app.route('/api/news_data', methods=['GET'])
def get_news_data():
    return jsonify(news_data)

@app.route('/api/scheme_data', methods=['GET'])
def get_scheme_data():
    return jsonify(scheme_data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
