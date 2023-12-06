x = 0
y = 0
for i in range(0, 10):
    x = int(input(f"Wat is het {i + 1}de getal\n"))
    y = y + x

gemiddelde = y/10
print(f"\n\nHet gemiddelde van de getallen is {gemiddelde}")
