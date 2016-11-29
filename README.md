This project contains simple analysis of electoral college scenarios for the 2016 election.

* state_data.py contains the basic per-state information on voting results, existing electoral college votes, and rounded and non-rounded potential electoral college votes if they were fully proportional to state size in comparison to 2010 census numbers (the rounded proportional numbers manage to lose an electoral vote when totaled up, due to some rounding somewhere)
* scenarios_existing_winner_take_all.py runs a few scenarios to compare existing electoral college results to the results if we used the proportional numbers, with some speculative divisions for the non-winner-take-all states
* scenarios_no_winner_take_all.py attempts to determine how votes would be divided with no winner-take-all, both for existing electoral college allocation and with the rebalanced rounded numbers
