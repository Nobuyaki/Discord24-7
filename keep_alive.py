from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    	return "DISCORD 24/7 READY\nHost In Uptimerobot.com"

def run():
    	app.run(host="0.0.0.0", port=8080)

def keep_alive():
    	server = Thread(target=run)
    	server.start()
