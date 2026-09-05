from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios para el login
USUARIOS = {
    "admin": "1234"
}

# Página de inicio
@app.route("/")
def inicio():
    return render_template("inicio.html")

# Inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")

        if usuario in USUARIOS and USUARIOS[usuario] == contrasena:

            return render_template(
                "login_resultado.html",
                exito=True,
                usuario=usuario
            )

        else:

            return render_template(
                "login_resultado.html",
                exito=False
            )

    return render_template("login.html")

# Registro de clientes
@app.route("/clientes", methods=["GET", "POST"])
def clientes():

    if request.method == "POST":

        nombre = request.form.get("nombre")
        nit = request.form.get("nit")
        correo = request.form.get("correo")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")

        return render_template(
            "clientes_confirmacion.html",
            nombre=nombre,
            nit=nit,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )

    return render_template("clientes.html")


# Registro de proveedores
@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():

    if request.method == "POST":

        empresa = request.form.get("empresa")
        contacto = request.form.get("contacto")
        nit = request.form.get("nit")
        tipo = request.form.get("tipo")
        pago = request.form.get("pago")

        if request.form.get("activo"):
            activo = "Sí"
        else:
            activo = "No"

        return render_template(
            "proveedores_confirmacion.html",
            empresa=empresa,
            contacto=contacto,
            nit=nit,
            tipo=tipo,
            pago=pago,
            activo=activo
        )

    return render_template("proveedores.html")


if __name__ == "__main__":
    app.run(debug=True)