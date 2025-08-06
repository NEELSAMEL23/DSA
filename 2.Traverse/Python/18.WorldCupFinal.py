def world_cup_final(NzScore, NzSuperOver, NzFours, EngScore, EngSuperOver, EngFours):
    if NzScore > EngScore:
        print("New Zealand")
    elif NzScore < EngScore:
        print("England")
    elif NzSuperOver > EngSuperOver:
        print("New Zealand")
    elif NzSuperOver < EngSuperOver:
        print("England")
    elif NzFours > EngFours:
        print("New Zealand")
    elif NzFours < EngFours:
        print("England")

# Hardcoded input
NzScore = 241
NzSuperOver = 15
NzFours = 21

EngScore = 241
EngSuperOver = 15
EngFours = 26

world_cup_final(NzScore, NzSuperOver, NzFours, EngScore, EngSuperOver, EngFours)
