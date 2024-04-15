from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.get("/")
def get_root():
    return {
        "endpoints": {
            "/static": "GET",
            "/server/<int:count>": "GET",
            "/client": "GET"
        }
            
    }

@app.get("/static")
def get_static():
    return send_file("static.html")

@app.get("/server/<int:count>")
def get_server(count):
    if count >= 30:
        return "count < 30 please"
    return render_template("server.html", count=count)

@app.get("/client")
def get_client():
    return send_file("client.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080)