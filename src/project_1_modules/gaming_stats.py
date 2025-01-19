def calculate_score(achievements, score):
    if score == 0:
        return achievements * 100
    return round(achievements / score * 100)

def get_rank(score):
    if score >= 200:
        return "Professional"
    elif score >= 150:
        return "Expert"
    elif score >= 100:
        return "Experienced"
    else:
        return "Beginner"
    
#Module-level constants
DEFAULT_ACHIEVEMENTS = 0
DEFAULT_SCORE = 0
GAME_NAME = "Space Wars"