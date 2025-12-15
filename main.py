from app import app
import os

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) #Heroku