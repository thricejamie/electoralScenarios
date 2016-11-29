from state_data import ALL_STATES

total_ec_clinton = 0
total_ec_trump = 0
total_ec_johnson = 0
total_ec_stein = 0
total_ec_mcmullin = 0
total_ec_other = 0

total_proportional_ec_clinton = 0
total_proportional_ec_trump = 0
total_proportional_ec_johnson = 0
total_proportional_ec_stein = 0
total_proportional_ec_mcmullin = 0
total_proportional_ec_other = 0

for state in ALL_STATES:
    clinton_votes = state.clinton_votes
    trump_votes = state.trump_votes
    johnson_votes = state.johnson_votes
    stein_votes = state.stein_votes if hasattr(state, 'stein_votes') else 0
    mcmullin_votes = state.mcmullin_votes if hasattr(state, 'mcmullin_votes') else 0
    other_votes = state.other_votes if hasattr(state, 'other_votes') else 0
    
    total_votes = clinton_votes + trump_votes + johnson_votes + stein_votes + mcmullin_votes + other_votes
    
    pct_clinton = float(clinton_votes)/total_votes
    pct_trump = float(trump_votes)/total_votes
    pct_johnson = float(johnson_votes)/total_votes
    pct_stein = float(stein_votes)/total_votes
    pct_mcmullin = float(mcmullin_votes)/total_votes
    pct_other = float(other_votes)/total_votes
    print(state.__name__, pct_clinton, pct_trump, pct_johnson, pct_stein, pct_mcmullin, pct_other)
    
    total_ec_clinton += int(round(pct_clinton * state.electoral_votes))
    total_ec_trump += int(round(pct_trump * state.electoral_votes))
    total_ec_johnson += int(round(pct_johnson * state.electoral_votes))
    total_ec_stein += int(round(pct_stein * state.electoral_votes))
    total_ec_mcmullin += int(round(pct_mcmullin * state.electoral_votes))
    total_ec_other += int(round(pct_other * state.electoral_votes))

    total_proportional_ec_clinton += int(round(pct_clinton * state.percentage_based_electoral_votes_rounded))
    total_proportional_ec_trump += int(round(pct_trump * state.percentage_based_electoral_votes_rounded))
    total_proportional_ec_johnson += int(round(pct_johnson * state.percentage_based_electoral_votes_rounded))
    total_proportional_ec_stein += int(round(pct_stein * state.percentage_based_electoral_votes_rounded))
    total_proportional_ec_mcmullin += int(round(pct_mcmullin * state.percentage_based_electoral_votes_rounded))
    total_proportional_ec_other += int(round(pct_other * state.percentage_based_electoral_votes_rounded))

print('Electoral votes: Clinton {}, Trump {}, Johnson {}, Stein {}, McMullin {}, Other {}'.format(total_ec_clinton,
                                                                                                  total_ec_trump,
                                                                                                  total_ec_johnson,
                                                                                                  total_ec_stein,
                                                                                                  total_ec_mcmullin,
                                                                                                  total_ec_other))
print('Proportional EC votes: Clinton {}, Trump {}, Johnson {}, Stein {}, McMullin {}, Other {}'.format(total_proportional_ec_clinton,
                                                                                                  total_proportional_ec_trump,
                                                                                                  total_proportional_ec_johnson,
                                                                                                  total_proportional_ec_stein,
                                                                                                  total_proportional_ec_mcmullin,
                                                                                                  total_proportional_ec_other))
