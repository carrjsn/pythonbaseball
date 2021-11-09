
"""
Python Baseball Simulator
by Jason C.

"""

import random
import time


def main():

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("Welcome to Python Baseball!")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    time.sleep(1.5)

    home_team = input("Enter the home team: ")
    away_team = input("Enter the away team: ")

    num_innings = int(input("Enter the number of innings you would like to play: "))

    max_off = input('Enter "yes" for maximum offense or "no" for more realistic scoring: ')
    print("")

    # initialize game stats - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    home_team_batting_avg = 0
    away_team_batting_avg = 0

    # strikeouts[0] walks[1] errors[2] home-runs[3] runs[4] hits[5] at-bats[6] doubles[7] triples[8]
    home_team_stat_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    away_team_stat_totals = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    home_team_lead = 0  # for walk-off scenario

    # for tracking runs per inning and printing out at end
    away_boxscore = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    home_boxscore = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    side = "top"
    time.sleep(1)
    print("Today the " + home_team + " host the " + away_team)
    time.sleep(2)
    print("Lets play ball!!")
    print(". . . . . . . . . . . . . . . . . . .")
    time.sleep(2.5)

    # MAIN LOOP - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    for i in range(num_innings):

        # top of inning  (AWAY TEAM Batting) - - - - -
        announce_inning(i, side, away_team, home_team)

        # "previous game runs total", for subtracting later to get runs scored in inning
        prev_run = away_team_stat_totals[4]

        # main half-inning loop (simulate half inning and get stats)
        half_inning_stats = half_inning(i, home_team_lead, side, num_innings, max_off)

        # adding inning stats to game totals
        away_team_stat_totals = update_stats(half_inning_stats, away_team_stat_totals)
        away_team_batting_avg = away_team_stat_totals[5] / away_team_stat_totals[6]  # batting avg

        # add runs scored in inning to boxscore for end of game display
        away_boxscore[i + 1] = half_inning_stats[4]

        # home_team runs - away_team runs (for walk-off)
        home_team_lead = home_team_stat_totals[4] - away_team_stat_totals[4]

        # check if bottom 9th necessary
        if i == (num_innings - 1) and home_team_lead > 0:
            break

        # end of side
        print("That's the end of the side")
        time.sleep(1.5)
        # old total runs - previous total
        print("The " + away_team + " scored " + str(away_team_stat_totals[4] - prev_run) + " runs")
        time.sleep(1.5)
        print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
        print("The score is the " + away_team + ": " + str(away_team_stat_totals[4]))
        print(home_team + ": " + str(home_team_stat_totals[4]))
        print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
        time.sleep(3)

        # bottom of inning (HOME TEAM batting) - - - - - - -
        side = "bottom"
        announce_inning(i, side, away_team, home_team)

        # for calculating runs per inning
        prev_run = home_team_stat_totals[4]

        # main half-inning loop (simulate half inning and get stats)
        half_inning_stats = half_inning(i, home_team_lead, side, num_innings, max_off)

        # adding inning stats to game totals
        home_team_stat_totals = update_stats(half_inning_stats, home_team_stat_totals)
        home_team_batting_avg = home_team_stat_totals[5] / home_team_stat_totals[6]      # batting avg

        # add runs scored in inning to boxscore for end of game display
        home_boxscore[i + 1] = half_inning_stats[4]

        # skip 'end of inning' text and go to 'end of game' text
        if i == (num_innings - 1):
            break

        # end of inning
        print("That's the end of the inning")
        time.sleep(1.5)
        print("The " + home_team + " scored " + str(home_team_stat_totals[4] - prev_run) + " runs")
        time.sleep(1.5)
        print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
        print("The score is the " + away_team + ": " + str(away_team_stat_totals[4]))
        print(home_team + ": " + str(home_team_stat_totals[4]))
        print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
        side = "top"
        time.sleep(4.5)

    # end of game
    time.sleep(2)
    print("")
    print("That's the end of the ballgame!")
    print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
    time.sleep(1.5)
    print("The final score is the " + away_team + ": " + str(away_team_stat_totals[4]))
    print(home_team + ": " + str(home_team_stat_totals[4]))
    print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
    time.sleep(2)

    away_team_batting_avg = get_str_average(away_team_batting_avg)
    home_team_batting_avg = get_str_average(home_team_batting_avg)

    # show boxscore
    make_boxscore(away_team, home_team, away_boxscore, home_boxscore, away_team_stat_totals, home_team_stat_totals)

    # show team stats
    print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
    time.sleep(1.5)
    print(away_team + " hitting: " + str(away_team_stat_totals[3]) + " HR | " + str(away_team_stat_totals[7]) + " 2B | "
          + str(away_team_stat_totals[8]) + " 3B | " + away_team_batting_avg[1:5] + " AVG")  # opposite team for errors
    print(home_team + " hitting: " + str(home_team_stat_totals[3]) + " HR | " + str(home_team_stat_totals[7]) + " 2B | "
          + str(home_team_stat_totals[8]) + " 3B | " + home_team_batting_avg[1:5] + " AVG")  # opposite team for errors
    print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")
    time.sleep(1.5)
    # pitching stats have home/away stats flipped because strikeouts/walks count towards opposite team
    print(away_team + " pitching: " + str(home_team_stat_totals[0]) + " strikeouts |  " +
          str(home_team_stat_totals[1]) + " walks")
    print(home_team + " pitching: " + str(away_team_stat_totals[0]) + " strikeouts | " +
          str(away_team_stat_totals[1]) + " walks")
    print(" . . . . . . . . . . . . . . . . . . . . . . . . . .")

    print("")
    time.sleep(1.5)
    print("Thanks for playing Python Baseball!")
    print("")


