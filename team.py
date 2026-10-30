#component A

def participant_cost(attendees, food_per_person, transport_per_person):
    cost_per_person = food_per_person + transport_per_person
    total_partitcipant_cost = attendees * cost_per_person
    return total_partitcipant_cost


#Component B

def event_total(attendees, food_per_person,transport_per_person, venue_cost):
    people_cost = participant_cost(attendees, food_per_person,transport_per_person, )
    combined_total = people_cost + venue_cost
    return combined_total


# Component C
def budget_status (budget, total):
    if total <= budget:
        return "Within budget"
    
    else:
        return "Over budget"
    
    
    # component D 
    
def event_summary (event_name, total, status):
        summary = f"{event_name}: total {total} naira {status}."
        return summary
    
    
    # Test cases
    
people = participant_cost(10, 800 , 200)
print (people)

total = event_total (10, 800, 200, 5000)
print(total)


status = budget_status (16000 , total)
print (status)


summary = event_summary( "Study Day", total, status)
print(summary)
    
print("--------Testing participant_cost ------")
# normal attendee count
normal_people = participant_cost(10, 800, 200)
print("Normal (10 people ): expected 10000 | Actual : {normal_people}")

#2 Zero Attendance 
Zero_people = participant_cost(0, 800, 200)
print(f"Zero(0 people):  Expected 0 | Actual :{Zero_people}")


#3   

print("/n ------ Testing event_total ---")
    
normal_total = event_total (10, 800,200, 5000)
print(f"Normal:        Expected 15000 | Actual :  {normal_total}")


# zero Attendance with a non zero venue

zero_total = event_total(0, 800, 200, 5000)

print(f"Zero attendees:     Expected 5000  | Actual : {zero_total}")




print("/n---- Testing budget_status -----")

#  Below Budget

status_below = budget_status (16000 , 15000)
print(f" Below Budget :  expected 'Within budget' | Actual : '{status_below}'")

# Exact budget 
status_exact = budget_status(15000, 15000)
print(f"Exact Budget:    Expected 'within budget' |Actual:'{status_exact}'")


#Over Budget

status_over =(budget_status(10000, 15000))

print(f"Over Budget:  Expected 'Over budget'  |Actual :'{status_over}")


#Testing Event Summary


print("/n----- Testing event_summary-----")

# Required Example 
Summary_example = event_summary("Study Day", 15000, "Within budget")

print(f"Example : Expected 'Study Day':  total 15000 naira. Within budget, '")
print(f"                                Actual :  '{Summary_example}")


#On a different event name and total 
summary_diff = event_summary(" Wedding", 50000, "Over budget")
print(f"different :Expected 'Wedding: total 50000 naira. over budget.'")

print(f"      Actual: '{summary_diff}'")
    
    
    
    
    
    