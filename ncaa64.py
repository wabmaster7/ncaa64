import random
from dataclasses import dataclass

@dataclass
class Team:
    name: str
    seed: int
    rpi: float
    last_ten: float

first_round = [
    # SOUTH
    (Team("Auburn", seed=1, rpi=0.689, last_ten=0.7), Team("Alabama ST", seed=16, rpi=0.467, last_ten=0.9)),
    (Team("Louisville", seed=8, rpi=0.618, last_ten=0.9), Team("Creighton", seed=9, rpi=0.596, last_ten=0.6)),
    (Team("Michigan", seed=5, rpi=0.625, last_ten=0.6), Team("UC San Diego", seed=12, rpi=0.595, last_ten=1.0)),
    (Team("Texas A&M", seed=4, rpi=0.612, last_ten=0.5), Team("Yale", seed=13, rpi=0.589, last_ten=0.9)),
    (Team("Ole Miss", seed=6, rpi=0.617, last_ten=0.5), Team("North Carolina", seed=11, rpi=0.594, last_ten=0.8)),
    (Team("Iowa St.", seed=3, rpi=0.594, last_ten=0.6), Team("Lipscomb", seed=14, rpi=0.536, last_ten=0.9)),
    (Team("Marquette", seed=7, rpi=0.599, last_ten=0.5), Team("New Mexico", seed=10, rpi=0.600, last_ten=0.7)),
    (Team("Michigan St.", seed=2, rpi=0.640, last_ten=0.8), Team("Bryant", seed=15, rpi=0.530, last_ten=0.9)),

    # WEST
    (Team("Florida", seed=1, rpi=0.662, last_ten=0.9), Team("Norfolk St.", seed=16, rpi=0.522, last_ten=0.8)),
    (Team("UConn", seed=8, rpi=0.573, last_ten=0.7), Team("Oklahoma", seed=9, rpi=0.565, last_ten=0.4)),
    (Team("Memphis", seed=5, rpi=0.640, last_ten=0.9), Team("Colorado St.", seed=12, rpi=0.586, last_ten=1.0)),
    (Team("Maryland", seed=4, rpi=0.601, last_ten=0.8), Team("Grand Canyon", seed=13, rpi=0.548, last_ten=0.9)),
    (Team("Missouri", seed=6, rpi=0.587, last_ten=0.5), Team("Drake", seed=11, rpi=0.602, last_ten=0.9)),
    (Team("Texas Tech", seed=3, rpi=0.594, last_ten=0.7), Team("UNC Wilmington", seed=14, rpi=0.566, last_ten=0.8)),
    (Team("Kansas", seed=7, rpi=0.603, last_ten=0.5), Team("Arkansas", seed=10, rpi=0.562, last_ten=0.6)),
    (Team("St. John's", seed=2, rpi=0.639, last_ten=0.9), Team("Omaha", seed=15, rpi=0.524, last_ten=0.8)),

    # EAST
    (Team("Duke", seed=1, rpi=0.657, last_ten=1.0), Team("America/Mount St Mary's", seed=16, rpi=0.522, last_ten=0.5)),
    (Team("Mississippi St.", seed=8, rpi=0.590, last_ten=0.4), Team("Baylor", seed=9, rpi=0.573, last_ten=0.4)),
    (Team("Oregon", seed=5, rpi=0.619, last_ten=0.8), Team("Liberty", seed=12, rpi=0.578, last_ten=0.9)),
    (Team("Arizona", seed=4, rpi=0.598, last_ten=0.5), Team("Akron", seed=13, rpi=0.592, last_ten=0.9)),
    (Team("BYU", seed=6, rpi=0.583, last_ten=0.9), Team("VCU", seed=11, rpi=0.599, last_ten=0.9)),
    (Team("Wisconsin", seed=3, rpi=0.607, last_ten=0.6), Team("Montana", seed=14, rpi=0.559, last_ten=0.9)),
    (Team("Saint Mary's", seed=7, rpi=0.623, last_ten=0.8), Team("Vanderbilt", seed=10, rpi=0.568, last_ten=0.4)),
    (Team("Alabama", seed=2, rpi=0.672, last_ten=0.5), Team("Robert Morris", seed=15, rpi=0.541, last_ten=1.0)),

    # MIDWEST
    (Team("Houston", seed=1, rpi=0.652, last_ten=1.0), Team("SIU Edwardsville", seed=16, rpi=0.495, last_ten=0.7)),
    (Team("Gonzaga", seed=8, rpi=0.604, last_ten=0.9), Team("Georgia", seed=9, rpi=0.588, last_ten=0.5)),
    (Team("Clemson", seed=5, rpi=0.619, last_ten=0.9), Team("McNeese", seed=12, rpi=0.578, last_ten=1.0)),
    (Team("Purdue", seed=4, rpi=0.619, last_ten=0.4), Team("High Point", seed=13, rpi=0.576, last_ten=1.0)),
    (Team("Illinois", seed=6, rpi=0.589, last_ten=0.6), Team("Texas/Xavier", seed=11, rpi=0.522, last_ten=0.5)),
    (Team("Kentucky", seed=3, rpi=0.628, last_ten=0.6), Team("Troy", seed=14, rpi=0.543, last_ten=0.8)),
    (Team("UCLA", seed=7, rpi=0.585, last_ten=0.6), Team("Utah St.", seed=10, rpi=0.598, last_ten=0.6)),
    (Team("Tennessee", seed=2, rpi=0.655, last_ten=0.7), Team("Wofford", seed=15, rpi=0.525, last_ten=0.7)),
]