# HELPER FUNCTIONS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def make_boxscore(away, home, away_box, home_box, away_stats, home_stats):
    print("                       1   2   3   4   5   6   7   8   9   |  R   H   E")
    print('{:20}'.format(away) + " | " + str(away_box[1]) + "   " + str(away_box[2]) + "   " + str(away_box[3]) +
          "   " + str(away_box[4]) + "   " + str(away_box[5]) + "   " + str(away_box[6]) + "   " + str(away_box[7]) +
          "   " + str(away_box[8]) + "   " + str(away_box[9]) + "   |  " + str(away_stats[4]).ljust(4) +
          str(away_stats[5]).ljust(4) + str(home_stats[2]).ljust(4))
    print('{:20}'.format(home) + " | " + str(home_box[1]) + "   " + str(home_box[2]) + "   " + str(home_box[3]) +
          "   " + str(home_box[4]) + "   " + str(home_box[5]) + "   " + str(home_box[6]) + "   " + str(home_box[7]) +
          "   " + str(home_box[8]) + "   " + str(home_box[9]) + "   |  " + str(home_stats[4]).ljust(4) +
          str(home_stats[5]).ljust(4) + str(away_stats[2]).ljust(4))

def update_stats(inning_stats, team_stat_totals):

    for i in range(len(team_stat_totals)):
        team_stat_totals[i] += inning_stats[i]

    return team_stat_totals

# making bat avg string and adding 0s if less than 3 decimal points
def get_str_average(batting_avg):
    if (batting_avg * 1000) % 10 == 0:
        avg = str(batting_avg)
        result = avg + "00"
        return result
    else:
        return str(batting_avg)


# hit percentages
def at_bat(isMax):
    num = random.randint(1, 100)

    if isMax.lower() == 'no':
      if num <= 2:
          return "triple"
      elif 2 < num <= 6:
          return "homerun"
      elif 6 < num <= 11:
          return "double"
      elif 11 < num <= 28:
          return "single"
      elif 28 < num <= 33:
          return "walk"
      elif 33 < num <= 34:
          return "hit by pitch"
      elif 34 < num <= 35:
          return "error"
      else:
          return "out"

    # more offense - - -
    else:
      if num <= 2:
          return "triple"
      elif 2 < num <= 7:
          return "homerun"
      elif 7 < num <= 13:
          return "double"
      elif 13 < num <= 38:
          return "single"
      elif 38 < num <= 43:
          return "walk"
      elif 43 < num <= 44:
          return "hit by pitch"
      elif 44 < num <= 45:
          return "error"
      else:
          return "out"


