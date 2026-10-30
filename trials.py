def budget_remaining(budget , food, transport):
    remaining = budget - food - transport
    return remaining 
    
  
  
  #Function 2 
  
def budget_message(name, remaining):
      message = f"{name} has {remaining} naira remaining."
      return message
    
    
    #Test case
    
print("----Test 1 : normal case ---")
remaining_amount = budget_remaining(2000, 900 , 600)
print("Remaining value:", remaining_amount)

message = budget_message ("ada", remaining_amount)
print("Message:", message)

print("/n --- Test 2: Zero case ---")
zero_remaining = budget_remaining (1500, 0, 0)
print("Remainig value:", zero_remaining)
print("Message:", budget_message("John", zero_remaining))

print("/n--- Test 3: Overspend case----")

overspend_remaining = budget_remaining (1000, 800, 200)
print("Remaining value:", overspend_remaining)
print("Message:", budget_message("Tobi", overspend_remaining))

