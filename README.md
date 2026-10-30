Component owned:budget_status
what it returns?:  Returns the string "Within budget when total is less than or equal to budget, otherwise returns "Over budget" 
Test run : Tested below budget (16000, 15000) exactly equal (15000, 15000), ad over budget (10000, 15000).
Any assumptions or unresolved issue:None assumes inputs are integers



Component owned : Event_summary
What it returns: Returns a formatted readable string combining the event name, total cost, and budget status.

Test run: Required example ("Study Day", 15000, "Within budget) -> Expected Study Day : total 15000 naira within budget,", Actual matches.
Different name/total ("Wedding", 50000. "over budget")-> actual matches

Any assumptions or unresolved issues:Requires exactly three arguments in the order specified. Uses python f-strings for formatting.
