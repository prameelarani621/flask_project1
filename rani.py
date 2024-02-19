from flask import Flask

FAI=Flask(__name__)

@FAI.route('/srtingresponse')
def srtingresponse():
    return 'hai this is our first view of flask'

@FAI.route('/secondsrtingresponse')
def secondsrtingresponse():
    return 'hai this is our second view of flask'


if __name__=='__main__':
    FAI.run(debug=True)