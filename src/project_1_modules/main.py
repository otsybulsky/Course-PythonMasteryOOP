from gaming_stats import calculate_score, get_rank, GAME_NAME
import player_utils as ut

def main():
    player = ut.create_player_profile("Oleg", 49)
    print(f"Welcome to {GAME_NAME}!")
    print("-" * 30)
    
    achievements = 15
    score = 5
    stats = ut.format_player_stats(player["name"], achievements, score)
    print(stats)

if __name__ == "__main__":
    main()