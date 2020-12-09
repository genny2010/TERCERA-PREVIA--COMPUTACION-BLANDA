#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CONTROL DIFUSO API
# Genny Paola Rivera Becerra 1087561571

#Elimina las advertencias 
import warnings
warnings.filterwarnings("ignore")

#Importa las librerias 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 
get_ipython().run_line_magic('matplotlib', 'inline')

#Se crean los objetos antecedentes y concecuentes a partir de las 
# vairables del universo y las funciones de membresia

Calidad = ctrl.Antecedent(np.arange(0, 11, 1), "Calidad")
Servicio = ctrl.Antecedent(np.arange(0, 11, 1), "Servicio")
Propina = ctrl.Consequent(np.arange(0, 26, 1), "Propina")

# La poblacion de la funcion de membresia automatica es posible con .automf (3, 5 o 7)
Calidad.automf(3)
Servicio.automf(3)

# Las funciones de membresia personalizadas se pueden contruir interactivamente con la 
# API Pythonic
Propina["bajo"]= Fuzz.trimf(Propina.universe, [0, 0, 13])
Propina["medio"]= Fuzz.trimf(Propina.universe, [0, 13, 25])
Propina["alto"]= Fuzz.trimf(Propina.universe, [13, 25, 25])

# Visualizacion con .view()
Calidad["average"].view()
Servicio.view()
Propina.view()

# Creacion de las reglas 
regla1 = ctrl.Rule(Calidad ["poor"] | Servicio["poor"], Propina["bajo"])
regla2 = ctrl.Rule(Servicio ["average"] | Propina["medio"])
regla3 = ctrl.Rule(Servicio ["good"] | Calidad["good"], Propina["alto"])

# Visualizacion de la regla 1
regla1.view()

# Generacion del simulador 
control_Propina = ctrl.ControlSystem([regla1, regla2, regla3])
asignacion_Propina = ctrl.ControlSystemSimulation(control_Propina)

# Pasar entradas al ControlSystem usando etiquetas "Antecedent" con Pythonic API
# Nota: si quiere pasar muchas entradas a la vez, usar .inputs (dict_of_data)
asignacion_Propina.input["Calidad"] = 6.5
asignacion_Propina.input["Servicio"] = 9.8

# Se obtiene el valor 
asignacion_Propina.computer()

# Se muestra la informacion
Print("valor de la Propina:")
Print (asignacion_Propina.output["Propina"])

# Se muestra la curva de asignacion de porpina
Propina.view(sim=asignacion_Propina)


# In[ ]:





# In[ ]:




