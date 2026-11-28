from app.agent import classify_ticket

ticket = "My refund has not arrived. And I cannot log in to my account"

result = classify_ticket(ticket)

print(result)