#Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_number = reg_num
        self.type = vehicle_type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated: Vehicle {self.registration_number} is now owned by {self.owner}")


# Demonstration
if __name__ == "__main__":
    # Creating instances of Vehicle
    vehicle1 = Vehicle("ABC123", "Car", "Alice")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Bob")
    
    # Display initial ownership
    print(f"Initial Ownership:")
    print(f"Vehicle {vehicle1.registration_number} is owned by {vehicle1.owner}")
    print(f"Vehicle {vehicle2.registration_number} is owned by {vehicle2.owner}")
    print()
    
    # Changing ownership
    vehicle1.update_owner("Carol")
    vehicle2.update_owner("David")
    
    # Display updated ownership
    print(f"\nUpdated Ownership:")
    print(f"Vehicle {vehicle1.registration_number} is now owned by {vehicle1.owner}")
    print(f"Vehicle {vehicle2.registration_number} is now owned by {vehicle2.owner}")

#Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count

# Demonstration
if __name__ == "__main__":
    # Create an instance of Event
    event = Event("Birthday Party", "2024-07-04")
    
    # Add participants
    event.add_participant()
    event.add_participant()
    event.add_participant()
    
    # Retrieve and print participant count
    print(f"{event.name} on {event.date} has {event.get_participant_count()} participants.")