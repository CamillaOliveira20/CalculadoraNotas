percentual = int(input("Qual a nota do aluno em %? "))
ultimo_digito = percentual % 10


if ultimo_digito >= 7:
    modificador = "+"
elif ultimo_digito >= 3:
    modificador = ""
else:
    modificador = "-"

nota = ""

if percentual >= 90:
    if percentual >= 93:
        nota = "A"
    else:
        nota = "A-"

elif percentual >= 80:
        nota = "B" + modificador
   
elif percentual >= 70:
    if percentual >= 78:
        nota = "C"
    else:
        nota = "C-"

elif percentual >= 60:
    if percentual >= 68:
        nota = "D"
    else:
        nota = "D-"

else:
    nota = "F"

print(f"A nota do aluno é {nota}")
