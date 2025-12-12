def responder(mensaje):
    mensaje = mensaje()

    if "hola" or "Hola" in mensaje:
        return "¡Hola! ¿En qué puedo ayudarte en agronomía?"

    elif "maíz" or "maiz" in mensaje:
        return "El maíz requiere buen nitrógeno y temperaturas mayores a 15°C para sembrar."

    elif "fertilizante" in mensaje:
        return "Los fertilizantes NPK son comunes. ¿Para qué cultivo lo necesitas?"
    
    elif "quien te creo?" in mensaje: 
        return "La Lejandra y El terror de las milfs, alias el gavilanez"

    else:
        return "Aún no tengo una respuesta para eso. ¿Puedes intentar de nuevo?"
