class Player:
    def __init__(self, speed, stamina, power, accuracy):
        self.speed = speed
        self.stamina = stamina
        self.power = power
        self.accuracy = accuracy

class Goalkeeper(Player):
    def __init__(self, speed, stamina, power, accuracy):
        super().__init__(speed, stamina, power, accuracy)
    def keep_goal(self):
        print('What a save!! ')

class Defender(Player):
    def __init__(self, speed, stamina, power, accuracy):
        super().__init__(self, speed, stamina, power, accuracy)

    def ball(self):
        print('took the ball ')

class Midfielder(Player):
    def __init__(self, speed, stamina, power, accuracy):
        super().__init__(speed, stamina, power, accuracy)

    def secure(self):
        print('started counter-attack ')

class Winger(Player):
    def __init__(self, speed, stamina, power, accuracy, ):
        super().__init__(speed, stamina, power, accuracy)

    def goal(self):
        print('What a Brilliant goal!!!! ')

f1 = Winger(Player)
print(f1.goal)


