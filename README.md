# Jogo-de-perguntas-e-respostas
RESOLUÇÃO DE PROBLEMA COM PARADIGMA IMPERATIVO USANDO O TEMA: Jogo de perguntas e respostas
# Quiz de Perguntas e Respostas — Paradigma Imperativo (Python)
 
**Disciplina:** Paradigmas de Programação — Universidade da Amazônia (Ciência da Computação)
**Professor:** Rodrigo Medeiros Costa
**Atividade:** AV1 — Resolução de problema com paradigma imperativo
## Integrantes
 
| Nome | GitHub |
| --- | --- |
| _João Oberlim Lira Martins_ | _@oberlimm_ |
| _Pedro Lucas da Silva Goulart_ | _@PedroGordoLucas_ |
| _Germano Pedro Minami Rodrigues_ | _@germano004_ |
## 🎥 Vídeo de demonstração
 
_Cole aqui o link do vídeo (ou insira o arquivo no repositório)._
 
---Depois a gente coloca

## 1. Descrição do problema
 
Criamos um **jogo de perguntas e respostas (quiz)** executado no terminal, com pontuação, controle de rodadas e apresentação do resultado final.
Plaintext

## Fluxo do Jogo

```text
INÍCIO
  │  pontos = 0, rodada = 1          ← estado inicial
  ▼
┌─► Ainda há perguntas? ──não──► mostrar resultado final → FIM
│        │ sim
│        ▼
│   mostrar pergunta + opções
│        ▼
│   ler resposta do jogador          ← ENTRADA
│        ▼
│   resposta == correta? ──sim──► pontos += 1
│        │ não                   (estado muda)
│        ▼
│   dar feedback
│        ▼
└── rodada += 1
```
 
**Entradas**
- Nome do jogador.
- Resposta de cada pergunta (uma letra entre `a` e `d`).
- Confirmação (`s`/`n`) para jogar novamente.

**Regras principais**
- O jogo tem **3 rodadas** com **5 perguntas** cada (15 no total), sorteadas de um banco de 20 perguntas, sem repetição na mesma partida.
- Cada pergunta tem 4 opções, embaralhadas a cada exibição.
- Cada acerto vale **10 pontos**. A partir de **3 acertos seguidos**, cada acerto ganha **+5 de bônus**. Errar zera a sequência.
- Respostas inválidas são rejeitadas e a leitura é repetida.

- **Resultados esperados**
- Feedback imediato após cada resposta (acertou/errou e qual era a correta).
- Resumo ao fim de cada rodada.
- Resultado final: acertos, erros, percentual, maior sequência, pontuação e classificação.
- Recorde da sessão quando o jogador joga mais de uma partida.

- 
## 2. Como executar
 
**Requisitos:** Python 3.8 ou superior. Nenhuma biblioteca externa (usa apenas o módulo `random` da biblioteca padrão).
 
```bash
git clone <link-do-repositorio>
cd <pasta-do-repositorio>
python quiz.py        # no Linux/macOS pode ser python3 quiz.py
```
 
Para encerrar a qualquer momento: `Ctrl + C`.

## 3. Explicação da solução
 
O programa é organizado como uma **sequência de instruções** que altera o **estado** (variáveis) ao longo da execução. A execução começa em `main()`, que chama `jogar_partida()`, que chama `jogar_rodada()`, que chama `fazer_pergunta()`.

### Elementos do paradigma imperativo no código
 
| Elemento | Onde aparece | O que faz |
| --- | --- | --- |
| **Sequência de instruções** | `main()`, `jogar_partida()`, `fazer_pergunta()` | Os comandos executam em ordem: exibir pergunta → ler resposta → verificar → atualizar pontos → mostrar feedback. |
| **Variáveis e atribuições (estado)** | `criar_estado()` e `atualizar_estado()` | O dicionário `estado` guarda `pontuacao`, `acertos`, `erros`, `sequencia` e `melhor_sequencia`. A cada resposta, ele é alterado por atribuições, como `estado["acertos"] = estado["acertos"] + 1`. |
| **Decisões (`if / elif / else`)** | `atualizar_estado()`, `classificar()`, `fazer_pergunta()` | Decide se houve acerto, se vale bônus, se bate o recorde e qual classificação o jogador recebe. |
| **Repetição com `while`** | `pedir_nome()`, `ler_letra()`, `perguntar_sim_nao()`, `jogar_rodada()`, `main()` | Repete a leitura até a entrada ser válida; percorre as perguntas da rodada; mantém o jogo rodando enquanto o jogador quiser. |
| **Repetição com `for`** | `jogar_partida()`, `fazer_pergunta()` | Percorre as rodadas e imprime as opções de resposta. |
| **Funções / procedimentos** | Todo o arquivo | Dividem o problema em partes pequenas, cada uma com uma responsabilidade. |

### Exemplo de alteração de estado
 
Em uma partida, `sequencia` e `pontuacao` evoluem assim:
 
| Resposta | `sequencia` | Pontos ganhos | `pontuacao` |
| --- | --- | --- | --- |
| acerto | 1 | 10 | 10 |
| acerto | 2 | 10 | 20 |
| acerto | 3 | 10 + 5 | 35 |
| erro | 0 | 0 | 35 |
 
Uma partida perfeita (15 acertos) rende 10×15 + 5×13 = **215 pontos**.

### Decisões de implementação
 
- **Dicionário `estado` passado para as funções:** as funções alteram o mesmo dicionário, o que deixa visível como o estado muda ao longo do processamento.
- **Banco com a primeira opção sempre correta:** simplifica o cadastro de perguntas. As opções são embaralhadas em `preparar_opcoes()`, que trabalha sobre uma **cópia** da lista para não alterar o banco original.
- **`random.sample`:** garante que nenhuma pergunta se repete dentro da mesma partida.
- **Constantes no topo do arquivo:** mudar o número de rodadas, perguntas ou pontos exige alterar apenas um valor.

- ## 4. Reflexão sobre o desenvolvimento
 
<!-- Ajuste este trecho com a experiência real do grupo antes de entregar. -->
 
**Principais decisões:** usar apenas a biblioteca padrão; separar o programa em funções pequenas; centralizar o estado da partida em um único dicionário; validar toda entrada do usuário com laços `while`.
 
**Dificuldades:** embaralhar as opções sem perder a informação de qual é a correta; garantir que o bônus de sequência fosse calculado antes de somar à pontuação; tratar entradas inválidas sem encerrar o programa.
 
**Possíveis melhorias:** carregar as perguntas de um arquivo (JSON ou CSV); salvar um ranking de pontuações em arquivo; criar níveis de dificuldade e temas; adicionar limite de tempo por pergunta; escrever testes automatizados para `atualizar_estado()`.

## 5. Contribuição dos integrantes
 
| Integrante | Contribuição |
| --- | --- |
| _Seu nome aqui_ | _Descreva a sua participação._ |

## 6. Estrutura do repositório
 
```
.
├── quiz.py     # código-fonte completo
└── README.md   # este arquivo
```













