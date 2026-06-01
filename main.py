from texasholdem import Card
from texasholdem.evaluator import evaluate, rank_to_string
import os


def main(hole_cards, cartas_user, fase_key):
    if fase_key == "1":
        card1 = max(hole_cards[0].rank, hole_cards[1].rank)
        card2 = min(hole_cards[0].rank, hole_cards[1].rank)
        suited = hole_cards[0].suit == hole_cards[1].suit
        pair = card1 == card2

        score = card1 + card2
        if pair:
            score += 10
        if suited:
            score += 3
        if card1 - card2 <= 1:
            score += 2
        if card1 - card2 <= 2:
            score += 1
        if card1 - card2 > 4:
            score -= 1
        if card1 < 5:
            score -=3
        if pair:
            percentual = min(round((score/39) * 100), 100)
        if not pair:
            percentual = min(round((score/28) * 100), 100)



        if (pair and card1 >= 10) or (card1 == 12 and card2 == 11) or (card1 == 12 and card2 == 10):
            os.system('cls')
            print(f"{' '.join(cartas_user)} é uma mão extremamente boa!")
            print("Recomendo RAISE alto, mas tenha cuidado.")
            print("Para evitar que os jogadores 'foldem', não seja extremamente agressivo")
            print(f"Equidade estimada: {percentual}%")
        elif (pair and card1 <= 9 and card1 >= 5) or (not suited and card1 == 12 and card2 == 10):
            os.system('cls')
            print(f"{' '.join(cartas_user)} é uma mão forte!")
            print("Recomendo RAISE não agressivo, mas tenha cuidado.")
            print("Sua mão pode ser neutralizada de forma relativamente fácil.")
            print(f"Equidade estimada: {percentual}%")
        elif (not suited and card1 == 12 and card2 == 9) or (suited and card1 == 11 and card2 == 10):
            os.system('cls')
            print(f"{' '.join(cartas_user)} é uma mão forte!")
            print("Recomendo RAISE não agressivo, mas tenha cuidado.")
            print("Sua mão pode ser neutralizada de forma relativamente fácil.")
            print(f"Equidade estimada: {percentual}%")
        elif (pair and card1 >=0 and card1 <= 4) or (suited and card1 + card2 >= 19) or (suited and card1 >=4 and card1 <= 7 and card1 - card2 <= 2):
            os.system('cls')
            print(f"{' '.join(cartas_user)} é uma mão forte!")
            print("Recomendo apenas fazer o CALL.")
            print("É uma mão forte, mas não o suficiente para RAISE")
            print(f"Equidade estimada: {percentual}%")
        elif (not suited and card1 + card2 >= 19 and card1 !=12) or (suited and card1 - card2 <= 2 and card1 >= 1 and card1 <= 3):
            os.system('cls')
            print(f"{' '.join(cartas_user)} é uma mão relativamente forte!")
            print("Recomendo apenas fazer o CALL caso esteja em um posição boa.")
            print("Ex: Button, Cutoff ou Hijack (ou seja, posições tardias)")
            print("É uma mão boa, mas não o suficiente para CALL de qualquer forma")
            print(f"Equidade estimada: {percentual}%")
        else:
            os.system('cls')
            print(f"{' '.join(cartas_user)} é NÃO é uma mão boa!")
            print("Recomendo fazer o FOLD")
            print("É uma mão péssima")
            print(f"Equidade estimada: {percentual}%")
    elif fase_key == "2":
        os.system('cls')
        while True:
            mesa_cards = input("Na mesma notação, escreva as 3 cartas comunitárias: ").split()
            try:
                table_cards = [Card(c) for c in mesa_cards]
                if len(table_cards) == 3:
                    break
                else:
                    print("Digite exatamente 3 cartas, tente novamente.")
            except ValueError:
                print("Mesa inválida! Tente novamente.")
        rank = evaluate(cards=hole_cards, board=table_cards)
        evaluation = round((1 - rank / 7462) * 100, 2)
        tipo_mao = rank_to_string(rank)
    
        if rank <= 300:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num flop como esse é uma mão fortissima!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo um BET agressivo, mas cuidado para não assustar outros players")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 1000:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num flop como esse é uma mão forte!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo um BET moderado, mas cuidado, pode ter alguém com mão melhor")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 2500:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num flop como esse é uma mão mediana!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo fazer o CALL ou um BET baixo, mas cuidado, não pague bets muito caras.")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 4500:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num flop como esse é uma mão relativamente fraca!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo fazer o CHECK ou um CALL baixo, mas cuidado, provavelmente tem alguém melhor.")
            print(f"O tipo da sua mão é {tipo_mao}")
        else:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num flop como esse é uma mão pessima!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo fazer o FOLD na maioria das situações, a não ser que sejam cartas muito altas.")
            print(f"O tipo da sua mão é {tipo_mao}")
    elif fase_key == "3": 
        os.system('cls')
        while True:
            mesa_cards = input("Na mesma notação, escreva as 4 cartas comunitárias: ").split()
            try:
                table_cards = [Card(c) for c in mesa_cards]
                if len(table_cards) == 4:
                    break
                else:
                    print("Digite exatamente 4 cartas, tente novamente.")
            except ValueError:
                print("Mesa inválida! Tente novamente.")

        rank = evaluate(cards=hole_cards, board=table_cards)
        evaluation = round((1 - rank / 7462) * 100, 2)
        tipo_mao = rank_to_string(rank)
    
        if rank <= 300:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num turn como esse é uma mão fortissima!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo um BET agressivo, mas cuidado para não assustar outros players")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 1000:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num turn como esse é uma mão forte!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo um BET moderado, mas cuidado, pode ter alguém com mão melhor")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 2500:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num turn como esse é uma mão mediana!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo fazer o CALL ou um BET baixo, mas cuidado, não pague bets muito caras.")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 4500:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num turn como esse é uma mão relativamente fraca!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo fazer o CHECK ou um CALL baixo, mas cuidado, provavelmente tem alguém melhor.")
            print(f"O tipo da sua mão é {tipo_mao}")
        else:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num turn como esse é uma mão pessima!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo fazer o FOLD na maioria das situações, a não ser que sejam cartas muito altas.")
            print(f"O tipo da sua mão é {tipo_mao}")
    elif fase_key == "4":

        os.system('cls')
        while True:
            mesa_cards = input("Na mesma notação, escreva as 5 cartas comunitárias: ").split()
            try:
                table_cards = [Card(c) for c in mesa_cards]
                if len(table_cards) == 5:
                    break
                else:
                    print("Digite exatamente 5 cartas, tente novamente.")
            except ValueError:
                print("Mesa inválida! Tente novamente.")

        rank = evaluate(cards=hole_cards, board=table_cards)
        evaluation = round((1 - rank / 7462) * 100, 2)
        tipo_mao = rank_to_string(rank)
    
        if rank <= 300:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num river como esse é uma mão fortissima!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo um BET agressivo — essa é sua mão final, extraia o máximo valor do pot!")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 1000:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num river como esse é uma mão forte!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo um BET moderado — é sua última chance de ganhar valor, não deixe barato.")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 2500:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num river como esse é uma mão mediana!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo CHECK — sem espaço para melhora, não arrisque fichas com mão mediocre.")
            print(f"O tipo da sua mão é {tipo_mao}")
        elif rank <= 4500:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num river como esse é uma mão fraca!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo FOLD se houver qualquer bet — não há mais cartas para salvar sua mão.")
            print(f"O tipo da sua mão é {tipo_mao}")
        else:
            os.system('cls')
            print(f"{' '.join(cartas_user)} num river como esse é uma mão péssima!")
            print(f"Seu percentual de força estimado é {evaluation}%")
            print("Recomendo FOLD — só continue se puder fazer um bluff convincente.")
            print(f"O tipo da sua mão é {tipo_mao}")

    
