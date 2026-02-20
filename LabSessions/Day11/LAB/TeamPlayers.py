class Player:
    def __init__(self, name):
        self.name = name
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)
    def show_players(self):
        print("Team:", self.name)
        for p in self.players:
            print(p.name)
p1 = Player("Ishan")
p2 = Player("Tilak")
team = Team("India")
team.add_player(p1)
team.add_player(p2)
team.show_players()
