def participant_cost(attendees, food_per_person, transport_per_person):
    cost_per_person= food_per_person + transport_per_person
    total_participant_cost = attendees * cost_per_person
    return total_participant_cost

people = participant_cost(10, 800, 200)
print (people)

#normal attendance
normal_people = participant_cost(10, 800, 200)
print("normal (10 people): expected 10000 / actual : {normal_people}")

#zero attendance
zero_people = participant_cost (0, 800, 200)
print("zero people): expected 0| actual :{zero_people}")