class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket- player: {self.__player}, score: {self.__score}")

    def play(self):
        print(f"{self.__player} makes a CENTURY.")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score>=0:
           self.__score = new_score
           print(f"Score updated to {self.__score}")
        else:
           print("Score cannot be negative.")
class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football- player: {self.__player}, score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a GOAL!!")

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        if new_score>=0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")

cricket = Cricket("Abhishek Sharma", 141)
football = Football("Lionel Messi", 3)

print("=== Sports Scorecard=== /n")
for sports in(cricket, football):
    sports.info()
    sports.play()
    print()

print("--- direct change attempt---")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score()}")

print("/n--- Updating scores ---")
cricket.set_score(150)
football.set_score(5)