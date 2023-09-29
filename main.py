from flask import Flask, render_template, request, make_response, jsonify, Response
import logic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/integrate', methods=['POST'])
def solve_equation():
    try:
        return jsonify(logic.integrate(request.get_json()))
    except Exception as ex:
        return make_response(str(ex), 400)


if __name__ == '__main__':
    app.run(debug=True)