def simulate_game(team1, team2):
    power = 0.9
    j = 1.4
    k = 1.1
    team1_seed_weight = 1 / (team1.seed**power)
    team2_seed_weight = 1 / (team2.seed**power)
    team1_weight = (j * team1.rpi + k * (team1.last_ten - 0.4)) * team1_seed_weight
    team2_weight = (j * team2.rpi + k * (team2.last_ten - 0.4)) * team2_seed_weight

    total = team1_seed_weight + team2_seed_weight
    team1_prob = 100 * (team1_weight / total)
    team2_prob = 100 * (team2_weight / total)

    winner = random.choices([team1, team2], weights=[team1_prob, team2_prob], k=1)[0]
    return winner

def simulate_tournament(first_round):
    # 2 5/12 upsets, 8 #1 seed wins after 2 rounds, my_team with 6 wins, at most 3 #1 seeds in Final Four,
    # Upsets: ≤8 in Round 1, ≤4 in Round 2, ≤2 in Round 3
    
    while True:  # Outer loop to restart the simulation if conditions fail
        current_games = first_round
        winners_list = []  # Track all winners in this tournament
        iteration_count = 0  # Track while loop iterations
        seed_5_vs_12_team2_wins = 0  # Track #12 seed wins over #5 seeds in first round
        upset_counts = {1: 0, 2: 0, 3: 0}  # Track upsets per round

        while len(current_games) > 0:
            iteration_count += 1
            winners = []

            if iteration_count == 1:
                # First round: 2 forced 5 vs. 12 upsets, ≤8 total upsets
                for team1, team2 in current_games:
                    if team1.seed == 5 and team2.seed == 12 and seed_5_vs_12_team2_wins < 2:
                        # Force team2 (#12 seed) to win for the first two 5 vs. 12 matchups
                        winner = team2
                        seed_5_vs_12_team2_wins += 1
                        upset_counts[1] += 1
                    else:
                        winner = simulate_game(team1, team2)
                        if winner == team2 and team2.seed > team1.seed:
                            upset_counts[1] += 1
                    winners.append(winner)
                    winners_list.append(winner)
                if upset_counts[1] > 8:
                    break  # Restart if more than 8 upsets in Round 1

            elif iteration_count in (2, 3):
                # Rounds 2 and 3: Limit upsets
                for team1, team2 in current_games:
                    winner = simulate_game(team1, team2)
                    if winner == team2 and team2.seed > team1.seed:
                        upset_counts[iteration_count] += 1
                    winners.append(winner)
                    winners_list.append(winner)
                if (iteration_count == 2 and upset_counts[2] > 4) or \
                   (iteration_count == 3 and upset_counts[3] > 2):
                    break  # Restart if upset limits exceeded

            else:
                # Normal simulation for Rounds 4+
                for team1, team2 in current_games:
                    winner = simulate_game(team1, team2)
                    winners.append(winner)
                    winners_list.append(winner)

            # Check condition after 2 iterations
            if iteration_count == 2:
                seed_1_wins = sum(1 for team in winners_list if team.seed == 1)
                if seed_1_wins < 8:
                    break  # Restart if #1 seeds have fewer than 8 wins

            # Check Final Four condition after 5 iterations
            if iteration_count == 5:
                seed_1_count = sum(1 for team in winners if team.seed == 1)
                if seed_1_count > 3:
                    break  # Restart if more than 3 #1 seeds reach Final Four

            if len(winners) == 1:
                my_team = "Florida"
                # Final check: Ensure Florida has 6 wins
                my_team_wins = sum(1 for team in winners_list if team.name == my_team)
                if my_team_wins != 6:
                    break  # Restart if my_team doesn't have exactly 6 wins
                return winners_list  # Return if all conditions are met

            next_round = []
            for i in range(0, len(winners), 2):
                next_round.append((winners[i], winners[i + 1]))
            current_games = next_round

        # Restart if any condition fails
        if iteration_count in (1, 2, 3, 5) or len(winners) == 1:
            continue  # Restart due to upsets, #1 seeds, Final Four, or Florida condition
        return winners_list  # Return if simulation completes normally

