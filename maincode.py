#wechat log in
from wxpy import *
from wechat_sender import *
bot = Bot()

#回复my_friend发送的消息
my_friend = bot.friends().search(u'your friend name')
@bot.register(my_friend)
def reply_message(msg):
    message = msg.text
    return response(message)
	
# Define respond()
def respond(message):
    params = {}
    entities = interpreter.parse(message)["entities"]
    intent = interpreter.parse(message)["intent"]
    intent = intent["name"]
    if entities == []:
        return intent
    else:
        for ent in entities:
            params[ent["entity"]] = str(ent["value"])
        org = params["organization"]
        return intent,org
		
## functional fun
from iexfinance import Stock
def getopen(org):
    return (org.get_open())
def getclose(org):
    return (org.get_close())
def gethigh(org):
    return (org.get_previous()['high'])
def getlow(org):
    return (org.get_previous()['low'])
def getvolume(org):
    return (org.get_volume())
def getprice(org):
    return (org.get_price())
def getchangepercent(org):
    return (org.get_previous()['changePercent'])

#policy	
from iexfinance import Stock
def policy(message):
    intent = respond(message)[0]
    org = respond(message)[1]
    org = Stock(org)
    if intent == "opening price":
        return  getopen(org)
    if intent == "closing price":
        return  getclose(org)
    if intent == 'high price':
        return  gethigh(org)
    if intent == "low price":
        return  getlow(org)
    if intent == "volume":
        return  getvolume(org)
    if intent == "price": 
        return  getprice(org)
    if intent == "change percent":
        return  getchangepercent(org)

#response
def response(message):
    intent = respond(message)[0]
    data = policy(message)
    a = len(intent)
    if intent == "g":
        return "Wish u a happy day:)"
    if a!=1 :
        org = respond(message)[1]
        if intent == "volume":
            return "The {} of {} is {}".format(intent,org,data)
        if intent == "change percent":
            return "The {} of {} is {}%".format(intent,org,data)
        else:
            return "The {} of {} is ${}".format(intent,org,data)
    else:
        return "You can ask me other question:)"
		
	