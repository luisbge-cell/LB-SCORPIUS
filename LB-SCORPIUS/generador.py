import os

# Definir estructura
folders = ['api', 'public']
files = {
    'api/index.py': """from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        user_msg = request.json.get('message')
        prompt = f"Actúa como LB-SCORPIUS, una IA mentor humanizada de Escorpio. Reglas: Seguridad de datos, parafraseo y expertiz técnica. Usuario dice: {user_msg}"
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
""",
    'public/index.html': """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>LB-SCORPIUS HUD</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="scorpio-hud">
        <header>
            <div class="brand">LB-SCORPIUS</div>
            <div class="status">🛡️ MODO_SEGURO_ACTIVO</div>
        </header>
        <div id="chat-window"></div>
        <div class="input-area">
            <input type="text" id="user-input" placeholder="Iniciando secuencia de comando...">
            <button onclick="sendMessage()">ENVIAR</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
""",
    'public/style.css': """body { background: #050505; color: #fff; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
#scorpio-hud { width: 90%; max-width: 800px; background: #000; border: 1px solid #ff0000; box-shadow: 0 0 30px rgba(255, 0, 0, 0.2); padding: 30px; border-radius: 5px; }
header { display: flex; justify-content: space-between; border-bottom: 1px solid #222; padding-bottom: 15px; margin-bottom: 20px; }
.brand { color: #ff0000; font-weight: bold; letter-spacing: 3px; font-size: 20px; }
.status { color: #555; font-size: 12px; }
#chat-window { height: 400px; overflow-y: auto; padding: 10px; border-bottom: 1px solid #222; }
.input-area { display: flex; gap: 10px; margin-top: 20px; }
input { flex-grow: 1; background: #0a0a0a; border: 1px solid #333; color: #fff; padding: 12px; border-radius: 4px; }
button { background: #ff0000; color: #fff; border: none; padding: 10px 25px; cursor: pointer; font-weight: bold; }
button:hover { background: #b30000; }
""",
    'public/script.js': """async function sendMessage() {
    const input = document.getElementById('user-input');
    const chat = document.getElementById('chat-window');
    const msg = input.value;
    if(!msg) return;

    chat.innerHTML += `<p style="color:#888"><strong>Tú:</strong> ${msg}</p>`;
    input.value = '';

    const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message: msg })
    });
    const data = await response.json();
    chat.innerHTML += `<p style="color:#ff3131"><strong>SCORPIUS:</strong> ${data.response}</p>`;
    chat.scrollTop = chat.scrollHeight;
}
""",
    'requirements.txt': "flask\\ngoogle-generativeai\\nflask-cors",
    'vercel.json': """{
  "rewrites": [{ "source": "/api/(.*)", "destination": "/api/index.py" }]
}"""
}

# Crear carpetas
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Crear archivos
for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("✅ SISTEMA LB-SCORPIUS GENERADO CON ÉXITO.")
print("Ahora puedes subir esta carpeta a tu GitHub.")