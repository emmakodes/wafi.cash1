from models import User, users

def add_user(name):
    """Add a new user"""
    user = User(name)
    users.append(user)
    return user

def deposit_money(user, amount):
    """Deposit a user's money"""
    user.balance += amount

def send_money(sender, receiver, amount):
    """Send a user's money"""
    sender.balance -= amount
    receiver.balance += amount

def check_balance(user):
    """Check if a user has enough money"""
    return user.balance

def transfer_money_out(user, amount):
    """transfer a user's money"""
    user.balance -= amount
