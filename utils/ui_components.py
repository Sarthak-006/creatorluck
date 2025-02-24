import streamlit as st
import pandas as pd
from typing import List, Dict, Any
import plotly.graph_objects as go

class UIComponents:
    @staticmethod
    def render_stats_cards(balance: float, total_bets: int, win_rate: float, jackpot: float):
        """Render the stats cards with animations"""
        cols = st.columns(4)
        with cols[0]:
            st.markdown(f'<div class="stats-card">💰 Balance<br>${balance:,.2f}</div>', unsafe_allow_html=True)
        with cols[1]:
            st.markdown(f'<div class="stats-card">🎯 Total Bets<br>{total_bets}</div>', unsafe_allow_html=True)
        with cols[2]:
            st.markdown(f'<div class="stats-card">📈 Win Rate<br>{win_rate:.1f}%</div>', unsafe_allow_html=True)
        with cols[3]:
            st.markdown(f'<div class="stats-card">🏆 Jackpot<br>${jackpot:,.2f}</div>', unsafe_allow_html=True)

    @staticmethod
    def render_game_history(history: List[Dict[str, Any]]):
        """Render game history with enhanced visuals"""
        if not history:
            return
            
        df = pd.DataFrame(history)
        
        # Recent games table
        st.subheader("Recent Games")
        st.dataframe(
            df.tail(10).style.apply(
                lambda x: ['background-color: rgba(76,175,80,0.1)' if x['won'] 
                          else 'background-color: rgba(255,0,0,0.1)' for i in x], 
                axis=1
            )
        )
        
        # Analytics
        if len(df) >= 5:
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.subheader("Game Performance")
                game_stats = df.groupby('game_type')['won'].agg(['count', 'mean'])
                game_stats.columns = ['Total Games', 'Win Rate']
                game_stats['Win Rate'] = game_stats['Win Rate'].apply(lambda x: f"{x*100:.1f}%")
                st.dataframe(game_stats)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.subheader("Profit/Loss Trend")
                df['profit'] = df.apply(lambda x: x['payout'] - x['bet_amount'], axis=1)
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    y=df['profit'].cumsum(),
                    mode='lines',
                    name='Cumulative P/L',
                    line=dict(color='#FFD700', width=2)
                ))
                fig.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis=dict(showgrid=False),
                    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
                    font=dict(color='#FFFFFF'),
                    margin=dict(l=0, r=0, t=0, b=0)
                )
                st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

    @staticmethod
    def render_number_trends(last_numbers: List[int]):
        """Render number trends and statistics"""
        if not last_numbers:
            return
            
        number_freq = {}
        for num in range(10):
            count = last_numbers.count(num)
            number_freq[num] = count
        
        hot_numbers = sorted(number_freq.items(), key=lambda x: x[1], reverse=True)[:3]
        cold_numbers = sorted(number_freq.items(), key=lambda x: x[1])[:3]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("🔥 Hot Numbers")
            for num, freq in hot_numbers:
                st.markdown(f'<div class="trend-indicator hot-number">{num} ({freq}x)</div>', 
                          unsafe_allow_html=True)
        with col2:
            st.markdown("❄️ Cold Numbers")
            for num, freq in cold_numbers:
                st.markdown(f'<div class="trend-indicator cold-number">{num} ({freq}x)</div>', 
                          unsafe_allow_html=True)

    @staticmethod
    def render_lucky_numbers(numbers: List[int]):
        """Render lucky numbers with animations"""
        if not numbers:
            return
            
        st.markdown("### 🍀 Lucky Numbers")
        cols = st.columns(len(numbers))
        for idx, num in enumerate(numbers):
            with cols[idx]:
                st.markdown(f'<div class="lucky-number">{num}</div>', unsafe_allow_html=True) 