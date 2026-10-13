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

https://github.com/user-attachments/assets/9c1a3167-1fce-4e6b-a60c-0147dd5ac742

## 1. Descrição do problema
 
Criamos um jogo de perguntas e respostas (quiz) executado no terminal, com pontuação, controle de rodadas e apresentação do resultado final. O jogador se identifica, responde perguntas de múltipla escolha sobre programação e computação e, ao final, recebe um resumo do desempenho.

## Fluxo do Jogo

```text
INÍCIO
  │  pedir nome, recorde = 0
  ▼
┌─► Nova partida: estado zerado (pontos = 0, acertos = 0, erros = 0, sequência = 0)
│   sortear 15 perguntas sem repetição
│        ▼
│   ┌─► Para cada rodada (1 a 3)
│   │     ▼
│   │   ┌─► Para cada pergunta da rodada (5)
│   │   │     ▼
│   │   │   embaralhar opções → mostrar pergunta
│   │   │     ▼
│   │   │   ler resposta (repete até ser válida)      ← ENTRADA
│   │   │     ▼
│   │   │   acertou? ──sim──► acertos += 1, sequência += 1
│   │   │     │               pontos += 10 (+5 se sequência ≥ 3)
│   │   │     │ não           (o estado muda)
│   │   │     ▼
│   │   │   erros += 1, sequência = 0
│   │   │     ▼
│   │   │   mostrar feedback
│   │   └───────┘ (próxima pergunta)
│   │     ▼
│   │   resumo da rodada
│   └───────┘ (próxima rodada)
│        ▼
│   resultado final + classificação
│        ▼
│   atualizar recorde da sessão
│        ▼
└── jogar novamente? ──sim──┘
         │ não
         ▼
        FIM
```
 
**Entradas**
- Nome do jogador.
- Resposta de cada pergunta (uma letra entre `a` e `d`).
- Confirmação (`s`/`n`) para jogar novamente.
- Enter para avançar entre as rodadas.

**Regras principais**
- O jogo tem **3 rodadas** com **5 perguntas** cada (15 no total), sorteadas de um banco de 50 perguntas, sem repetição na mesma partida.
- Cada pergunta tem 4 opções, embaralhadas a cada exibição.
- Cada acerto vale **10 pontos**. A partir de **3 acertos seguidos**, cada acerto ganha **+5 de bônus**. Errar zera a sequência.
- Respostas inválidas (nome vazio, letra fora de a–d, resposta diferente de s/n) são rejeitadas e a leitura é repetida.

**Resultados esperados**
- Feedback imediato após cada resposta (acertou/errou e qual era a correta).
- Resumo ao fim de cada rodada (acertos da rodada e pontuação atual).
- Resultado final: acertos, erros, percentual, maior sequência de acertos, pontuação e classificação.
- Recorde da sessão quando o jogador joga mais de uma partida.

## 2. Como executar
 
**Requisitos:**
- Python 3.8 ou superior.
- Nenhuma biblioteca externa: o programa usa apenas módulos da biblioteca padrão (`random`, `sys`, `time` e `os`).
- Um terminal com suporte a cores ANSI (Windows 10 ou superior, Linux e macOS já suportam).

```bash
git clone https://github.com/oberlimm/Jogo-de-perguntas-e-respostas.git
cd Jogo-de-perguntas-e-respostas
python PyQuest-0N.py        # no Linux/macOS pode ser python3 PyQuest-0N.py
```
 
Para encerrar a qualquer momento: `Ctrl + C`.

## 3. Explicação da solução
 
O programa é organizado como uma **sequência de instruções** que altera o **estado** (variáveis) ao longo da execução. A execução começa em `main()`, que chama `jogar_partida()`, que chama `jogar_rodada()`, que chama `fazer_pergunta()`.

### Elementos do paradigma imperativo no código
 
| Elemento | Onde aparece | O que faz |
| --- | --- | --- |
| **Sequência de instruções** | `main()`, `jogar_partida()`, `fazer_pergunta()` | Os comandos executam em ordem: exibir pergunta → ler resposta → verificar → atualizar pontos → mostrar feedback. |
| **Variáveis e atribuições (estado)** | `criar_estado()` e `atualizar_estado()` | O dicionário `estado` guarda `pontuacao`, `acertos`, `erros`, `sequencia` e `melhor_sequencia`. A cada resposta, ele é alterado por atribuições, como `estado["acertos"] = estado["acertos"] + 1`. |
| **Decisões (`if / elif / else`)** | `atualizar_estado()`, `classificar()`, `fazer_pergunta()`, `main()` | Decide se houve acerto, se vale bônus, qual classificação o jogador recebe e se bateu o recorde (em `main()`). |
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

### Interface no terminal

Além da lógica do jogo, a versão final conta com recursos visuais que não alteram as regras:
- Cores ANSI para destacar acertos (verde), erros (vermelho), perguntas (amarelo) e resultados (ciano/azul).
- Efeito de digitação na função `digitar()`, que exibe os textos caractere por caractere.
- Limpeza de tela na função `limpar_tela()`, que usa `cls` no Windows e `clear` nos demais sistemas.
  

## 4. Reflexão sobre o desenvolvimento
 
**Principais decisões:** usar apenas a biblioteca padrão; separar o programa em funções pequenas; centralizar o estado da partida em um único dicionário; validar toda entrada do usuário com laços while; começar por uma versão simples no terminal (rascunho) e só depois adicionar cores e efeito de digitação.
 
**Dificuldades:** embaralhar as opções sem perder a informação de qual é a correta; garantir que o bônus de sequência fosse calculado antes de somar à pontuação; tratar entradas inválidas sem encerrar o programa; manter as cores funcionando no terminal do Windows.
 
**Possíveis melhorias:** carregar as perguntas de um arquivo (JSON ou CSV); salvar um ranking de pontuações em arquivo; criar níveis de dificuldade e temas; adicionar limite de tempo por pergunta; escrever testes automatizados para atualizar_estado().

## 5. Contribuição dos integrantes
 
| Integrante | Contribuição |
| --- | --- |
|_João Oberlim Lira Martins_|Fazer a estrutura do Quiz, Melhoria do Codigo |
| _Pedro Lucas da Silva Goulart_ |Contribuição com ajuste do Codigo , Criação do Video |
| _Germano Pedro Minami Rodrigues_ |Adicionar Perguntas , Deixou o Codigo mais clean(limpo)|


## 6. Estrutura do repositório
 
```
.
├── PyQuest-0N.py   # código-fonte completo
└── README.md       # este arquivo
```













