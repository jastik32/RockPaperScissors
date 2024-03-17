import random


def game():
    while True:
        
        choose = random.randint(1, 3)
        user_choose = input("Сделайте выбор: ")
        possible_actions = ["камень", "ножницы", "бумага"]
        computer_action = random.choice(possible_actions)

        print(f"\nВы выбрали {user_choose}, компьютер выбрал {computer_action}.\n")

        if user_choose == computer_action:
            print(f"Оба пользователя выбрали {user_choose}. Ничья!!")

        elif user_choose == "камень":
            if computer_action == "ножницы":
                print("Камень бьет ножницы! Вы победили!")
            else:
                print("Бумага оборачивает камень! Вы проиграли")

        elif user_choose == "бумага":
            if computer_action == "камень":
                print("Бумага оборачивает камень! Вы победили!")
            else:
                print("Ножницы режут бумагу! Вы проиграли.")

        elif user_choose == "ножницы":
            if computer_action == "бумага":
                print("Ножницы режут бумагу! Вы победили!")
            else:
                print("Камень бьет ножницы! Вы проиграли.")

        print(f"=" * 50)


game()
