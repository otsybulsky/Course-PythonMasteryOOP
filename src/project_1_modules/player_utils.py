from gaming_stats import  calculate_score, get_rank

def create_player_profile(name, age):
    return {
        "name": name,
        "age": age,
        "games_played": 0,
        "is_active": True,        
    }

def format_player_stats(name, achievements, score):
    calculated_score = calculate_score(achievements, score)
    rank = get_rank(calculated_score)
    return f"""
Player statistics: {name}
--------------------------
Achievements: {achievements}
Score: {score}
Calculated Score: {calculated_score}
Rank: {rank}
"""