os.system('cls')
print("╔══════════════════════════════════════╗")
print("║   🃏  TEXAS HOLD'EM ADVISOR  🃏      ║")
print("╠══════════════════════════════════════╣")
print("║                                      ║")
print("║   Como escrever suas cartas:         ║")
print("║   Ranks:  2 3 4 5 6 7 8 9 T J Q K A  ║")
print("║   Naipes: h=♥  d=♦  c=♣  s=♠         ║")
print("║                                      ║")
print("║   Exemplos:  As = Ás de espadas      ║")
print("║              Kh = Rei de copas       ║")
print("║              Td = 10 de ouros        ║")
print("║                                      ║")
print("║      Escreva as cartas SEPARADAS     ║")
print("║   Exemplo: As Kh                     ║")
print("║                                      ║")
print("╚══════════════════════════════════════╝")

while True:
    cartas_user = input("Digite as suas cartas na notação descrita acima: ").split()
    try:
        hole_cards = [Card(c) for c in cartas_user]
        break
    except ValueError:
        print("Carta inválida! Tente novamente.")

os.system('cls')
fases = {"1": "PRE-FLOP", "2": "FLOP", "3": "TURN", "4": "RIVER"}
print("Qual é a fase atual?")
for k, v in fases.items():
    print(f"  {k}. {v}")
fase_key = input("Fase (1-4): ").strip()
fase = fases.get(fase_key, "FLOP")

main(hole_cards, cartas_user, fase_key)