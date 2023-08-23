class FlightTable:
    def __init__(self):
        self.flights = {
            "AI161E90": ("BLR", "BOM", 5600),
            "BR161F91": ("BOM", "BBI", 6750),
            "AI161F99": ("BBI", "BLR", 8210),
            "VS171E20": ("JLR", "BBI", 5500),
            "AS171G30": ("HYD", "JLR", 4400),
            "AI131F49": ("HYD", "BOM", 3499),
        }
        self.city_names = {
            "BLR": "Bengaluru",
            "BOM": "Mumbai",
            "BBI": "Bhubaneswar",
            "HYD": "Hyderabad",
            "JLR": "Jabalpur",
        }

    def search_flights_for_city(self, city):
        print("Flights for city:", self.city_names.get(city, "Unknown City"))
        for flight_id, (from_city, to_city, price) in self.flights.items():
            if from_city == city or to_city == city:
                print(f"Flight ID: {flight_id}, From: {self.city_names[from_city]}, To: {self.city_names[to_city]}, Price: {price}")

    def search_flights_from_city(self, from_city):
        print("Flights from city:", self.city_names.get(from_city, "Unknown City"))
        for flight_id, (from_city, to_city, price) in self.flights.items():
            if from_city == from_city:
                print(f"Flight ID: {flight_id}, To: {self.city_names[to_city]}, Price: {price}")

    def search_flights_between_cities(self, from_city, to_city):
        print("Flights between cities:", self.city_names.get(from_city, "Unknown City"), "and", self.city_names.get(to_city, "Unknown City"))
        for flight_id, (from_city, to_city, price) in self.flights.items():
            if from_city == from_city and to_city == to_city:
                print(f"Flight ID: {flight_id}, Price: {price}")


if __name__ == "__main__":
    flight_table = FlightTable()

    while True:
        print("\nSearch Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            city = input("Enter city code: ")
            flight_table.search_flights_for_city(city)
        elif choice == "2":
            from_city = input("Enter city code: ")
            flight_table.search_flights_from_city(from_city)
        elif choice == "3":
            from_city = input("Enter source city code: ")
            to_city = input("Enter destination city code: ")
            flight_table.search_flights_between_cities(from_city, to_city)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
