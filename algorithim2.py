def ImprovedBoarding(rows, seats_per_row):
    boarding_order = []

    def AssignSeatsOptimally(rows, seats_per_row):
        seat_assignments = {}
        for row in range(1, rows + 1):
            for seat in range(1, seats_per_row + 1):
                seat_assignments[f'Passenger_{row}_{seat}'] = (row, seat)
        return seat_assignments

    def GetPriorityPassengers():
        priority_passengers = ['Passenger_1_1', 'Passenger_2_2']
        return priority_passengers

    def AssignPriorityBoardingOrder(priority_passengers):
        return priority_passengers

    def PerformPreBoardingProcedures():
        pass

    def CommunicateBoardingInstructions():
        pass

    seat_assignments = AssignSeatsOptimally(rows, seats_per_row)

    priority_passengers = GetPriorityPassengers()

    priority_boarding_order = AssignPriorityBoardingOrder(priority_passengers)

    PerformPreBoardingProcedures()

    CommunicateBoardingInstructions()

    for passenger in priority_boarding_order:
        boarding_order.append(seat_assignments[passenger])

    for passenger in seat_assignments:
        if passenger not in priority_boarding_order:
            boarding_order.append(seat_assignments[passenger])

    return boarding_order

def main():
    rows = [5, 10, 20]
    seats_per_row = [3, 5, 10]

    for rows, seats_per_row in zip(rows, seats_per_row):
        boarding_order = ImprovedBoarding(rows, seats_per_row)

        print(f"Boarding order for {rows} rows and {seats_per_row} seats per row:")
        for i, seat in enumerate(boarding_order, start=1):
            print(f"Passenger {i}: Row {seat[0]}, Seat {seat[1]}")
        print()

if __name__ == "__main__":
    main()
