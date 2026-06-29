# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)
CORS(app)

chave = os.getenv("GOOGLE_API_KEY")
cliente = genai.Client(api_key=chave)

historico = []

system_prompt = """
És um assistente de suporte ao cliente da TechNova, uma loja portuguesa de tecnologia.

SOBRE A LOJA:
- Produtos: telemóveis, computadores, tablets, acessórios e smart home
- Devoluções: aceites até 30 dias, produto em estado original, reembolso em 5-7 dias úteis
- Entregas: standard 3-5 dias úteis (grátis acima de 50€), expresso 24h por 4,99€
- Garantia: 2 anos em todos os produtos, avarias resolvidas em 48h
- Pagamentos: cartão, MB Way, Multibanco, PayPal, prestações acima de 150€
- Horário de suporte humano: segunda a sexta, 9h-18h
- Localização: Porto, entregas para todo o território nacional

REGRAS:
- Responde sempre em português europeu
- Sê simpático, profissional e conciso
- Se não souberes responder, diz honestamente e oferece escalar para humano
- Se o cliente pedir para falar com humano, escreve [ESCALAR] no fim da resposta
"""

@app.route("/chat", methods=["POST"])
def chat():
    dados = request.json
    mensagem = dados["mensagem"]

    historico.append(
        types.Content(role="user", parts=[types.Part(text=mensagem)])
    )

    resposta = cliente.models.generate_content(
        model="gemini-3.5-flash",
        contents=historico,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt
        )
    )

    texto = resposta.candidates[0].content.parts[0].text

    historico.append(
        types.Content(role="model", parts=[types.Part(text=texto)])
    )

    escalar = "[ESCALAR]" in texto
    texto_limpo = texto.replace("[ESCALAR]", "").strip()

    return jsonify({
        "resposta": texto_limpo,
        "escalar": escalar
    })

if __name__ == "__main__":
    app.run(debug=True)