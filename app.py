from flask import Flask, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

# Número do WhatsApp de destino (sem espaços, com DDI +55)
WHATSAPP_NUMBER = "5521975681798"

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form["nome"]
    apelido = request.form["apelido"]
    idade = request.form["idade"]
    faixa = request.form["faixa"]
    peso = request.form["peso"]
    equipe = request.form["equipe"]
    professor = request.form["professor"]

    mensagem = f"""
📋 *Inscrição Guerra das Faixas – 2ª Edição*

👤 Nome: {nome}
🏷️ Apelido: {apelido}
🎂 Idade: {idade}
🥋 Faixa: {faixa}
⚖️ Peso: {peso}
🤝 Equipe: {equipe}
📚 Professor: {professor}

⚠️ *Comprovante e foto devem ser enviados em anexo!*
    """

    mensagem_encoded = urllib.parse.quote(mensagem)
    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={mensagem_encoded}"

    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
