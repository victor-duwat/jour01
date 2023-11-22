def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    return f"{heures} heures et {minutes_restantes} minutes"


print(time_to_text(125))  

