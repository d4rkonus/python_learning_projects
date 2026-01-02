#!/usr/bin/python3

class Games:
    def __init__(self, title, price, console):
        self.__title = title
        self._price = price
        self.console = console

    def new_price(self, new_price):
        if new_price < 0:
            print("The price cannot be negative.")
            return

        if new_price > self._price:
            print(f"{self.__title} - (Price increase detected!)")
            print(f"\n- [!] Real price: {self._price}€, Offered price: {new_price}€")
            print(f"\n- [+] The difference of the increase is: {new_price - self._price}€")
        else:
            print("The game has the correct price!")
            self._price = new_price
            print(f"{self.__title} The game has the correct price! New price: {self._price}€")
        
    def game_info(self):
        print(f"\nWe have this game available:")
        print(f"[+] Title: {self.__title}")
        print(f"[+] Price: {self._price}€")
        print(f"[+] Console: {self.console}")


game_1 = Games(f"The Legend of Zelda: Breath of the Wild", 59.99, "Nintendo Switch")
game_2 = Games(f"God of War Ragnarok", 49.99, "PlayStation 5")
game_3 = Games(f"Halo Infinite", 39.99, "Xbox Series X")

for game in (game_1, game_2, game_3):
    game.game_info()
#    game.new_price(100.00)
