from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    # Capturamos los valores numéricos del formulario
    transporte = float(request.form['transporte'])
    energia = float(request.form['energia'])
    consumo = float(request.form['consumo'])

    # Cálculo base más realista (en toneladas de CO₂/año)
    # transportes y consumos más altos generan más impacto
    resultado = round((transporte * 1.8 + energia * 1.2 + consumo * 0.9) / 3, 2)

    # Determinamos una comparación ecológica
    if resultado < 1:
        equivalencia = "equivale a plantar 10 árboles 🌱"
        mensaje = "Excelente, tu huella es muy baja. ¡Sigue así!"
        color = "verde"
    elif resultado < 3:
        equivalencia = "equivale a la contaminación de un viaje de 1500 km 🚗"
        mensaje = "Tienes una huella media"
        color = "amarillo"
    elif resultado < 6:
        equivalencia = "equivale a la contaminación de 10 vuelos en avión ✈️"
        mensaje = "Tu huella es alta"
        color = "rojo"
    else:
        equivalencia = "equivale a la contaminación de 20 vuelos en avión ✈️"
        mensaje = "¡Alerta! Tu impacto ambiental es muy elevado."
        color = "rojo"

    return render_template(
        'resultado.html',
        resultado=resultado,
        equivalencia=equivalencia,
        mensaje=mensaje,
        color=color
    )


if __name__ == '__main__':
    app.run(debug=True)
