vogais = ["a","e","i","o","u"]
aux = []

palavra = input("Digite a palavra que deseja contar as vogais: ")
for i in vogais:
    for j in palavra:
        if j.lower() == i.lower():
            aux.append(j)

print(f"Na palavra {palavra} foram encontradas {len(aux)} vogais.\nAs vogais são {aux}")
