from flask import Flask, render_template

app = Flask(__name__, 
    static_url_path='',
    static_folder='style',  
    template_folder='templates'
)
app.secret_key = '1KMsm112KMI8Fd45v8ben3333jkcV8878'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/lab1/')
def lab1():
    return render_template('Lab1_mylian/lab1.html')

@app.route('/templates/Lab1_mylian/html/<filename>')
def lab1_examples(filename):
    return render_template(f'Lab1_mylian/html/{filename}')

@app.route('/templates/Lab1_mylian/lab1.html')
def lab1_main():
    return render_template('Lab1_mylian/lab1.html')

@app.route('/templates/Lab2_mylian/lab2.html')
def lab2_main():
    return render_template('Lab2_mylian/lab2.html')

@app.route('/templates/Lab3_mylian/lab3.html')
def lab3_main():
    return render_template('Lab3_mylian/lab3.html')

@app.route('/templates/Lab4_mylian/lab4.html')
def lab4_main():
    return render_template('Lab4_mylian/lab4.html')

@app.route('/templates/Lab4_mylian/<filename>')
def lab4_files(filename):
    return render_template(f'Lab4_mylian/{filename}')

@app.route('/templates/Lab5_mylian/lab5.html')
def lab5_main():
    return render_template('Lab5_mylian/lab5.html')

@app.route('/templates/Lab6_mylian/lab6.html')
def lab6_main():
    return render_template('Lab6_mylian/lab6.html')

@app.route('/templates/Lab7_mylian/lab7.html')
def lab7_main():
    return render_template('Lab7_mylian/lab7.html')

@app.route('/templates/Lab8_mylian/lab8.html')
def lab8_main():
    return render_template('Lab8_mylian/lab8.html')


if __name__ == '__main__':
    app.run(debug=True)  
