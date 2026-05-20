import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ace= cards[0]

start=True
while start:
    user_cards = []
    dealer_cards = []
    choose_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choose_to_play == "n":
        print("Ok. Next Time!")
        start= False
    else:
        print("\n"*20)
        print(art.logo)
        user_cards.append(random.choice(cards))
        another_card= True
        while another_card:
            user_cards.append(random.choice(cards))
            user_sum = sum(user_cards)
            if ace in user_cards:
                if user_sum>21:
                    user_sum= user_sum-10
            print(f"Your cards:{user_cards}, current score: {user_sum}")

            dealer_sum= sum(dealer_cards)
            while dealer_sum<17:
                dealer_cards.append(random.choice(cards))
                dealer_sum = sum(dealer_cards)
            print(f"Computer's first card: {dealer_cards[0]}")

            def final_output():
                print(f"Your final hand: {user_cards}, final score: {user_sum}")
                print(f"Computer's final hand: {dealer_cards}, final score: {dealer_sum}")
                if user_sum > 21:
                    print("You went over. You lose!")
                elif dealer_sum > 21:
                    print("Opponent went over. You win!")
                elif dealer_sum > user_sum:
                    print("You lose.")
                elif dealer_sum < user_sum:
                    print("You win!")
                elif dealer_sum == user_sum:
                    print("It's a Draw.")

            if user_sum > 21:
                final_output()
                another_card= False

            else:
                shall_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if shall_continue=="n":
                    final_output()
                    another_card= False



