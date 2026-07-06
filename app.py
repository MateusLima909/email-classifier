from flask import Flask, render_template, request, flash
from config import Config
from services.extraction import extract_text
from services.ai_analysis import analyze_email_pro

Config.validate()

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config['MAX_CONTENT_LENGTH'] = Config.MAX_CONTENT_LENGTH

@app.route("/", methods=["GET", "POST"])
def index():
    context = {"classification": None, "suggestion": None, "email_text": "", "confidence": None}

    if request.method == "POST":
        email_text = request.form.get("email_text", "")
        email_file = request.files.get("email_file")

        file_content = extract_text(email_file)
        if file_content:
            email_text = file_content

        context["email_text"] = email_text

        if email_text.strip():
            analysis = analyze_email_pro(email_text)
            if analysis:
                context.update(analysis)
            else:
                flash("Houve um erro na análise inteligente. Tente novamente.")

    return render_template("index.html", **context)

@app.errorhandler(413)
def file_too_large(e):
    flash("Arquivo muito grande. Máximo de 2MB.")
    return render_template("index.html", classification=None, suggestion=None, email_text="", confidence=None), 413

if __name__ == "__main__":
    app.run(debug=True)