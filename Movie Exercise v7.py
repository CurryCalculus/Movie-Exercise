"""Movie theatre ticketing system -v7
Ensures vaid number entered for num_tickets
Created by Yuu Nakashima
"""


# Component 7 - integer checker. Loops until valid integer entered
def integer_checked(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# Component 6 - price summary
def print_summary(tickets_sold, adult_tickets, student_tickets, child_tickets,
                  gift_tickets, total_sales):
    print("="*20)
    print(f"The total tickets sold today was {tickets_sold}\n"
          f"This was made up of: \n"
          f"\t{adult_tickets} for adults; and\n"
          f"\t{student_tickets} for students and \n"
          f"\t{child_tickets} for children; and\n"
          f"\t{gift_tickets} gift vouchers\n"
          f"Sales for the day came to ${total_sales:.2f}")
    print("="*20)


# Component 4 - Confirm order
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have ordered {number} {ticket} ticket(s)!"
                        f"at a cost of ${cost * number:.2f}\n"
                        f"('Y' or 'N': ")
        if confirm == "Y":
            return True

        else:
            return False


#Component 3 - Calculate ticket price
def get_price(type_):
    prices = [["A", 12.5],["C", 7], ["S", 9], ["G", 0]]
    for price in prices:
        if price[0] == type_:
            return price[1]


# Component 1 -  Welcome screen and set up variables
def sell_ticket():
    print("********** Fanfare Movies - ticketing system **********\n")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sales = 0

    # Component 2 - Get the category and number of tickets required

    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket to you want: \n"
                            "\t 'A' for Adult, or\n"
                            "\t 'S' for Student, or\n"
                            "\t 'C' for Child, or\n"
                            "\t 'G' for Gift Voucher\n"
                            ">> ").upper()

        # Ensuring valid ticket type chosen
        valid_types = ["A", "S", "C", "G"]
        if ticket_type not in valid_types:
            print("not a valid ticket-type/n")
        else:
            num_tickets = integer_checker(f"How many '{ticket_type}' tickets do"
                                          f" you want: ")

            cost =get_price(ticket_type)

            if confirm_order(ticket_type, num_tickets, cost):
                print("Order confirmed")

                # Component 5 - Update Totals
                total_sales += cost
                tickets_sold += num_tickets
                if ticket_type == "A":
                    adult_tickets += num_tickets
                elif ticket_type == "S":
                    student_tickets += num_tickets
                elif ticket_type == "C":
                    child_tickets += num_tickets
                else:
                    gift_tickets += num_tickets
            else:
                print("Order cancelled")

        ticket_wanted = input("Do you want to sell another ticket? (Y/N): "
                              "").upper()

# Component 6 - produce summary of sales
    print_summary(tickets_sold, adult_tickets, student_tickets, child_tickets,
                  gift_tickets, total_sales)


# Main routine
sell_ticket()
print("Goodbye\nThanks for using Fanfare Movies")

