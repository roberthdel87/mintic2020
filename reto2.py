# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:49:10 2020

@author: roberthdel87
"""
def prestamo(informacion: dict) -> dict:
    id_prestamo = informacion["id_prestamo"]
    i_c = informacion["ingreso_codeudor"]
    i_d = informacion["ingreso_deudor"]
    c_p = informacion["cantidad_prestamo"]
    
    if informacion["historia_credito"]==1:
        if i_c > 0 and (i_d/9) > c_p:
            return {"id_prestamo": id_prestamo, "aprobado": True}
        else:
            if (informacion["dependientes"] == "3+" or informacion["dependientes"] > 2 )  and informacion["independiente"]=="Si":
                return {"id_prestamo": id_prestamo, "aprobado": ((i_c / 12) > c_p)}
            else: 
                return {"id_prestamo": id_prestamo, "aprobado": (c_p < 200)}
    else:
        if informacion["independiente"]=="Si":
            if not(informacion["casado"]=="Si" and (informacion["dependientes"] =="3+" or informacion["dependientes"] > 1 )):
                if (i_d/10) > c_p or (i_c/10) >c_p:
                    return {"id_prestamo": id_prestamo, "aprobado": (c_p < 180)}
                else:
                    return {"id_prestamo": id_prestamo, "aprobado": False}
            else:
                return {"id_prestamo": id_prestamo, "aprobado": False}
        else:
            if not(informacion["tipo_propiedad"]=="semiurbano" and informacion["dependientes"] < 2):
                if informacion["educacion"]=="Graduado":
                    return {"id_prestamo": id_prestamo, "aprobado": ((i_d/11) > c_p and (i_c/11) > c_p)}
                else:
                    return {"id_prestamo": id_prestamo, "aprobado": False}
            else:
                return {"id_prestamo": id_prestamo, "aprobado": False}
    
print(prestamo({
    'id_prestamo': 'RETOS2_001',
    'casado': 'No',
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'Si',
    'ingreso_deudor': 4692,
    'ingreso_codeudor': 0,
    'cantidad_prestamo': 106,
    'plazo_prestamo': 360,
    'historia_credito': 1,
    'tipo_propiedad': 'Rural'
    }))
print(prestamo({'id_prestamo': 'RETOS2_011', 'casado': 'No', 'dependientes': '3+', 'educacion': 'Graduado', 'independiente': 'No', 'ingreso_deudor': 3083, 'ingreso_codeudor': 0, 'cantidad_prestamo': 255, 'plazo_prestamo': 360, 'historia_credito': 1, 'tipo_propiedad': 'Rural'}))

'''
Ejemplos para usar: 

id_prestamo = "RETOS2_001"
casado = "No"
dependientes = 1
educacion = "Graduado"
independiente = "Si"
ingreso_deudor = 4692
ingreso_codeudor = 0
cantidad_prestamo = 106
plazo_prestamo = 360
historia_credito = 1
tipo_propiedad = "Rural"

id_prestamo = "RETOS2_002"
casado = "No"
dependientes = "3+"
educacion = "No Graduado"
independiente = "No"
ingreso_deudor = 1830
ingreso_codeudor = 0
cantidad_prestamo = 100
plazo_prestamo = 360
historia_credito = 0
tipo_propiedad = "Urbano"

id_prestamo = "RETOS2_003"
casado = "No"
dependientes = 0
educacion = "No Graduado"
independiente = "No"
ingreso_deudor = 3748
ingreso_codeudor = 1668
cantidad_prestamo = 110
plazo_prestamo = 360
historia_credito = 1
tipo_propiedad = "Semiurbano"
'''
