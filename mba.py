'''def goal_contribution(player_name,goals,assists):
    total_contribution=goals+assists
    print(f"{player_name} contributed {total_contribution} times (Goals : {goals}, Assists: {assists} in the Match")
goal_contribution('Kylian Mbappé',3,3)
goal_contribution('Kevin De Bruyne',1,2)
goal_contribution('Vinicius Junior',2,1)
print(goal_contribution.__doc__)'''

def cal_bill(bill_amount,tip_percent=5):
    tip_amount=(bill_amount*tip_percent)/100
    total_amount=bill_amount+tip_amount
    return total_amount,tip_amount

def food_checklist(*items):
    print("\nOrdered food Checklist: ")
    for i in items:
        print(f"- {i}")

def spill_bill(total_amount,num_people):
    if num_people==0:
        return "Number of people cannot be zero"
    per_person=total_amount/num_people
    return per_person

def restaurant_payment(bill_amount,tip_percent=15,num_people=1,*fooditems):
    food_checklist(*fooditems)
    total_bill,tip_amount=cal_bill(bill_amount,tip_percent)
    per_person_cost=spill_bill(total_bill,num_people)

    print(f" Original Bill Amount: ${total_bill}")
    print(f" Tip Amount: ${tip_amount}")
    print(f" Spill Bill: ${per_person_cost}")

restaurant_payment(100,18,3,"Burger","Pizza","Shawarma")
restaurant_payment(200,20,1,"Steak","Cake","Dessert")