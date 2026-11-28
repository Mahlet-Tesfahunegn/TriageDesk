from app.agent import classify_ticket

def main():

    print("=" * 53)
    print("              Welcome to TriageDesk")
    print("=" * 53)

    while True:
        ticket = input("Enter your ticket (or type 'exit' to quit): ")

        if ticket.strip().lower() == "exit":
            print("Thank you for using TriageDesk. Goodbye!")
            break
        
        try: 
            if not ticket.strip():
                print("Error: Ticket cannot be empty. Please try again.")
                continue
            
            result = classify_ticket(ticket)

            matched_rules = (
                "None"
                if result["category"] == "Manual Review" and not result["matched_rules"]
                else ", ".join(result["matched_rules"])
            )
                
            print("\n" + "=" * 53)
            print("              TICKET CLASSIFICATION")
            print("=" * 53)
            print(f"Category:       {result['category']}")
            print(f"Priority:       {result['priority']}")
            print(f"Department:     {result['department']}")
            print(f"Matched Rules:  {matched_rules}")

            print(f"\nExplanation:\n{result['explanation']}")
            print(f"\nRecommended Action:\n{result['recommended_action']}")

            print("=" * 53)


        except ValueError as error:
            print(error)
                


if __name__ == "__main__":
    main()

