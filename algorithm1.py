def steffen_boarding_method(rows, seats_per_row):
    # Create a list to hold the boarding order
    boarding_order = []

    # Loop through each row
    for row in range(rows, 0, -1):
        # Loop through each seat in the row
        for seat in range(1, seats_per_row + 1):
            # Add the seat to the boarding order
            boarding_order.append((row, seat))

    return boarding_order

if __name__ == "__main__":
    rows = 5
    seats_per_row = 3

    boarding_order = steffen_boarding_method(rows, seats_per_row)

    for seat in boarding_order:
        print("Row:", seat[0], ", Seat:", seat[1])
