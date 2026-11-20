
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My DevOps Project</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .container {
                background: white;
                padding: 50px;
                border-radius: 20px;
                text-align: center;
                width: 90%;
                max-width: 600px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }

            h1 {
                color: #333;
                font-size: 32px;
                margin-bottom: 20px;
            }

            h2 {
                color: #667eea;
                margin-bottom: 20px;
            }

            p {
                color: #666;
                font-size: 16px;
                margin: 15px 0;
            }

            .version {
                display: inline-block;
                background: #e0e7ff;
                color: #4338ca;
                padding: 10px 20px;
                border-radius: 20px;
                font-weight: bold;
                margin-top: 15px;
            }

            .status {
                color: #16a34a;
                font-weight: bold;
                margin-top: 20px;
            }

            .button {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 25px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: 0.3s;
            }

            .button:hover {
                background: #4f46e5;
                transform: scale(1.05);
            }

            @media (max-width: 500px) {
                .container {
                    padding: 30px 20px;
                }

                h1 {
                    font-size: 25px;
                }
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>Welcome to My DevOps Project!</h1>

            <h2>Automated CI/CD Pipeline</h2>

            <p>
                Successfully deployed using
                <b>Jenkins, Docker and AWS EC2.</b>
            </p>

            <div class="version">
                Application Version: 1.0
            </div>

            <p class="status">
                ● Application Status: Running
            </p>

            <a href="/health" class="button">
                Check Application Health
            </a>

        </div>

    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
