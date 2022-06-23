from audioop import cross
from app import app , bot
from flask import request , make_response , url_for , render_template
from flask_cors.decorator import  cross_origin
from flask_cors.extension import  CORS


@app.route('/')
@cross_origin()
def index():
    return render_template('/public/template/index.html')


@app.route('/chatbot' , methods =['POST'])
@cross_origin()
def chat():
    jsony = request.json
    data = jsony['msg']
    print(data)
    return str(bot.get_response(data))

@app.route("/sentiment_analysis")
def about():
    return render_template('public/template/sentiment_analysis.html')