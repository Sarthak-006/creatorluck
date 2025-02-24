import random
from datetime import datetime, timedelta
from typing import List, Dict, Any, Tuple

class GameLogic:
    @staticmethod
    def generate_numbers() -> Tuple[List[int], int, List[int], int]:
        """Generate random numbers for the game"""
        first_set = [random.randint(0, 9) for _ in range(3)]
        first_sum = sum(first_set) % 10
        second_set = [random.randint(0, 9) for _ in range(3)]
        second_sum = sum(second_set) % 10
        return first_set, first_sum, second_set, second_sum

    @staticmethod
    def check_win(game_type: str, user_numbers: List[int], first_set: List[int], 
                  first_sum: int, second_set: List[int], second_sum: int) -> bool:
        """Check if the player has won based on game type and numbers"""
        if game_type == "Royal Single":
            return user_numbers[0] in [first_sum, second_sum]
        elif game_type == "Golden Jodi":
            result_jodi = first_sum * 10 + second_sum
            return user_numbers[0] == result_jodi
        elif game_type == "Triple Crown":
            return sorted(user_numbers) == sorted(first_set) or sorted(user_numbers) == sorted(second_set)
        elif game_type == "Double Fortune":
            return (len(set(user_numbers)) == 2 and 
                   (sorted(user_numbers) == sorted(first_set) or sorted(user_numbers) == sorted(second_set)))
        else:  # Royal Flush
            return (len(set(user_numbers)) == 1 and 
                   (sorted(user_numbers) == sorted(first_set) or sorted(user_numbers) == sorted(second_set)))

    @staticmethod
    def get_payout_multiplier(game_type: str) -> int:
        """Get the payout multiplier for each game type"""
        return {
            "Royal Single": 10,
            "Golden Jodi": 90,
            "Triple Crown": 150,
            "Double Fortune": 300,
            "Royal Flush": 500
        }[game_type]

    @staticmethod
    def calculate_jackpot(current_jackpot: float, bet_amount: float) -> float:
        """Calculate new jackpot amount"""
        contribution = bet_amount * 0.01  # 1% of bet goes to jackpot
        return current_jackpot + contribution

    @staticmethod
    def format_currency(amount: float) -> str:
        """Format currency with proper separators"""
        return f"{amount:,.2f}"

    @staticmethod
    def is_market_open() -> Tuple[bool, str, int]:
        """Check if market is open and return status with remaining time"""
        current_time = datetime.now().time()
        market_open = datetime.strptime("09:00", "%H:%M").time()
        market_close = datetime.strptime("21:00", "%H:%M").time()
        
        if market_open <= current_time <= market_close:
            time_to_close = datetime.combine(datetime.today(), market_close) - datetime.now()
            return True, "open", time_to_close.seconds
        elif current_time < market_open:
            time_to_open = datetime.combine(datetime.today(), market_open) - datetime.now()
            return False, "opening_soon", time_to_open.seconds
        else:
            return False, "closed", 0 