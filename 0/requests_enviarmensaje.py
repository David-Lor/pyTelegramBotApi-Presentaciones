import requests

TOKEN = ""

url = "https://api.telegram.org/bot{token}/{method}"
method = "sendMessage?chat_id={chatid}&text={text}"

def send_message(chatid, text):
	r = requests.get(url.format(
		token=TOKEN,
		method=method.format(
			chatid=chatid,
			text=text
		)
	))
	return r
