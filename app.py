from flask import Flask, render_template, request, jsonify
from web_chalaa import execute


app = Flask(__name__)

@app.route('/')
def home():
    return(render_template('index.html'))

@app.route('/run_script', methods=['POST'])
def run_script():
    code = request.form['code']
    try:
        result = execute(code)  # Replace with your actual function
        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)