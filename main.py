from fastapi import FastAPI
import random

app = FastAPI()

money_tips = [
    "Pay yourself first: Save at least 20% of your income before spending.",
    "Avoid impulse buying—wait 24 hours before making a big purchase.",
    "Invest early: Compound interest is the key to long-term wealth.",
    "Create a monthly budget and track your expenses.",
    "Use the 50/30/20 rule: 50% needs, 30% wants, 20% savings.",
    "Diversify your investments—don't put all your money in one place.",
    "Avoid unnecessary debt—only borrow for things that appreciate in value.",
    "Build an emergency fund with at least 6 months of expenses.",
    "Negotiate your bills—many companies offer better rates if you ask.",
    "Live below your means and avoid lifestyle inflation.",
    "Learn about tax-saving strategies to keep more of your money.",
    "Buy quality over quantity—spend wisely on things that last longer.",
    "Automate your savings and investments to make wealth-building effortless.",
]

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

@app.get("/")
def read_root():
    return {
        "message": "Hello World, Go to /money_tips or /side_hustles to get a random money_tips or side_hustles"
    }

@app.get ("/money_tips")
def get_money_tips():
    """Returns a random money tips idea"""
    return {"money_tips": random.choice(money_tips)}


@app.get ("/side_hustles")
def get_side_hustles():
    """Returns a random side hustles idea""" 
    return {"side_hustles": random.choice(side_hustles)}
