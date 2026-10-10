import random
import sys
import time
import os
# ---------------------------------------------------------------------------
# CONFIGURAÇÕES (valores fixos usados pelo programa)
# ---------------------------------------------------------------------------
PONTOS_POR_ACERTO = 10
BONUS_SEQUENCIA = 5          # bônus extra a cada acerto a partir da sequência mínima
SEQUENCIA_MINIMA_BONUS = 3   # acertos seguidos necessários para ganhar bônus
PERGUNTAS_POR_RODADA = 5
TOTAL_RODADAS = 3
LETRAS = "abcd"

# ---------------------------------------------------------------------------
# BANCO DE PERGUNTAS
# Convenção: a PRIMEIRA opção de cada pergunta é sempre a correta.
# As opções são embaralhadas na hora de exibir (ver preparar_opcoes).
# ---------------------------------------------------------------------------
BANCO_PERGUNTAS = [
    {"pergunta": "Qual estrutura de repetição executa um bloco enquanto uma condição for verdadeira?",
     "opcoes": ["while", "if", "def", "import"]},
    {"pergunta": "Qual símbolo é usado em Python para atribuir um valor a uma variável?",
     "opcoes": ["=", "==", "!=", "->"]},
    {"pergunta": "Qual função do Python exibe um texto na tela?",
     "opcoes": ["print()", "input()", "len()", "range()"]},
    {"pergunta": "Qual palavra-chave é usada para definir uma função nomeada em Python?",
     "opcoes": ["def", "func", "function", "method"]},
    {"pergunta": "Qual tipo de dado do Python guarda uma sequência ordenada e modificável de elementos?",
     "opcoes": ["list", "tuple", "str", "int"]},
    {"pergunta": "Qual é o resultado de 7 // 2 em Python?",
     "opcoes": ["3", "3.5", "4", "1"]},
    {"pergunta": "Qual é o resultado de 7 % 2 em Python?",
     "opcoes": ["1", "3", "0", "3.5"]},
    {"pergunta": "Em qual paradigma o programa é descrito como uma sequência de comandos que alteram o estado dos dados?",
     "opcoes": ["Imperativo", "Funcional", "Lógico", "Declarativo"]},
    {"pergunta": "Qual linguagem foi criada por Dennis Ritchie?",
     "opcoes": ["C", "Python", "Java", "Pascal"]},
    {"pergunta": "Qual comando encerra um laço (for/while) antes de a sua condição terminar?",
     "opcoes": ["break", "continue", "pass", "else"]},
    {"pergunta": "O que a expressão len('python') retorna?",
     "opcoes": ["6", "5", "7", "'python'"]},
    {"pergunta": "Qual operador lógico do Python representa o 'E'?",
     "opcoes": ["and", "or", "not", "xor"]},
    {"pergunta": "Qual estrutura é usada para tomar decisões em um programa?",
     "opcoes": ["if", "for", "while", "def"]},
    {"pergunta": "Quantas vezes o bloco de 'for i in range(3):' é executado?",
     "opcoes": ["3", "2", "4", "Infinitas vezes"]},
    {"pergunta": "Qual é o índice do primeiro elemento de uma lista em Python?",
     "opcoes": ["0", "1", "-1", "2"]},
    {"pergunta": "O que significa a sigla CPU?",
     "opcoes": ["Unidade Central de Processamento", "Central de Programas Unificados",
                "Controle de Processos Unidos", "Computador Pessoal Universal"]},
    {"pergunta": "Quantos bits formam 1 byte?",
     "opcoes": ["8", "4", "16", "32"]},
    {"pergunta": "Qual comando do Git registra as alterações no histórico do repositório local?",
     "opcoes": ["git commit", "git push", "git clone", "git init"]},
    {"pergunta": "Qual comando do Git envia os commits locais para o repositório remoto?",
     "opcoes": ["git push", "git commit", "git add", "git status"]},
    {"pergunta": "Qual função do Python lê um texto digitado pelo usuário?",
     "opcoes": ["input()", "print()", "open()", "range()"]},
]
 
def digitar(texto, atraso=0.03):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
CIANO = "\033[96m"
RESET = "\033[0m"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
# ---------------------------------------------------------------------------
# FUNÇÕES DE ESTADO E ENTRADA
# ---------------------------------------------------------------------------
def criar_estado():
    """Cria o dicionário que guarda o estado de uma partida."""
    estado = {
        "pontuacao": 0,
        "acertos": 0,
        "erros": 0,
        "sequencia": 0,          # acertos seguidos no momento
        "melhor_sequencia": 0,   # maior sequência da partida
    }
    return estado
 
 
