from state_data import ALL_STATES

total_clinton_ec = 0
total_clinton_proportional = 0
total_clinton_proportional_rounded = 0
total_trump_ec = 0
total_trump_proportional = 0
total_trump_proportional_rounded = 0

for state in ALL_STATES:
    if state.winner_take_all:
        if state.clinton_votes > state.trump_votes:
            print(state.__name__, 'Clinton', state.electoral_votes)
            total_clinton_ec += state.electoral_votes
            total_clinton_proportional += state.percentage_based_electoral_votes
            total_clinton_proportional_rounded += state.percentage_based_electoral_votes_rounded
        else:
            print(state.__name__, 'Trump', state.electoral_votes)
            total_trump_ec += state.electoral_votes
            total_trump_proportional += state.percentage_based_electoral_votes
            total_trump_proportional_rounded += state.percentage_based_electoral_votes_rounded
    else:
        clinton_cds_won = len([cd for cd in state.congressional_district_votes if cd[0] > cd[1]])
        trump_cds_won = len([cd for cd in state.congressional_district_votes if cd[0] < cd[1]])
        print(state.__name__ + ' congressional ', 'Clinton ' + str(clinton_cds_won), 'Trump ' + str(trump_cds_won))
        if state.clinton_votes > state.trump_votes:
            print(state.__name__ + ' at large', 'Clinton', 2)
            total_clinton_ec += 2
        else:
            print(state.__name__ + ' at large', 'Trump', 2)
            total_trump_ec += 2
        total_clinton_ec += clinton_cds_won
        total_clinton_proportional += state.percentage_based_electoral_votes * float(clinton_cds_won)/len(state.congressional_district_votes)
        total_clinton_proportional_rounded += int(round(state.percentage_based_electoral_votes_rounded * float(clinton_cds_won)/len(state.congressional_district_votes)))
        total_trump_ec += trump_cds_won
        total_trump_proportional += state.percentage_based_electoral_votes * float(trump_cds_won)/len(state.congressional_district_votes)
        total_trump_proportional_rounded += int(round(state.percentage_based_electoral_votes_rounded * float(trump_cds_won)/len(state.congressional_district_votes)))

print('Electoral College: Clinton {}, Trump {}'.format(total_clinton_ec, total_trump_ec))
print('Proportional EC, fractional: Clinton {}, Trump {}'.format(total_clinton_proportional, total_trump_proportional))
print('Proportional EC, rounded: Clinton {}, Trump {}'.format(total_clinton_proportional_rounded, total_trump_proportional_rounded))
