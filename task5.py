"""
Creator: Krylova Elizaveta
"""

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def homepage():
    """This function"""
    return """
        <style type="text/css">
        .styletest {
        color: #8B0000; 
        font-size: 20px; 
        font-family: Constantia;
        style: font-weight:bold;
        line-height: 3px;
        }
        </style>
        <img src="https://sun9-69.userapi.com/c834302/v834302264/17cfa8/i5ANGXyfJ3c.jpg" alt="Лизя" height=250px width=200px>
        <p><font class="styletest"> К Р Ы Л О В А </font></p>
        <p><font class="styletest"> Елизавета Сергеевна </font></p>
        <p> Python разработчик </p>
        <p> тел.: 8(900)-987-87-97 </p>
        <p> Начинающий python разработчик </p>
        <p> OOO "ЛИЗЯ" <p>
        """

APP.run(port=8080, debug=True)
