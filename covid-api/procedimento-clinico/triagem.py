def handler(event, context):
    
    if (event['temperatura']) > 37:
        resultado = "quarantena"
    else:
        resultado = "liberado"
       
    return { 
        'diagnostico' : resultado
    }
