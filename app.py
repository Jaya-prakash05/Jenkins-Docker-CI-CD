from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>My DevOps Project</title>
    </head>
    <body style="text-align:center; margin-top:100px;
                 font-family:Arial; background:#eef2ff;">

        <h1>Welcome to My DevOps Project!</h1>

        <h2>Automated CI/CD Pipeline</h2>

        <p>Deployed using Jenkins, Docker and AWS EC2.</p>

        <p>Application Version: 1.0</p>

    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
