import json
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    textToTranslate = request.args.get('textToTranslate')
    frenchTranslation = translator.english_to_french(textToTranslate)
    return frenchTranslation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    textToTranslate = request.args.get('textToTranslate')
    englishTranslation = translator.french_to_english(textToTranslate)
    return englishTranslation
    
@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
