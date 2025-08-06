from flask import Flask, request
import requests

app = Flask(__name__)

# IP/port of your local machine (must be accessible or use ngrok)
LOCAL_COMPUTER_URL = "http://your-local-ip:5001/receive"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    print("\n✅ Received TradingView Alert:")
    print(data)

    # Forward it to your local Python script
    try:
        response = requests.post(LOCAL_COMPUTER_URL, json=data)
        print("➡️ Forwarded to local computer:", response.status_code)
    except Exception as e:
        print("❌ Failed to forward:", e)

    return {"status": "received"}, 200

if __name__ == "__main__":
    app.run()
