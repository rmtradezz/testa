### sim_trader.py

import random
from datetime import datetime
from config import *

class SimulatedTrader:
    def __init__(self):
        self.sol_balance = INITIAL_SOL_BALANCE
        self.aud_profit = 0
        self.daily_trades = []

    def is_peak_hour(self):
        return datetime.utcnow().hour in PEAK_HOURS_UTC

    def can_trade(self):
        max_alloc = self.sol_balance * MAX_TRADE_ALLOCATION_PCT
        return max_alloc >= 0.01  # Don't trade if you can't spare 0.01 SOL

    def fake_price_movement(self):
        # Simulate random win or loss
        return random.choice(["win", "loss"])

    def run_trade(self, token):
        if not self.can_trade():
            print(f"[SKIP] Not enough SOL to trade {token}")
            return

        entry_price = random.uniform(0.1, 1.0)
        sol_used = self.sol_balance * MAX_TRADE_ALLOCATION_PCT
        stop_loss_price = entry_price * (1 - STOP_LOSS_PERCENT)
        take_profit_price = entry_price * (1 + TAKE_PROFIT_PERCENT)

        result = self.fake_price_movement()
        exit_price = take_profit_price if result == "win" else stop_loss_price
        percent_change = (exit_price - entry_price) / entry_price

        pnl_sol = sol_used * percent_change
        self.sol_balance += pnl_sol
        pnl_aud = pnl_sol * AUD_PER_SOL
        self.aud_profit += pnl_aud

        print(f"[{token}] {'✅ WIN' if result == 'win' else '❌ LOSS'}: {pnl_sol:.4f} SOL → ${pnl_aud:.2f} AUD")
        print(f"   Balance: {self.sol_balance:.4f} SOL | AUD Profit Today: ${self.aud_profit:.2f}")
