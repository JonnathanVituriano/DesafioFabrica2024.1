count = 1

while count <= 6:

    if count <= 5:
        aluno = str(input("Qual o seu nome? "))

        n1 = float(input("Digite a sua primeira nota: "))
        n2 = float(input("Digite a sua segunda nota: "))
        n3 = float(input("Digite a sua terceira nota: "))

        media = (n1 + n2 + n3) / 3

        print ("A média do aluno", aluno, "é igual à: ", media)

        count += 1

        print (count)
    else: 
        print ("Todas as notas de todos os 5 alunos foram feitas!!")
        break