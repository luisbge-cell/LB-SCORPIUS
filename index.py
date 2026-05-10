from flask import Flask, request, jsonify
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
