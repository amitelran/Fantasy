# =============================================================================
#                               Team Class
# =============================================================================


class Team:

    def __init__(self, team_name, goalkeeper, defenders, midfielders, attackers):

        self.team_name = team_name
        self.goalkeeper = goalkeeper
        self.defenders = defenders
        self.midfielders = midfielders
        self.attackers = attackers


    # Print Team data

    def print_team(self):
        print("\n***")
        print("Team Name: %s " % self.team_name)

        print("")
