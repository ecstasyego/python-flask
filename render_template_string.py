from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head><title>TITLE</title></head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """
    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
