def days_to_reach_target(target, daily_deposite):
    if target <= 0:
        return 0

    balance = 0
    days = 0

    while balance < target:
        balance += daily_deposite
        days += 1
        
    return days