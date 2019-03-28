def solution(total_money, total_demage, costs, damages):
    n=len(costs)
    for i in range(n):
        for j in range(n):
            if(costs[i]<costs[j]):
                temp=costs[i]
                costs[i]=costs[j]
                costs[j]=temp
                temp=damages[i]
                damages[i]=damages[j]
                damages[j]=temp
    money_used=0
    damage_made=0
    for i in range(n):
        for j in range(n):
            money_used=money_used+costs[i]
            if (money_used>total_money):
                break
            damage_made=damage_made+damages[j]
            if(money_used<=total_money and damage_made>=total_demage):
                return True
    return False

print(solution(5,3,[4,5,1],[1,2,3]))