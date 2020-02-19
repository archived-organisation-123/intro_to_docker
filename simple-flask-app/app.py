from flask import Flask

count = 0
app = Flask(__name__)

@app.route("/")
def counter():
    # Just a toy example, never do this in real code
    global count
    count += 1
    return f"I've been loaded {count} times!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
