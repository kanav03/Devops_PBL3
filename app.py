from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with Bootstrap for better UI
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Jenkins CI/CD Pipeline Demo</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(to right, #667eea, #764ba2);
            color: #fff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .container {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .card {
            background: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            padding: 30px;
            text-align: center;
            max-width: 500px;
            animation: fadeIn 1.5s ease-in-out;
        }
        h1 {
            margin-bottom: 20px;
        }
        @keyframes fadeIn {
            0% {opacity: 0; transform: translateY(-20px);}
            100% {opacity: 1; transform: translateY(0);}
        }
        .btn-custom {
            background-color: #ff6a00;
            border: none;
            color: white;
        }
        .btn-custom:hover {
            background-color: #ff9e43;
        }
        .footer {
            text-align: center;
            padding: 10px;
            font-size: 0.9rem;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card shadow-lg">
            <h1>🚀 Jenkins CI/CD Demo</h1>
            <p>Your Flask app is successfully deployed on Kubernetes!</p>
            <a href="#" class="btn btn-custom mt-3">View Pipeline</a>
        </div>
    </div>
    <div class="footer">
        Flask + Jenkins + Kubernetes Demo
    </div>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
