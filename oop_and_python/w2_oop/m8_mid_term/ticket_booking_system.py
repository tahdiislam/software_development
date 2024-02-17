# cinema hall ticket booking system
class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, row, col, hall_no) -> None:
        self._seats = {}
        self.show_list = []
        self.__row = row
        self.__col = col
        self._hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movie_name, time):
        new_show = id, movie_name, time
        self.show_list.append(new_show)
        new_seats = [[0 for _ in range(self.__col)] for _ in range(self.__row)]
        self._seats[id] = new_seats

    def show_id_validator(self, id):
        if id not in self._seats:
            print("Show id is invalid ❌\n")
            return False
        else:
            return True

    def book_seats(self, id, *args):
        if id not in self._seats:
            print("Show id is invalid ❌\n")
            return
        else:
            for tup in args:
                if (
                    tup[0] - 1 < 0
                    or tup[1] - 1 < 0
                    or tup[0] - 1 >= self.__row
                    or tup[1] - 1 >= self.__col
                ):
                    print("Seat row or column is invalid ❌\n")
                elif self._seats[id][tup[0] - 1][tup[1] - 1] == 1:
                    print("Seat is already booked ❌\n")
                else:
                    self._seats[id][tup[0] - 1][tup[1] - 1] = 1
                    print(f"Seat ({tup[0]}, {tup[1]})booked successfully ✅ \n")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show Name: {show[1]}, Show ID: {show[0]}, Show Time: {show[2]}")
        print("\n")

    def view_available_seats(self, id):
        if id not in self._seats:
            print("Show id is invalid ❌\n")
            return
        else:
            for col in self._seats[id]:
                print(col)
            print("\n")

ak_cinema = Hall(8, 8, 1)
ak_cinema.entry_show(301, "Osomoy", "14/2/24 3:00PM")
ak_cinema.entry_show(302, "Mohanagar", "14/2/24 5:00PM")
ak_cinema.entry_show(303, "hawa", "15/2/24 5:00PM")

while True:
    print("Options:")
    print("1. View all show today")
    print("2. View available seats")
    print("3. Book ticket")
    print("4. exit \n")
    opt = int(input("Enter option: "))
    print("\n")
    if opt == 4:
        break
    elif opt == 1:
        ak_cinema.view_show_list()
    elif opt == 2:
        show_id = int(input("Enter show ID: "))
        print("\n")
        ak_cinema.view_available_seats(show_id)
    elif opt == 3:
        show_id = int(input("Enter show ID: "))
        print("\n")
        if ak_cinema.show_id_validator(show_id):
            seat_num = int(input("Number of seat you want to book: "))
            print("\n")
            for i in range(0, seat_num):
                row = int(input("Enter row number: "))
                print("\n")
                col = int(input("Enter col number: "))
                print("\n")
                ak_cinema.book_seats(show_id, (row, col))
    else:
        print("Option is invalid ❌ \n")
