import pystyle

color = pystyle.Colors.DynamicMIX((pystyle.Col.white, pystyle.Col.light_gray)) 

def out(text = ""):
    print(pystyle.Colorate.Horizontal(color, text))

def inp(text = ""):
    data = input(pystyle.Colorate.Horizontal(color, f"{text} :") + " ")
    return data
