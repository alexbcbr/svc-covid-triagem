def handler(event, context):
    
    if (int(event['temperatura'])) > 37:
        resultado = "quarantena"
    else:
        resultado = "liberado"
       
    return { 
        'diagnostico' : resultado
    }
