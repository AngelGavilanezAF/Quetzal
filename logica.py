def responder(mensaje):
    mensaje = mensaje.lower()

    saludos = ["hola", "buenos dias", "buenas tardes", "buenas noches", "que tal"]
    fertilizante = ["abono", "nutriente", "fertilizante"]
    plaga = ["plagas", "insectos", "plaga"]

    if any(palabra in mensaje for palabra in saludos):
        return "Hola, ¿en qué puedo ayudarte?"

    elif any(palabra in mensaje for palabra in fertilizante):
        return "Los fertilizantes aportan nutrientes al suelo y ayudan a la planta."

    elif any(palabra in mensaje for palabra in plaga):
        return "Primero se debe identificar qué tipo de insecto es."

    else:
        return "Error, inténtelo después."
