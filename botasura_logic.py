import random

def gen_eco():
    ecologic = ["FILTRO DE AGUA 🚰 https://www.youtube.com/watch?v=nk7f3cwxFUQ", "LADRILLOS ECOLOGICOS 🧱 https://www.youtube.com/watch?v=gSf7pq45Ymg","COMO RECICLAR EN CASA ♻️ https://www.youtube.com/watch?v=zG45P6-dpM4" ]
    return random.choice(ecologic)

def gen_consejo():
    ecoconsejo = ["si vas a crear un ladrillo ecologico no metas papel dentro", "para crear buenos ladrillos ecologicos debes lavar los residuos primero","si vas a reciclar revisa que sea el bote correcto","puedes utilizar varios resiudos organicos para hacer un buen compostaje" ]
    return random.choice(ecoconsejo)