def run_simulations(first_round, num_simulations=5000):
    # Create a dictionary to map team names to their seeds from first_round
    team_seeds = {team.name: team.seed for pair in first_round for team in pair}
    
    # Initialize dictionary to track wins for each team
    win_counts = {team.name: 0 for pair in first_round for team in pair}
    
    # Run simulations
    for _ in range(num_simulations):
        tournament_winners = simulate_tournament(first_round)
        # Count wins for each team in this tournament
        for winner in tournament_winners:
            win_counts[winner.name] += 1
    
    return win_counts, team_seeds

# Run the simulation
results, team_seeds = run_simulations(first_round, num_simulations=1)

# ANSI color codes
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"


RESET = "\033[0m"

# Sort results by wins (descending)
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

# Split into three columns: first 16, next 16, last 32
first_column_teams = sorted_results[:16]  # Top 16
second_column_teams = sorted_results[16:32]  # Next 16
third_column_teams = sorted_results[32:]  # Last 32

# Prepare formatted strings for each team with conditional coloring
max_name_length = max(len(team[0]) for team in sorted_results) + 10
column_format = f"{{:<{max_name_length + 10}}}"

# Build three lists for printing with conditional colors
first_column = []
for team, wins in first_column_teams:
    color = RED if team_seeds[team] == 1 else YELLOW if team_seeds[team] == 2 else GREEN if team_seeds[team] == 3 else BLUE if team_seeds[team] == 4 else ""
    first_column.append(f"{color}#{team_seeds[team]} {team}: {wins} wins{RESET}")

second_column = []
for team, wins in second_column_teams:
    color = RED if team_seeds[team] == 1 else YELLOW if team_seeds[team] == 2 else GREEN if team_seeds[team] == 3 else BLUE if team_seeds[team] == 4 else ""
    second_column.append(f"{color}#{team_seeds[team]} {team}: {wins} wins{RESET}")

third_column = []
for team, wins in third_column_teams:
    color = RED if team_seeds[team] == 1 else YELLOW if team_seeds[team] == 2 else GREEN if team_seeds[team] == 3 else BLUE if team_seeds[team] == 4 else ""
    third_column.append(f"{color}#{team_seeds[team]} {team}: {wins} wins{RESET}")

# Print in three columns with extra spacing in columns 1 and 2
print("\nTournament Results (Wins by Team):")
for i in range(32):  # 32 lines to accommodate all teams in third column
    # First column: print every other line (16 teams over 32 lines)
    left = first_column[i // 2] if i % 2 == 0 and i // 2 < len(first_column) else ""
    # Second column: print every other line (16 teams over 32 lines)
    middle = second_column[i // 2] if i % 2 == 0 and i // 2 < len(second_column) else ""
    # Third column: print all 32 teams, one per line
    right = third_column[i] if i < len(third_column) else ""
    print(f"{column_format.format(left)}{column_format.format(middle)}{right}")