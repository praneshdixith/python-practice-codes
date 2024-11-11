from flask import Flask, jsonify, request 

app = Flask(__name__)

@app.route('/', method = ['GET','POST'])
def home():
    if(request.methos == 'GET'):
        data = "hello world"
        return jsonify({'data': data}) 
    
if __name__ == '__main__':
    app.run(debug = True)