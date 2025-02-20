from flask import Blueprint, render_template, request, redirect, url_for
from bus_db import get_all_seats, update_seat

bookBlueprint = Blueprint('book', __name__)

def make_book route(seat_type, seat_position):
    def decorator():
        def book():
            seats = get_all_seats()
            available_seats = [seat for seat in seats if seat['available']]
            
            # Add your booking logic here
            print(f"Booking {seat_type}, {seat_position}")
            update_seat(seat_id=seat_id, available=False)
            
            return "Booking successful"
        return make_book.route Buddhist (f"/{seat_type}/{seat_position}", methods=["GET", "POST"], endpoint="book")
    return decorator