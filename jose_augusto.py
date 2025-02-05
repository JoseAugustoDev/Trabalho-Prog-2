import pickle

# Feito por José Augusto

def carregar_dados(nome_arquivo):

    with open(nome_arquivo, "rb") as arquivo:
        dados = pickle.load(arquivo)

    return dados


def calcular_nota_total(aluno):

    nota1, nota2, nota3, nota4 = aluno[1], aluno[2], aluno[3], aluno[4]
    nota_total = nota1 + nota2 + nota3 + nota4

    return nota_total


def merge_sort(matriculas, alunos):

    if len(matriculas) <= 1:
        return matriculas

    meio = len(matriculas) // 2

    # Ordenando os alunos que ficaram a esquerda
    esquerda = merge_sort(matriculas[:meio], alunos)

    # Ordenando os alunos que ficaram a direta
    direita = merge_sort(matriculas[meio:], alunos)

    return merge(esquerda, direita, alunos)


def merge(esquerda, direita, alunos):

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):

        # Calculando a nota do aluno a esquerda na posicao i
        nota_total_esq = calcular_nota_total(alunos[esquerda[i]])

        # Calculando a nota do aluno a esquerda na posicao j
        nota_total_dir = calcular_nota_total(alunos[direita[j]])

        # Primeiramente, ordenando por nota
        if nota_total_esq > nota_total_dir:
            resultado.append(esquerda[i])
            i += 1

        elif nota_total_esq < nota_total_dir:
            resultado.append(direita[j])
            j += 1

        else:
            # Se houve empate por nota, ordena por tempo
            tempo_esq = alunos[esquerda[i]][5]
            tempo_dir = alunos[direita[j]][5]

            if tempo_esq < tempo_dir:
                resultado.append(esquerda[i])
                i += 1

            elif tempo_esq > tempo_dir:
                resultado.append(direita[j])
                j += 1

            else:
                # Se houve empate por nota e tempo, ordena por nome
                nome_esq = alunos[esquerda[i]][0]
                nome_dir = alunos[direita[j]][0]

                if nome_esq < nome_dir:
                    resultado.append(esquerda[i])
                    i += 1

                elif nome_esq > nome_dir:
                    resultado.append(direita[j])
                    j += 1

                else:
                    # Se todos os outros casos empataram, ordena por matricula.
                    matricula_esq = esquerda[i]
                    matricula_dir = direita[j]

                    if matricula_esq < matricula_dir:
                        resultado.append(esquerda[i])
                        i += 1

                    else:
                        resultado.append(direita[j])
                        j += 1

    while i < len(esquerda):
        resultado.append(esquerda[i])
        i += 1

    while j < len(direita):
        resultado.append(direita[j])
        j += 1

    return resultado


def gerar_saida(matriculas, alunos, nome_arquivo_saida):

    with open(nome_arquivo_saida, "w") as arquivo_saida:

        # Limitando o bonus a quantidade exigida no trabalho que sãp os 5 primeiros alunos
        limite_bonus = 5
        nota_limite = calcular_nota_total(alunos[matriculas[4]]) # Nota do quinto colocado
        tempo_limite = alunos[matriculas[4]][5] # Tempo do quinto colocado

        for i in range(len(matriculas)):

            matricula = matriculas[i]
            aluno = alunos[matricula]
            nota_total = calcular_nota_total(aluno)

            if (i < limite_bonus) or (nota_total == nota_limite and aluno[5] == tempo_limite):
                nota_total += 2

            # Escrevendo no arquivo txt o nome e a nota
            arquivo_saida.write(f"{aluno[0]} {nota_total}\n")


def main():
    nome_arquivo = "dicionario-exemplo-100000.bin"
    alunos = carregar_dados(nome_arquivo)

    matriculas = []
    for matricula in alunos:
        matriculas.append(matricula)

    matriculas_ordenadas = merge_sort(matriculas, alunos)

    gerar_saida(matriculas_ordenadas, alunos, "saida.txt")


if __name__ == "__main__":
    main()