def half_inning(i, home_lead, side, num_innings, max_off):   # parameters only exist for walk-off case
    outs = 0
    base_runners = [0, 0, 0, ' the bases empty >>']  # or [0, 0, 0, '']  w/ empty string

    # stats that are returned
    runs_scored_in_inning = 0
    hits_in_inning = 0
    walks_in_inning = 0
    errors_in_inning = 0
    strikeouts_in_inning = 0
    homeruns_in_inning = 0
    at_bats_in_inning = 0
    doubles_in_inning = 0
    triples_in_inning = 0

    while outs < 3:

        time.sleep(3.5)

        result = at_bat(max_off)     # todo: take in batter name as parameter
        if result == 'triple':
            print("It's a triple!")
            runs_in = triple(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            hits_in_inning += 1
            triples_in_inning += 1
            at_bats_in_inning += 1
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0: # for walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        elif result == 'homerun':
            print("It's a homerun!")
            runs_in = home_run(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            hits_in_inning += 1
            homeruns_in_inning += 1
            at_bats_in_inning += 1
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0: # walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        elif result == 'double':
            print("It's a double!")
            runs_in = double(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            hits_in_inning += 1
            doubles_in_inning += 1
            at_bats_in_inning += 1
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0:  # walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        elif result == 'single':
            print("It's a single!")
            runs_in = single(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            hits_in_inning += 1
            at_bats_in_inning += 1
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0:  # walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        elif result == 'walk':
            print("The batter walked.")
            runs_in = walk(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            walks_in_inning += 1
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0: # walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        elif result == 'error':
            num = random.randint(1,2)
            if num == 1:
                print("The batter popped it up..", end=" ", flush=True)
                time.sleep(1.5)
                print("but the ball was dropped!")
            else:
                print("It's a routine ground ball..", end=" ", flush=True)
                time.sleep(1.5)
                print("but the ball was mishandled!")
            time.sleep(1)
            print("The fielder was given an error.")
            runs_in = walk(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            errors_in_inning += 1
            at_bats_in_inning += 1
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0:  # walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        elif result == 'hit by pitch':
            print("The batter was hit by the pitch!")
            runs_in = walk(base_runners)
            base_runners = update_base_runners(result, base_runners)
            runs_scored_in_inning += runs_in
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0:  # walk-off
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            at_bat_summary(outs, runs_in, base_runners)

        else:
            out_info = out_type(outs, base_runners)   # returns list
            outs = out_info[0]
            base_runners = out_info[1]
            runs_in = out_info[2]    # fielders choice double-play ball, or sac fly
            strikeouts_in_inning += out_info[3]
            runs_scored_in_inning += runs_in
            at_bats_in_inning += out_info[4]
            if i == (num_innings - 1) and side == "bottom" and (home_lead + runs_scored_in_inning) > 0:  # for walk-off case
                print(str(runs_in) + " runs scored")
                time.sleep(2)
                break
            time.sleep(2.5)
            print("")
            if outs != 3:
                print("There are " + str(outs) + " outs with" + base_runners[3])
                time.sleep(2.5)
                print("The next batter enters the batter's box.", end=" ", flush=True)
                time.sleep(1.5)
                print("Here's the pitch...")

    totals = [strikeouts_in_inning, walks_in_inning, errors_in_inning, homeruns_in_inning, runs_scored_in_inning,
              hits_in_inning, at_bats_in_inning, doubles_in_inning, triples_in_inning]

    return totals


# HIT FUNCTIONS - returns runs scored (if any) - - - - - - - - - - - - - - - - - - - - - - - -
# conditions must match the conditions of update_base_runners()

def triple(runners_on_base):        # ex. runners_on_base = [1, 1, 1, 'the bases are loaded!']

    if runners_on_base[0:3] == [1, 1, 1]:
        return 3
    elif runners_on_base[0:3] == [0, 1, 1] or runners_on_base[0:3] == [1, 1, 0] or runners_on_base[0:3] == [1, 0, 1]:
        return 2
    elif runners_on_base[0:3] == [0, 0, 0]:
        return 0
    else:
        return 1


def double(runners_on_base):

    if runners_on_base[0:3] == [1, 1, 1]:
        return 3
    elif runners_on_base[0:3] == [0, 1, 1]:
        return 2
    elif runners_on_base[0:3] == [0, 0, 0] or runners_on_base[0:3] == [1, 0, 0]:
        return 0
    else:              # runners_on_base == [1, 1, 0] or [1, 0, 1] or [0, 0, 1] or [0, 1, 0]
        return 1

# update for more baserunning results
def single(runners_on_base):

    # num = random.randint(1,2)
    if runners_on_base[0:3] == [0, 1, 0] or runners_on_base[0:3] == [0, 0, 1] or runners_on_base[0:3] == [1, 0, 1]:
        return 1
    elif runners_on_base[0:3] == [1, 1, 1] or runners_on_base[0:3] == [0, 1, 1]:
        return 2
    else:
        return 0


def walk(runners_on_base):

    if runners_on_base[0:3] == [1, 1, 1]:
        return 1
    else:
        return 0


def home_run(runners_on_base):

    if runners_on_base[0:3] == [1, 1, 1]:
        return 4
    elif runners_on_base[0:3] == [0, 1, 1] or runners_on_base[0:3] == [1, 1, 0] or runners_on_base[0:3] == [1, 0, 1]:
        return 3
    elif runners_on_base[0:3] == [0, 0, 0]:
        return 1
    else:
        return 2


# Randomly determines how the batter gets out and then updates resulting conditions accordingly  - - - - - - - -
def out_type(num_outs, runners):

    outs = num_outs
    base_runners = runners
    runs_in = 0
    strikeouts = 0
    at_bats = 1

    rand = random.randint(1, 14)
    types_of_outs = ["grounded out to first. ", "grounded out to second. ", "lined out to left field. ",
            "grounded out to third. ", "lined out to right field. ", "struck out! ",
            "popped out to left field. ", "popped out to center field. ",
            "grounded out to short. ", "popped out to right field. ", "struck out! ", "struck out! ",
            "struck out! ", "struck out! "]

    out_choice = types_of_outs[rand - 1]

    # SACRIFICE FLY
    if ((base_runners[0:3] == [0, 0, 1] or base_runners[0:3] == [0, 1, 1] or base_runners[0:3] == [1, 1, 1]) and
            outs < 2 and "pop" in out_choice):
        num2 = random.randint(1, 2)   # 50% chance of sac fly
        if num2 == 1:
            print("The batter " + out_choice)
            time.sleep(1.5)
            print("It's a sacrifice fly!")
            print("1 runs scored")
            runs_in += 1
            outs += 1
            at_bats -= 1

            if base_runners[0:3] == [1, 1, 1]:
                base_runners = [0, 1, 0, ' a runner on 2nd >>']
            elif base_runners[0:3] == [1, 0, 1]:
                base_runners = [1, 1, 0, ' runners on 1st and 2nd >>']
            elif base_runners[0:3] == [0, 1, 1]:
                base_runners = [1, 0, 0, ' a runner on 1st >>']
            else:
                base_runners = [0, 0, 0, " the bases empty >>"]

            sac_fly = [outs, base_runners, runs_in, strikeouts, at_bats]         # need to include strikeouts 0 here even if no new ones
            return sac_fly
        else:
            outs += 1
            print("The batter " + out_choice)
            time.sleep(1.5)
            print("The runner at third couldn't tag.")
            no_sac_fly = [outs, base_runners, runs_in, strikeouts, at_bats]     # need to include strikeouts 0 here even if no new ones
            return no_sac_fly

    # FORCE OUT SCENARIOS  (including double play)
    elif (base_runners[0:3] == [1, 0, 0] or base_runners[0:3] == [1, 1, 0] or base_runners[0:3] == [1, 1, 1]) and outs < 2:
        num1 = random.randint(1, 5)  # adjust percentage of double play

        # double play
        if num1 == 1:
            print("The batter hit into a double play!")
            time.sleep(1.5)
            outs += 2
            if base_runners[0:3] == [1, 1, 0]:
                base_runners = [0, 0, 1, ' a runner on third >>']
            elif base_runners[0:3] == [1, 1, 1] and outs < 3:
                runs_in += 1
                print("1 runs scored")
                base_runners = [0, 0, 0, ' the bases empty >>']
            else:
                base_runners = [0, 0, 0, " the bases empty >>"]

            double_play = [outs, base_runners, runs_in, strikeouts, at_bats]       # need to include strikeouts 0 here even if no new ones
            return double_play

        # no double play
        else:
            outs += 1
            print("The batter " + out_choice)
            time.sleep(1)

            # ground out scenario: batter out at first, other base runners advance
            if "ground" in out_choice and outs < 3:
                if base_runners[0:3] == [1, 1, 0]:
                    print("The runners advance.")
                    base_runners = [0, 1, 1, ' runners on 2nd and 3rd >>']
                elif base_runners[0:3] == [1, 1, 1]:
                    at_bats -= 1
                    runs_in += 1
                    print("1 runs scored")
                    base_runners = [0, 1, 1, ' runners on 2nd and 3rd >>']
                elif base_runners[0:3] == [1, 0, 0]:
                    print("Runner advances to second base.")
                    base_runners = [0, 1, 0, ' a runner on 2nd >>']
                else:
                    base_runners = base_runners     # unchanged

            if "struck" in out_choice:
                strikeouts += 1
            no_double_play = [outs, base_runners, runs_in, strikeouts, at_bats]    #strikeouts [3]
            return no_double_play

    # REGULAR OUT
    else:
        outs += 1
        print("The batter " + out_choice)
        if "struck" in out_choice:
            strikeouts += 1
        no_double_play = [outs, base_runners, runs_in, strikeouts, at_bats]       #strikeouts   [3]
        return no_double_play


def announce_inning(i, side, away_team, home_team):

    if i == 0:
        print("It's the " + side + " of the " + str(i + 1) + "st inning")
    elif i == 1:
        print("It's the " + side + " of the " + str(i + 1) + "nd inning")
    elif i == 2:
        print("It's the " + side + " of the " + str(i + 1) + "rd inning")
    else:
        print("It's the " + side + " of the " + str(i + 1) + "th inning")
    time.sleep(2.5)

    if side == 'top':
        print("The " + away_team + " are up to bat")
    else:
        print("The " + home_team + " are up to bat")
    time.sleep(2)
    print("The first batter enters the batter's box.", end=" ", flush=True)
    time.sleep(1.5)
    print("Here's the pitch...")


def update_base_runners(result, base_runners):

    curr_base_runners = base_runners

    if result == 'triple':
        curr_base_runners = [0, 0, 1, ' a runner on 3rd >>']

    elif result == 'homerun':
        curr_base_runners = [0, 0, 0, ' the bases empty >>']

    elif result == 'double':
        if base_runners[0:3] == [1, 1, 0] or base_runners[0:3] == [1, 0, 1] or base_runners[0:3] == [1, 0, 0]:
            curr_base_runners = [0, 1, 1, ' runners on 2nd and 3rd >>']
        else:
            curr_base_runners = [0, 1, 0, ' a runner on 2nd >>']

    elif result == 'single':
        if base_runners[0:3] == [1, 0, 1] or base_runners[0:3] == [1, 0, 0] or base_runners[0:3] == [1, 1, 1]:
            curr_base_runners = [1, 1, 0, ' runners on 1st and 2nd >>']
        elif base_runners[0:3] == [1, 1, 0]:
            curr_base_runners = [1, 1, 1, ' the bases loaded! >>']
        else:
            curr_base_runners = [1, 0, 0, ' a runner on 1st >>']

    elif result == 'walk' or result == 'hit by pitch' or result == "error":
        if base_runners[0:3] == [1, 0, 0] or base_runners[0:3] == [0, 1, 0]:
            curr_base_runners = [1, 1, 0, ' runners on 1st and 2nd >>']
        elif base_runners[0:3] == [0, 0, 0]:
            curr_base_runners = [1, 0, 0, ' a runner on 1st >>']
        elif base_runners[0:3] == [0, 0, 1]:
            curr_base_runners = [1, 0, 1, ' runners on 1st and 3rd >>']
        else:
            curr_base_runners = [1, 1, 1, ' the bases loaded! >>']

    return curr_base_runners


# prints number of runs scored and current outs/baserunner conditions to user for each at bat,
def at_bat_summary(outs, runs_in, base_runners):

    if runs_in > 0:
        print(str(runs_in) + " runs scored")
    time.sleep(2.5)
    print("")
    print("There are " + str(outs) + " outs with" + base_runners[3])
    time.sleep(2.5)
    print("The next batter enters the batter's box.", end=" ", flush=True)
    time.sleep(1.5)
    print("Here's the pitch...")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


if __name__ == '__main__':
    main()