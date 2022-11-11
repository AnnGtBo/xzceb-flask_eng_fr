from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """
    This function translate eng to french using ibm cloud dictinary
    """
    textToTranslate = request.args.get('textToTranslate')

    return translator.englishToFrench(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    This function translate french to eng using ibm cloud dictinary
    """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.frenchToEnglish(textToTranslate)

@app.route("/")
def renderIndexPage():
    """
    create defoult page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
