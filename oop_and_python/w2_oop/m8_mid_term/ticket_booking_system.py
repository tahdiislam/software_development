# cinema hall ticket booking system
class Hall:
    def __init__(self, row, col, hall_no) -> None:
        self._seats = {}
        self.show_list = []
        self.__row = row
        self.__col = col
        self._hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        new_show = id, movie_name, time
        self.show_list.append(new_show)
        new_seats = [[0 for _ in range(self.__col)] for _ in range(self.__row)]
        self._seats[id] = new_seats

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


class Star_Cinema:
    hall_list = []

    def entry_hall(self, row, col, hall_no):
        new_hall = Hall(row, col, hall_no)
        self.hall_list.append(new_hall)


ak_cinema = Star_Cinema()
ak_cinema.entry_hall(8, 8, 1)
ak_cinema.hall_list[0].entry_show(301, "Osomoy", "14/2/24 3:00PM")
ak_cinema.hall_list[0].entry_show(302, "Mohanagar", "14/2/24 5:00PM")
ak_cinema.hall_list[0].entry_show(303, "Leader", "15/2/24 3:00PM")
ak_cinema.hall_list[0].entry_show(304, "Hawa", "15/2/24 5:00PM")
ak_cinema.hall_list[0].entry_show(305, "Monpura", "16/2/24 3:00PM")
ak_cinema.hall_list[0].entry_show(306, "Friday", "16/2/24 5:00PM")

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
        ak_cinema.hall_list[0].view_show_list()
    elif opt == 2:
        show_id = int(input("Enter show ID: "))
        print("\n")
        ak_cinema.hall_list[0].view_available_seats(show_id)
    elif opt == 3:
        show_id = int(input("Enter show ID: "))
        print("\n")
        row = int(input("Enter row number: "))
        print("\n")
        col = int(input("Enter col number: "))
        print("\n")
        ak_cinema.hall_list[0].book_seats(show_id, (row, col))
    else:
        print("Option is invalid ❌ \n")
