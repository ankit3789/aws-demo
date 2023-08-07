from flask import Flask

app = Flask('__name__')

@app.route('/', methods=['POST', 'GET'])
def index():
    return "demo-repo check aws!"

app.run(host='0.0.0.0', port=80)