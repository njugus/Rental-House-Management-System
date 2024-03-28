class Tenant:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Tenant: {self.name}, Contact: {self.contact}"


class House:
    def __init__(self, house_id, address, rent, status='Available'):
        self.house_id = house_id
        self.address = address
        self.rent = rent
        self.status = status

    def __str__(self):
        return f"House ID: {self.house_id}, Address: {self.address}, Rent: ${self.rent:.2f}, Status: {self.status}"

    def rent_house(self):
        if self.status == 'Available':
            self.status = 'Rented'
            return True
        else:
            return False

    def release_house(self):
        if self.status == 'Rented':
            self.status = 'Available'
            return True
        else:
            return False


class HouseManagementSystem:
    def __init__(self):
        self.houses = []

    def add_house(self, house):
        self.houses.append(house)

    def rent_house(self, house_id):
        for house in self.houses:
            if house.house_id == house_id:
                return house.rent_house()
        return False

    def release_house(self, house_id):
        for house in self.houses:
            if house.house_id == house_id:
                return house.release_house()
        return False

    def display_houses(self):
        for house in self.houses:
            print(house)


# Example usage:
if __name__ == "__main__":
    # Creating house management system
    house_system = HouseManagementSystem()

    # Adding houses
    house1 = House(1, "123 Main St", 1000)
    house2 = House(2, "456 Park Ave", 1500)
    house_system.add_house(house1)
    house_system.add_house(house2)

    # Displaying available houses
    print("Available Houses:")
    house_system.display_houses()

    # Renting a house
    house_system.rent_house(1)

    # Displaying houses after renting
    print("\nHouses after renting:")
    house_system.display_houses()

    # Releasing a rented house
    house_system.release_house(1)

    # Displaying houses after releasing
    print("\nHouses after releasing:")
    house_system.display_houses()
