import streamlit as st
from backend import get_all_seats, main

def main():
    st.title("Bus Seat Reservation System")

    st.write("""
        This is a bus seat reservation system that allows you to book seats in buses.
        Please select your preferred seat type and position.
    """)


    seats = get_all_seats()

    if len(seats) == 0:
        st.error("No seats available at the moment.")
        return

    selected_seat = None

    with st.form(key="seatReservationForm"):
        # Seat type options (Window, Aisle, Center)
        seat_type_options = ['Window', 'Aisle', 'Center']
        
        current_seat_type = st.selectbox("Select Seat Type", seat_type_options)

        if len(current_seat_type) > 0:
            current_seat_position = st.number_input("Seat Position:", min_value=1, max_value=20)
            
            # Check seat availability
            available_seats = [seat for seat in seats 
                              if (seat["available"] and 
                                  seat["seat_type"] == current_seat_type)]
            
            if len(available_seats) > 0:
                selected_seat = {
                    "seat_type": current_seat_type,
                    "seat_position": current_seat_position
                }

        # Submit button
        if st.form_submit():
            # Make booking logic here
            print(f"Booking {selected_seat['seat_type']}, {selected_seat['seat_position']}")

    st.write(f"""
    ### Selected Seats:
    {selected_seat}
    """)
    
if __name__ == "__main__":
    main()