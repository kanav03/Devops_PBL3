from flask import Flask, render_template_string

app = Flask(__name__)

# Updated HTML template with a more polished and professional UI
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Deployment Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            color: #E0E0E0;
            margin: 0;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            
            /* Animated Gradient Background */
            background: linear-gradient(-45deg, #0D1B2A, #1B263B, #415A77, #778DA9);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .glass-card {
            /* Glassmorphism Effect */
            background: rgba(27, 38, 59, 0.6);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            
            padding: 2.5rem;
            text-align: center;
            max-width: 550px;
            width: 90%;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            animation: fadeIn 1s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .card-title {
            font-weight: 700;
            font-size: 2.25rem;
            color: #FFFFFF;
            margin-bottom: 0.75rem;
        }

        .card-subtitle {
            font-weight: 400;
            font-size: 1.1rem;
            color: #A9B4C2;
            margin-bottom: 2rem;
        }
        
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background-color: rgba(34, 197, 94, 0.2);
            color: #22C55E;
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            font-weight: 600;
            margin-bottom: 2.5rem;
            border: 1px solid rgba(34, 197, 94, 0.5);
        }
        
        .status-badge .dot {
            width: 8px;
            height: 8px;
            background-color: #22C55E;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(34, 197, 94, 0); }
            100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
        }

        .footer {
            position: absolute;
            bottom: 10px;
            font-size: 0.8rem;
            opacity: 0.6;
        }
    </style>
</head>
<body>
    <div class="glass-card">
        <div class="status-badge">
            <div class="dot"></div>
            <span>Deployment Successful</span>
        </div>
        <h1 class="card-title">CI/CD Pipeline Activated</h1>
        <p class="card-subtitle">
            This application was automatically built and deployed to Kubernetes using a Jenkins pipeline.
        </p>
    </div>

    <div class="footer">
        Kanav Nijhawan | DevOps Project
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
