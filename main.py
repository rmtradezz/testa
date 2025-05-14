### main.py
import asyncio
import random
from sim_trader import SimulatedTrader

TOKENS = ["WIF", "FLOKI", "BONK", "GMGN", "BOZO", "TATE", "PUMP"]

async def main():
    trader = SimulatedTrader()

    while trader.aud_profit < DAILY_TARGET_AUD:
        if not trader.is_peak_hour():
            print("⏳ Waiting for peak trading hours...")
            await asyncio.sleep(5)
            continue

        tokens_to_trade = random.sample(TOKENS, k=3)
        print(f"\n🚀 Evaluating: {', '.join(tokens_to_trade)}")

        for token in tokens_to_trade:
            trader.run_trade(token)
            await asyncio.sleep(1)

        await asyncio.sleep(3)

    print("\n✅ Daily target reached. Shutting down.")

if __name__ == "__main__":
    asyncio.run(main())


