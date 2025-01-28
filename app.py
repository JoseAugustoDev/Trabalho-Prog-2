import time

def qsort(l: list):
    if len(l) <= 1:
        return l
    
    menores = []
    maiores = []
    iguais = []

    pivot = l[0][1]

    for nome, nota in l:

        if nota < pivot: menores.append((nome, nota))
        if nota > pivot: maiores.append((nome, nota))
        if nota == pivot: iguais.append((nome, nota))
        
        trocaIgual(iguais)

    return qsort(maiores) + iguais + qsort(menores)

def trocaIgual(iguais: list):
    for i in range(len(iguais) - 1):
        if iguais[i][0] > iguais[i + 1][0]: 
            troca(iguais, i, i + 1)
    
    return iguais

    


def troca(l: list, i: int, j: int):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux



def exibir(alunos: list):
    for nome, nota in alunos:
        print(nome, nota, end=" ")
        print()


def main():
    l = [
    ("Hilário", 100), ("Ana", 85), ("Pedro", 50), ("Maria", 50), ("Bruno", 86),
    ("Joana", 92), ("Carlos", 75), ("Luana", 68), ("Felipe", 99), ("Sofia", 71),
    ("Ricardo", 60), ("Beatriz", 80), ("Gabriel", 90), ("Larissa", 95), ("Lucas", 88),
    ("Vera", 77), ("Marcelo", 65), ("Clara", 82), ("Rafael", 56), ("Paula", 94),
    ("Renato", 63), ("Isabela", 91), ("Júlio", 79), ("Lúcia", 72), ("Thiago", 89),
    ("Fernanda", 78), ("Eduardo", 64), ("Alice", 70), ("Tânia", 83), ("Gustavo", 80),
    ("Marta", 85), ("Ricardo", 92), ("Samara", 74), ("Marcelo", 87), ("Lucas", 91),
    ("Carlos", 96), ("Gabriel", 65), ("Larissa", 58), ("João", 81), ("Paula", 80),
    ("Rui", 50), ("Carolina", 90), ("Arthur", 92), ("Miguel", 99), ("Cristina", 68),
    ("Felipe", 74), ("Fátima", 60), ("Isabel", 76), ("Roberta", 91), ("Vitor", 72),
    ("Aline", 80), ("Roberto", 75), ("Mariana", 87), ("Diego", 91), ("Aline", 95),
    ("Juliana", 92), ("Tatiane", 64), ("Douglas", 78), ("Fabiana", 82), ("Jorge", 61),
    ("Sandra", 84), ("João", 95), ("Ricardo", 79), ("Joana", 85), ("Marcelo", 60),
    ("Carlos", 55), ("José", 90), ("Eduardo", 93), ("Pedro", 71), ("Rita", 88),
    ("Gustavo", 70), ("Amanda", 64), ("Leandro", 85), ("Natália", 77), ("Lilian", 92),
    ("Catarina", 83), ("Renato", 88), ("Valéria", 72), ("Bárbara", 91), ("Marcos", 68),
    ("Mariana", 89), ("Lúcia", 86), ("Cláudia", 93), ("Fábio", 77), ("Cecília", 84),
    ("Paulo", 59), ("Ariana", 99), ("Ester", 62), ("Vítor", 96), ("Sérgio", 90),
    ("Michele", 70), ("José", 95), ("Claudia", 84), ("Marcelo", 98), ("Daniel", 90),
    ("Gisele", 79), ("Gustavo", 61), ("Paula", 94), ("Tiago", 71), ("Simone", 88),
    ("Rodrigo", 66), ("Adriana", 78), ("Renan", 90), ("Guilherme", 74), ("André", 68),
    ("Tatiane", 80), ("Alberto", 77), ("Lúcia", 93), ("Eduardo", 72), ("Vanessa", 81),
    ("Ricardo", 87), ("Monique", 69), ("Sérgio", 62), ("Nayara", 91), ("Ricardo", 58),
    ("Lucas", 83), ("Bruna", 65), ("Alan", 99), ("Felipe", 90), ("Jéssica", 70),
    ("Roberta", 72), ("Laura", 74), ("Cristiano", 95), ("Carlos", 87), ("Fabiano", 90),
    ("Mônica", 76), ("Vítor", 89), ("Patrícia", 66), ("Jonas", 94), ("Felipe", 55),
    ("Fernanda", 71), ("Débora", 75), ("Jonas", 100), ("Carla", 60), ("Eliane", 88),
    ("José", 65), ("Vanessa", 91), ("João", 95), ("Júlia", 79), ("Camila", 85),
    ("Marco", 88), ("Diana", 80), ("Valéria", 63), ("Ana", 77), ("Tânia", 94),
    ("Gabriel", 66), ("Cristina", 80), ("Igor", 84), ("Joaquim", 90), ("Robson", 92),
    ("Maria", 63), ("Tatiane", 79), ("Arthur", 96), ("Sofia", 69), ("Gustavo", 59),
    ("Fernanda", 77), ("Thiago", 80), ("Aline", 92), ("Rodrigo", 71), ("Hugo", 60),
    ("Claudia", 100), ("Daniela", 87), ("Larissa", 88), ("Leandro", 72), ("Marta", 91),
    ("Sérgio", 75), ("Marcela", 96), ("Nina", 58), ("Carlos", 90), ("Bruna", 80),
    ("Cláudia", 89), ("Roberto", 65), ("Lúcia", 85), ("Gustavo", 68), ("Danilo", 100),
    ("Elisabeth", 70), ("Rafael", 92), ("Ana", 72), ("Marcos", 94), ("Tatiane", 82),
    ("Luana", 90), ("Cristiano", 91), ("Felipe", 73), ("Miguel", 84), ("Alana", 100),
    ("Vera", 69), ("Paulo", 88), ("Lucas", 85), ("Amanda", 77), ("Ricardo", 58),
    ("Felipe", 79), ("Letícia", 93), ("Maurício", 82), ("Tatiane", 60), ("Robson", 75),
    ("Bruna", 78), ("Ricardo", 94), ("Jéssica", 92), ("Sílvia", 66), ("Claudia", 67),
    ("André", 89), ("Valéria", 100), ("Catarina", 80), ("Fábio", 93), ("Silvana", 63),
    ("Lucas", 79), ("Carlos", 88), ("Gabriel", 75), ("Lucas", 92), ("Laura", 65)
]


    t1 = time.time()
    
    alunos = qsort(l)
    
    exibir(alunos)
    
    t2 = time.time()
    
    tempo = t2 - t1
    
    print(tempo)


if __name__ == "__main__":
    main()