def handler(event, context):
    
    if (event['temperatura']) > 37:
        resultado = "quarantena"
    else:
        resultado = "liberado"
    
    message = 'Paciente {} {}!'.format(event['paciente'], resultado)
    
    return { 
        'message' : message
    }
