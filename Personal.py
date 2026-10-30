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
    
    

#status = budget_status (16000 , total)
#print (status)


#summary = event_summary( "Study Day", total, status)
#print(summary)



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
    
    