def pedir_nome():
    """Repete a leitura até o jogador digitar um nome não vazio."""
    nome = ""
    while nome == "":
        nome = input("Agente, identifique-se: ").strip()
        if nome == "":
            print(VERMELHO + "O nome não pode ficar vazio." + RESET)
    return nome
 
 
def perguntar_sim_nao(texto):
    """Repete até o usuário responder 's' ou 'n'. Retorna True para 's'."""
    while True:
        resposta = input(texto + " (s/n): ").strip().lower()
        if resposta == "s":
            return True
        if resposta == "n":
            return False
        print(VERMELHO + "Responda apenas com 's' ou 'n'." + RESET)
 
 
def ler_letra(quantidade_opcoes):
    """Lê a resposta do jogador e valida; devolve o índice (0 a 3) da opção."""
    letras_validas = LETRAS[:quantidade_opcoes]
    while True:
        entrada = input("Sua resposta: ").strip().lower()
        if len(entrada) == 1 and entrada in letras_validas:
            return letras_validas.index(entrada)
        print(VERMELHO + "Resposta inválida. Digite uma letra entre a e " + letras_validas[-1] + "." + RESET)
 
 
# ---------------------------------------------------------------------------
# FUNÇÕES DO JOGO
# ---------------------------------------------------------------------------
def preparar_opcoes(pergunta):
    """
    Embaralha as opções de uma pergunta sem alterar o banco original.
    Retorna a lista embaralhada e o índice da opção correta.
    """
    opcoes = pergunta["opcoes"][:]        # cópia da lista
    texto_correto = opcoes[0]             # a primeira é a correta
    random.shuffle(opcoes)                # altera a ordem da cópia
    indice_correto = opcoes.index(texto_correto)
    return opcoes, indice_correto
 
 
def atualizar_estado(estado, acertou):
    """Altera as variáveis do estado conforme a resposta e devolve os pontos ganhos."""
    pontos_ganhos = 0
    if acertou:
        estado["acertos"] = estado["acertos"] + 1
        estado["sequencia"] = estado["sequencia"] + 1
        pontos_ganhos = PONTOS_POR_ACERTO
        if estado["sequencia"] >= SEQUENCIA_MINIMA_BONUS:
            pontos_ganhos = pontos_ganhos + BONUS_SEQUENCIA
        estado["pontuacao"] = estado["pontuacao"] + pontos_ganhos
        if estado["sequencia"] > estado["melhor_sequencia"]:
            estado["melhor_sequencia"] = estado["sequencia"]
    else:
        estado["erros"] = estado["erros"] + 1
        estado["sequencia"] = 0
    return pontos_ganhos
 
 
def fazer_pergunta(numero, total, pergunta, estado):
    """Exibe uma pergunta, lê a resposta, atualiza o estado. Retorna True se acertou."""
    opcoes, indice_correto = preparar_opcoes(pergunta)
 
    print("\nPergunta " + str(numero) + " de " + str(total))
    digitar(AMARELO + pergunta["pergunta"] + RESET)
    for i in range(len(opcoes)):
        print("  " + LETRAS[i] + ") " + VERDE + opcoes[i] + RESET)
 
    escolhida = ler_letra(len(opcoes))
    acertou = (escolhida == indice_correto)
    pontos = atualizar_estado(estado, acertou)
 
    if acertou:
        mensagem = "Correto! +" + str(pontos) + " pontos"
        if estado["sequencia"] >= SEQUENCIA_MINIMA_BONUS:
            mensagem = mensagem + " (bônus de sequência: " + str(estado["sequencia"]) + " seguidas)"
        print(VERDE + mensagem + RESET)
    else:
        print(VERMELHO + "Errado. A resposta correta era: " + LETRAS[indice_correto] + ") " + opcoes[indice_correto] + RESET)
    return acertou
 
 
