from flask import Flask,request,render_template


app = Flask(__name__, static_url_path='/PI-Flask/statics')
# app = Flask(__name__)

#ruta principal
@app.route('/')
def index():
    return render_template('Login.html')

#Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('Report.html')

#Datos Curiosos 
@app.route('/datoscuriosos')
def datoscuriosos():
    return render_template('DatosCuriosos.html')

#pre test
@app.route('/pretest')
def pretest():
    return render_template('Pretest.html')

#Reporte
@app.route('/reporte')
def reporte():
    return render_template('Reporte.html')

#signup
@app.route('/signup')
def signup():
    return render_template('Signup.html')

#test
@app.route('/test')
def test():
    return render_template('Test.html')

#Ruta erronea
@app.errorhandler(404)
def paginano(e):
    return 'Revisa tu sintaxis: PAGINA NO ENCONTRADA'

if __name__ == '__main__':
    app.run(port =4000,debug=True)
