from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/directory_fuzzing/secret_endpoint/')
def directory_fuzzing():
    return "You found the secret endpoint for directory fuzzing!"

@app.route('/page_fuzzing/secret_page.html')
def page_fuzzing():
    return "You found the secret page for page fuzzing!"

@app.route('/recursive_fuzzing/level1/level2/secret')
def recursive_fuzzing():
    return "You found the secret endpoint for recursive fuzzing!"

@app.route('/parameter_fuzzing/')
def parameter_fuzzing():
    secret = request.args.get('secret_param', None)
    if secret == 'secret_value':
        return "You found the secret parameter with the correct value!"
    return "Try fuzzing the parameters!"

@app.route('/value_fuzzing', methods=['POST'])
def value_fuzzing():
    if request.form.get('key') == 'secret_value':
        return "You fuzzed the correct POST value!"
    return "Try fuzzing POST values!"

# Sub-domain Fuzzing, Vhost Fuzzing, and others would require additional configurations
# outside of this Flask app.

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