def jogar_rodada(numero_rodada, perguntas, estado):
    """Percorre as perguntas da rodada. Retorna a quantidade de acertos nela."""
    print(VERDE + "\n" + "=" * 50 + RESET)
    print(AMARELO + "RODADA " + str(numero_rodada) + " de " + str(TOTAL_RODADAS) + RESET)
    print(VERDE + "=" * 50 + RESET)
 
    acertos_rodada = 0
    indice = 0
    while indice < len(perguntas):
        acertou = fazer_pergunta(indice + 1, len(perguntas), perguntas[indice], estado)
        if acertou:
            acertos_rodada = acertos_rodada + 1
        indice = indice + 1
 
    print("\nFim da rodada " + str(numero_rodada) + ": "
          + str(acertos_rodada) + "/" + str(len(perguntas)) + " acertos. "
          + "Pontuação atual: " + str(estado["pontuacao"]))
    return acertos_rodada
 
 
def classificar(percentual):
    """Devolve uma classificação em texto conforme o percentual de acertos."""
    if percentual >= 90:
        return (CIANO + "Excelente!" + RESET)
    elif percentual >= 70:
        return (VERDE + "Muito bom!" + RESET)
    elif percentual >= 50:
        return (AMARELO + "Bom, mas dá para melhorar." + RESET)
    else:
        return (VERMELHO + "Continue estudando!" + RESET)
 
 
def mostrar_resultado_final(nome, estado):
    """Calcula o percentual de acertos e imprime o resumo da partida."""
    total_perguntas = PERGUNTAS_POR_RODADA * TOTAL_RODADAS
    percentual = estado["acertos"] * 100 / total_perguntas
 
    print(VERDE + "\n" + "=" * 50 + RESET)
    print(AMARELO + "          RESULTADO FINAL - " + RESET + CIANO + nome + RESET)
    print(VERDE + "=" * 50 + RESET)
    print("Acertos: " + VERDE + str(estado["acertos"]) + "/" + str(total_perguntas) + RESET
          + " (" + str(round(percentual, 1)) + "%)")
    print("Erros: " + VERMELHO + str(estado["erros"]) + RESET)
    print("Maior sequência de acertos: " + CIANO + str(estado["melhor_sequencia"]) + RESET)
    print("Pontuação final: " + str(estado["pontuacao"]))
    print("Classificação: " + classificar(percentual))
 
 
def jogar_partida(nome):
    """Executa uma partida completa (todas as rodadas). Retorna a pontuação final."""
    estado = criar_estado()
 
    # Sorteia, sem repetir, as perguntas de TODAS as rodadas de uma vez.
    quantidade_total = PERGUNTAS_POR_RODADA * TOTAL_RODADAS
    sorteadas = random.sample(BANCO_PERGUNTAS, quantidade_total)
 
    for rodada in range(1, TOTAL_RODADAS + 1):
        inicio = (rodada - 1) * PERGUNTAS_POR_RODADA
        fim = inicio + PERGUNTAS_POR_RODADA
        perguntas_da_rodada = sorteadas[inicio:fim]
 
        jogar_rodada(rodada, perguntas_da_rodada, estado)
 
        if rodada < TOTAL_RODADAS:
            input("\nPressione Enter para a próxima rodada...")
 
    mostrar_resultado_final(nome, estado)
    return estado["pontuacao"]
 
 
def main():
    os.system("")
    limpar_tela()
    digitar(VERDE + "=" * 50 + RESET, 0.01)
    digitar(AMARELO + "         QUIZ DE PERGUNTAS E RESPOSTAS" + RESET, 0.03)
    digitar(VERDE + "=" * 50 + RESET, 0.01)
    digitar(AMARELO + "São " + str(TOTAL_RODADAS) + " rodadas com " + str(PERGUNTAS_POR_RODADA)
          + " perguntas cada. Cada acerto vale " + str(PONTOS_POR_ACERTO) + " pontos." + RESET, 0.03)
    digitar(AMARELO + "A partir de " + str(SEQUENCIA_MINIMA_BONUS) + " acertos seguidos, "
          + "você ganha +" + str(BONUS_SEQUENCIA) + " por acerto.\n" + RESET, 0.03)

    nome = pedir_nome()
    recorde = 0
    jogando = True
 
    while jogando:
        pontuacao = jogar_partida(nome)
 
        if pontuacao > recorde:
            recorde = pontuacao
            print("Novo recorde da sessão: " + str(recorde) + " pontos!")
        else:
            print("Recorde da sessão: " + str(recorde) + " pontos.")
 
        jogando = perguntar_sim_nao("\nDeseja jogar novamente?")
 
    print(VERDE + "\nObrigado por jogar, " + nome + "!" + RESET)
 
 
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nJogo encerrado.")