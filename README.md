<div align="center">

  <h1>🃏 Poker Advisor</h1>

  <p>
    <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge" alt="Status"/>
  </p>

  <p>Assistente inteligente de Texas Hold'em rodando no terminal. Analisa suas cartas e recomenda a melhor jogada em cada fase da mão.</p>

</div>

---

## Sobre o projeto

O programa recebe as suas cartas na mão e a fase atual da rodada, analisa a força da mão e retorna uma recomendação estratégica com o percentual de força estimado. No **Pre-Flop**, usa um sistema de score próprio. No **Flop**, **Turn** e **River**, utiliza a biblioteca `texasholdem` para calcular o rank real da mão (de 1 a 7462) e converte em percentual.

---

## Como funciona

1. O usuário digita as **2 cartas da mão** na notação padrão (ex: `As Kh`).
2. Escolhe a **fase atual** da rodada (Pre-Flop, Flop, Turn ou River).
3. Se necessário, informa as **cartas comunitárias** da mesa.
4. O programa avalia a força da mão e exibe a **recomendação de jogada** com explicação estratégica.

---

## Fases suportadas

| # | Fase     | Cartas comunitárias necessárias |
|---|----------|---------------------------------|
| 1 | Pre-Flop | Nenhuma                         |
| 2 | Flop     | 3 cartas                        |
| 3 | Turn     | 4 cartas                        |
| 4 | River    | 5 cartas                        |

---

## Recomendações possíveis

| Força da mão | Recomendação     |
|--------------|------------------|
| Fortíssima   | BET / RAISE agressivo |
| Forte        | BET / RAISE moderado  |
| Mediana      | CALL / BET baixo      |
| Fraca        | CHECK / CALL baixo    |
| Péssima      | FOLD                  |

---

## Notação das cartas

```
╔══════════════════════════════════════╗
║   🃏  TEXAS HOLD'EM ADVISOR  🃏      ║
╠══════════════════════════════════════╣
║                                      ║
║   Como escrever suas cartas:         ║
║   Ranks:  2 3 4 5 6 7 8 9 T J Q K A  ║
║   Naipes: h=♥  d=♦  c=♣  s=♠         ║
║                                      ║
║   Exemplos:  As = Ás de espadas      ║
║              Kh = Rei de copas       ║
║              Td = 10 de ouros        ║
║                                      ║
║      Escreva as cartas SEPARADAS     ║
║   Exemplo: As Kh                     ║
║                                      ║
╚══════════════════════════════════════╝
```

---

## Tecnologias utilizadas

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/texasholdem-Library-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/os-Built--in-blue?style=flat-square"/>
</p>

---

## Como executar

**Pré-requisitos:** Python 3.x instalado.

```bash
# Clone o repositório
git clone https://github.com/Eduardo-Nicolete37/Poker_Advisor.git
cd Poker_Advisor

# Instale a dependência
pip install texasholdem

# Execute
python main.py
```

---

## Autor

**Eduardo Nicolete**

[![GitHub](https://img.shields.io/badge/GitHub-Eduardo--Nicolete37-181717?style=flat-square&logo=github)](https://github.com/Eduardo-Nicolete37)

---

<div align="center">
  <sub>Feito com 🐍 e dedicação para aprender Python na prática.</sub>
</div>
