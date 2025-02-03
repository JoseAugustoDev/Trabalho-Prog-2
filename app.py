import pickle
import time

def qsort(l: list):
    if len(l) <= 1:
        return l
    
    menores = []
    maiores = []
    iguais = []

    pivot = l[0][1]

    for nome, nota, tempo in l:

        if nota < pivot: menores.append((nome, nota, tempo))
        if nota > pivot: maiores.append((nome, nota, tempo))
        if nota == pivot: iguais.append((nome, nota, tempo))
        
        if len(l) > 1:
            
          trocaIgual(iguais)

    return qsort(maiores) + iguais + qsort(menores)


def trocaIgual(iguais: list):

    for i in range(len(iguais) - 1):

        if iguais[i][0] > iguais[i + 1][0]: 
            troca(iguais, i, i + 1)

        if iguais[i][2] > iguais[i + 1][2]: 
            troca(iguais, i, i + 1)
    
    return iguais


def troca(l: list, i: int, j: int):

    aux = l[i]
    l[i] = l[j]
    l[j] = aux


def exibir(alunos: list):
    
    for nome, nota, tempo in alunos:
        
        print(nome, nota, tempo, end=" ")
        print()


def main():

    with open("dicionario-exemplo.bin", "rb") as f:
        alunos = pickle.load(f)

    l = []

    for matricula in alunos:
        
        notas = alunos[matricula][1:]
        nome_aluno = alunos[matricula][0]

        n1 = notas[0]
        n2 = notas[1]
        n3 = notas[2]
        n4 = notas[3]

        tempo = notas[4]

        nota = n1 + n2 + n3 + n4

        l.append((nome_aluno, nota, tempo))
    
    # l = [
    #  ("Hilario", 100, 23), ("Ana", 85, 12), ("Pedro", 50, 5), 
    #  ("Maria", 50, 18), ("Bruno", 86, 15), ("Joana", 92, 9),
    #  ("Carlos", 75, 27), ("Luana", 68, 14), ("Felipe", 99, 21), 
    #  ("Sofia", 71, 16), ("Ricardo", 60, 8), ("Beatriz", 80, 11), 
    #  ("Gabriel", 90, 30), ("Larissa", 95, 6), ("Lucas", 88, 19),
    #  ("Vera", 77, 3), ("Marcelo", 65, 26), ("Clara", 82, 25), 
    #  ("Rafael", 56, 17), ("Paula", 94, 7), ("Renato", 63, 20),
    #  ("Isabela", 91, 10), ("Julio", 79, 4), ("Lucia", 72, 22), 
    #  ("Thiago", 89, 28), ("Fernanda", 78, 13), ("Eduardo", 64, 24), 
    #  ("Alice", 70, 2), ("Tania", 83, 29), ("Gustavo", 80, 1),
    #  ("Marta", 85, 30), ("Ricardo", 92, 17), ("Samara", 74, 16),
    #  ("Marcelo", 87, 14), ("Lucas", 91, 5), ("Carlos", 96, 23),
    #  ("Gabriel", 65, 18), ("Larissa", 58, 9), ("Joao", 81, 13), 
    #  ("Paula", 80, 12), ("Rui", 50, 27), ("Carolina", 90, 8), 
    #  ("Arthur", 92, 15), ("Miguel", 99, 7), ("Cristina", 68, 25),
    #  ("Felipe", 74, 6), ("Fatima", 60, 19), ("Isabel", 76, 4), 
    #  ("Roberta", 91, 20), ("Vitor", 72, 22), ("Aline", 80, 11),
    #  ("Roberto", 75, 12), ("Mariana", 87, 5), ("Diego", 91, 10),
    #  ("Aline", 95, 6), ("Juliana", 92, 9), ("Tatiane", 64, 17),
    #  ("Douglas", 78, 26), ("Fabiana", 82, 3), ("Jorge", 61, 28),
    #  ("Sandra", 84, 21), ("Joao", 95, 23), ("Ricardo", 79, 8), 
    #  ("Joana", 85, 19), ("Marcelo", 60, 18), ("Carlos", 55, 7), 
    #  ("Jose", 90, 30), ("Eduardo", 93, 13), ("Pedro", 71, 5), 
    #  ("Rita", 88, 9), ("Gustavo", 70, 2), ("Amanda", 64, 11),
    #  ("Leandro", 85, 25), ("Natalia", 77, 6), ("Lilian", 92, 27), 
    #  ("Catarina", 83, 17), ("Renato", 88, 19), ("Valeria", 72, 3),
    #  ("Barbara", 91, 14), ("Marcos", 68, 8), ("Mariana", 89, 10), 
    #  ("Lucia", 86, 23), ("Claudia", 93, 4), ("Fabio", 77, 15), 
    #  ("Cecilia", 84, 18), ("Paulo", 59, 22), ("Ariana", 99, 12),
    #  ("Ester", 62, 9), ("Vitor", 96, 20), ("Sergio", 90, 28),
    #  ("Michele", 70, 17), ("Jose", 95, 8), ("Claudia", 84, 7),
    #  ("Marcelo", 98, 6), ("Daniel", 90, 13), ("Gisele", 79, 3),
    #  ("Gustavo", 61, 24), ("Paula", 94, 25), ("Tiago", 71, 26),
    #  ("Simone", 88, 10), ("Rodrigo", 66, 30), ("Adriana", 78, 4),
    #  ("Renan", 90, 23), ("Guilherme", 74, 17), ("Andre", 68, 12),
    #  ("Tatiane", 80, 20), ("Alberto", 77, 18), ("Lucia", 93, 21),
    #  ("Eduardo", 72, 6), ("Vanessa", 81, 13), ("Ricardo", 87, 15),
    #  ("Monique", 69, 10), ("Sergio", 62, 27), ("Nayara", 91, 22), 
    #  ("Ricardo", 58, 7), ("Lucas", 83, 16), ("Bruna", 65, 11), 
    #  ("Alan", 99, 30), ("Felipe", 90, 18), ("Jessica", 70, 5),
    #  ("Roberta", 72, 3), ("Laura", 74, 9), ("Cristiano", 95, 2),
    #  ("Carlos", 87, 6), ("Fabiano", 90, 24), ("Monica", 76, 28), 
    #  ("Vitor", 89, 21), ("Patricia", 66, 16), ("Jonas", 94, 10), 
    #  ("Felipe", 55, 8), ("Fernanda", 71, 14), ("Debora", 75, 13), 
    #  ("Jonas", 100, 29), ("Carla", 60, 7), ("Eliane", 88, 15),
    #  ("Jose", 65, 12), ("Vanessa", 91, 26), ("Joao", 95, 5), 
    #  ("Julia", 79, 19), ("Camila", 85, 3), ("Marco", 88, 22),
    #  ("Diana", 80, 17), ("Valeria", 63, 23), ("Ana", 77, 1),
    #  ("Tania", 94, 30), ("Gabriel", 66, 9), ("Cristina", 80, 24),
    #  ("Igor", 84, 18), ("Joaquim", 90, 27), ("Robson", 92, 7),
    #  ("Maria", 63, 16), ("Tatiane", 79, 5), ("Arthur", 96, 11),
    #  ("Sofia", 69, 12), ("Gustavo", 59, 25), ("Fernanda", 77, 8),
    #  ("Thiago", 80, 19), ("Aline", 92, 6), ("Rodrigo", 71, 17),
    #  ("Hugo", 60, 3), ("Claudia", 100, 6), ("Daniela", 87, 13),
    #  ("Larissa", 88, 15), ("Leandro", 72, 23), ("Marta", 91, 9),
    #  ("Sergio", 75, 5), ("Marcela", 96, 12), ("Nina", 58, 10),
    #  ("Carlos", 90, 6), ("Bruna", 80, 14), ("Claudia", 89, 25),
    #  ("Roberto", 65, 22), ("Lucia", 85, 18), ("Gustavo", 68, 11),
    #  ("Danilo", 100, 3), ("Elisabeth", 70, 19), ("Rafael", 92, 7),
    #  ("Ana", 72, 9), ("Marcos", 94, 30), ("Tatiane", 82, 15),
    #  ("Luana", 90, 2), ("Cristiano", 91, 12), ("Felipe", 73, 13),
    #  ("Miguel", 84, 28), ("Alana", 100, 26), ("Vera", 69, 30),
    #  ("Paulo", 88, 14), ("Lucas", 85, 17), ("Amanda", 77, 6),
    #  ("Ricardo", 58, 4), ("Felipe", 79, 25), ("Leticia", 93, 10),
    #  ("Mauricio", 82, 20), ("Tatiane", 60, 9), ("Robson", 75, 15),
    #  ("Bruna", 78, 16), ("Ricardo", 94, 7), ("Jessica", 92, 24),
    #  ("Silvia", 66, 19), ("Claudia", 67, 12), ("Andre", 89, 8),
    #  ("Valeria", 100, 5), ("Catarina", 80, 6), ("Fabio", 93, 17),
    #  ("Silvana", 63, 11), ("Lucas", 79, 13), ("Carlos", 88, 20),
    #  ("Gabriel", 75, 21), ("Lucas", 92, 4), ("Laura", 65, 23)
    # ]
    
    t1 = time.time()
    
    alunos = qsort(l)

    t2 = time.time()
    
    exibir(alunos)
    
    tempo = t2 - t1
    
    print(f"Tempo: {tempo}")


if __name__ == "__main__":
    main()