# =============================================================================
#                                 Points Constants
# =============================================================================


def init_points():

    # Positive Points

    goal_base = 3                                   # Goal points for attackers (midfielder += 1, defender += 2)
    scoring_more_than_single_goal = 1               # Bonus every goal scored after more than a single goal
    assist = 3                                      # Assist bonus
    get_penalty = 3                                 # Cause penalty
    stop_penalty = 4                                # Stop penalty
    play = 1                                        # Play less than 60 minutes
    play_60_minutes = 2                             # Play more than 60 minutes
    play_120_minutes = 3                            # Play full time + extra time
    defence_clean_sheet = 4                         # Goalie\Defender who keeps clean sheet
    midfield_clean_sheet = 1                        # Midfielder who keeps clean sheet
    passing_accuracy_above_85_percent = 1           # Bonus for passing accuracy


    positive_points = [goal_base, scoring_more_than_single_goal, assist, get_penalty, stop_penalty,
                       play, play_60_minutes, play_120_minutes, defence_clean_sheet, midfield_clean_sheet,
                       passing_accuracy_above_85_percent]


    # Negative Points

    yellow_card = -1
    red_card = -3
    concede_2_goals = -2
    own_goal = -4


    negative_points = [yellow_card, red_card, concede_2_goals, own_goal]
