import streamlit as st
from collections import deque
import time
from utils.game_logic import GameLogic
from utils.ui_components import UIComponents

# Page config with improved caching
st.set_page_config(
    page_title="CreatorLuck | Premium DeFi Gaming",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/yourusername/creatorluck',
        'Report a bug': "https://github.com/yourusername/creatorluck/issues",
        'About': "# CreatorLuck Premium DeFi Game\nA decentralized gaming experience on Creator Network."
    }
)

# Initialize session state with type hints
if 'balance' not in st.session_state:
    st.session_state.balance = 10000.0
if 'history' not in st.session_state:
    st.session_state.history = []
if 'last_numbers' not in st.session_state:
    st.session_state.last_numbers = deque(maxlen=10)
if 'jackpot' not in st.session_state:
    st.session_state.jackpot = 5000.0
if 'streak' not in st.session_state:
    st.session_state.streak = 0
if 'achievements' not in st.session_state:
    st.session_state.achievements = set()

# Load CSS from file
with open('static/css/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header with improved animation
st.markdown('<h1 class="game-title">🎲 CreatorLuck</h1>', unsafe_allow_html=True)

# Add network info
st.markdown(f"""
<div class="network-info">
    <p>Running on Creator Network | Current Block: {123456789}</p>
    <p>Total Staked: {1000000} CREATOR</p>
</div>
""", unsafe_allow_html=True)

# Market status check with improved error handling
try:
    is_open, status, remaining_time = GameLogic.is_market_open()
    hours = remaining_time // 3600
    minutes = (remaining_time % 3600) // 60
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if is_open:
            st.markdown(f'<div class="timer-display">⏰ Premium Market Open | Closes in: {hours}h {minutes}m</div>', 
                       unsafe_allow_html=True)
        else:
            if status == "opening_soon":
                st.markdown(f'<div class="timer-display">🌅 Market Opens in: {hours}h {minutes}m</div>', 
                           unsafe_allow_html=True)
            else:
                st.markdown('<div class="timer-display">🌙 Market Closed | Next Session at 09:00</div>', 
                           unsafe_allow_html=True)
except Exception as e:
    st.error(f"Error checking market status: {str(e)}")

# Stats display with error handling
try:
    total_bets = len(st.session_state.history)
    wins = sum(1 for x in st.session_state.history if x['won'])
    win_rate = (wins / total_bets * 100) if total_bets > 0 else 0
    UIComponents.render_stats_cards(
        st.session_state.balance,
        total_bets,
        win_rate,
        st.session_state.jackpot
    )
except Exception as e:
    st.error(f"Error displaying stats: {str(e)}")

# Number trends
if st.session_state.last_numbers:
    UIComponents.render_number_trends(list(st.session_state.last_numbers))
    UIComponents.render_lucky_numbers(list(st.session_state.last_numbers))

# Game interface with improved error handling
with st.expander("📖 How to Play Royal Fortune", expanded=False):
    st.markdown("""
    ### Premium Game Types:
    1. **Royal Single (0-9)** - Bet on a single digit (10x payout)
    2. **Golden Jodi (00-99)** - Bet on a two-digit number (90x payout)
    3. **Triple Crown (000-999)** - Three unique digits (150x payout)
    4. **Double Fortune** - Two matching digits (300x payout)
    5. **Royal Flush** - Three matching digits (500x payout + Jackpot chance)
    
    ### Special Features:
    - 🏆 Progressive Jackpot
    - 💫 Win Streaks Bonus
    - 🎯 Achievement System
    - 📊 Advanced Analytics
    """)

# Game selection with improved validation
game_type = st.selectbox(
    "Select Premium Game",
    ["Royal Single", "Golden Jodi", "Triple Crown", "Double Fortune", "Royal Flush"],
    help="Choose your game type carefully. Each has different winning odds and payouts."
)

# Game info display
multiplier = GameLogic.get_payout_multiplier(game_type)
st.markdown(f"""
<div class="feature-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h3 style="color: #FFD700;">Current Game: {game_type}</h3>
            <p style="color: #FFA500;">Potential Win: {multiplier}x your bet</p>
        </div>
        <div style="text-align: right;">
            <h4 style="color: #FFD700;">Market Status</h4>
            <p style="color: {'#00FF00' if is_open else '#FF0000'};">
                {'🟢 Open' if is_open else '🔴 Closed'}
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Number selection with improved validation
st.markdown('<div class="feature-card">', unsafe_allow_html=True)

try:
    if game_type == "Royal Single":
        col1, col2 = st.columns([3, 1])
        with col1:
            number = st.number_input("Select Your Lucky Number (0-9)", 0, 9, 5,
                help="Choose a single digit number between 0 and 9")
        with col2:
            st.markdown("""
            <div class="odds-display">
                <h4>Odds</h4>
                <p>1:10</p>
            </div>
            """, unsafe_allow_html=True)
        user_numbers = [number]
    elif game_type == "Golden Jodi":
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            num1 = st.number_input("First Digit", 0, 9, 5)
        with col2:
            num2 = st.number_input("Second Digit", 0, 9, 7)
        with col3:
            st.markdown("""
            <div class="odds-display">
                <h4>Odds</h4>
                <p>1:90</p>
            </div>
            """, unsafe_allow_html=True)
        user_numbers = [num1 * 10 + num2]
    else:
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
        with col1:
            num1 = st.number_input("First Digit", 0, 9, 5)
        with col2:
            num2 = st.number_input("Second Digit", 0, 9, 7)
        with col3:
            num3 = st.number_input("Third Digit", 0, 9, 8)
        with col4:
            odds = "1:150" if game_type == "Triple Crown" else "1:300" if game_type == "Double Fortune" else "1:500"
            st.markdown(f"""
            <div class="odds-display">
                <h4>Odds</h4>
                <p>{odds}</p>
            </div>
            """, unsafe_allow_html=True)
        user_numbers = [num1, num2, num3]

    # Bet amount with quick select
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        bet_amount = st.number_input("Bet Amount (CREATOR)", 
                                   min_value=10.0,
                                   max_value=float(st.session_state.balance),
                                   value=100.0,
                                   step=10.0)
    with col2:
        quick_bets = st.selectbox("Quick Bet", ["100", "500", "1000", "5000"])
        if st.button("Apply"):
            bet_amount = float(quick_bets)

except Exception as e:
    st.error(f"Error in number selection: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# Play button with improved error handling
if st.button("🎲 PLAY NOW", use_container_width=True):
    try:
        if not is_open:
            st.error("Market is currently closed!")
        elif bet_amount > st.session_state.balance:
            st.error("Insufficient balance!")
        else:
            st.session_state.balance -= bet_amount
            st.session_state.jackpot = GameLogic.calculate_jackpot(st.session_state.jackpot, bet_amount)
            
            with st.spinner("Drawing numbers..."):
                time.sleep(1)
                
            first_set, first_sum, second_set, second_sum = GameLogic.generate_numbers()
            
            # Animated display
            st.markdown('<div class="result-animation">', unsafe_allow_html=True)
            st.markdown(f'<div class="number-display">First Draw: {" ".join(map(str, first_set))} → {first_sum}</div>', 
                       unsafe_allow_html=True)
            
            time.sleep(0.5)
            
            st.markdown(f'<div class="number-display">Second Draw: {" ".join(map(str, second_set))} → {second_sum}</div>', 
                       unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Update lucky numbers
            st.session_state.last_numbers.append(first_sum)
            
            # Check win
            won = GameLogic.check_win(game_type, user_numbers, first_set, first_sum, second_set, second_sum)
            
            if won:
                winnings = bet_amount * multiplier
                st.session_state.balance += winnings
                st.session_state.streak += 1
                
                st.markdown('<div class="win-animation">', unsafe_allow_html=True)
                st.success(f"🎉 Congratulations! You won {GameLogic.format_currency(winnings)} CREATOR!")
                
                if st.session_state.streak >= 3:
                    bonus = bet_amount * 0.1  # 10% bonus for streak
                    st.session_state.balance += bonus
                    st.success(f"🔥 Win Streak Bonus: +{GameLogic.format_currency(bonus)} CREATOR!")
                
                st.balloons()
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Better luck next time! 😢")
                st.session_state.streak = 0
            
            # Update history
            st.session_state.history.append({
                'timestamp': time.strftime("%H:%M:%S"),
                'game_type': game_type,
                'numbers': user_numbers,
                'first_set': first_set,
                'second_set': second_set,
                'bet_amount': bet_amount,
                'won': won,
                'payout': winnings if won else 0
            })
            
    except Exception as e:
        st.error(f"Error during gameplay: {str(e)}")

# Game history with error handling
if st.session_state.history:
    with st.expander("📊 Game History & Analysis", expanded=False):
        try:
            UIComponents.render_game_history(st.session_state.history)
        except Exception as e:
            st.error(f"Error displaying game history: {str(e)}")

# Reset button with confirmation
if st.button("🔄 Reset Game"):
    if st.session_state.balance != 10000:  # Only show confirmation if game has been played
        if st.button("⚠️ Confirm Reset"):
            st.session_state.balance = 10000.0
            st.session_state.history = []
            st.session_state.last_numbers = deque(maxlen=10)
            st.session_state.jackpot = 5000.0
            st.session_state.streak = 0
            st.session_state.achievements = set()
            st.rerun()
    else:
        st.session_state.balance = 10000.0
        st.session_state.history = []
        st.session_state.last_numbers = deque(maxlen=10)
        st.session_state.jackpot = 5000.0
        st.session_state.streak = 0
        st.session_state.achievements = set()
        st.rerun() 