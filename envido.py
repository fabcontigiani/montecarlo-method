import random
from jugador import Jugador

def envido(quienCanta: Jugador, quienResponde:Jugador):
    # if quienResponde.tantos >= 27: # Quien responde dice 'Quiero'
    if random.random() <= quienResponde.probabilidadEnvido[quienResponde.tantos]: # Quien responde dice 'Quiero'
        quienResponde.tantosRival = quienCanta.tantos # Quien canta dice sus tantos
        
        if quienResponde.tantos > quienResponde.tantosRival: # Quien responde tiene mas tantos
            quienCanta.tantosRival = quienResponde.tantos # Quien responde dice sus tantos
            quienResponde.puntos += 2
            return
        else: # Quien responde tiene menos tantos
            quienCanta.puntos += 2
            return # Quien responde dice 'Son buenas', denegando informacion al rival
    quienCanta.puntos += 1 # Quien responde dice 'No quiero'