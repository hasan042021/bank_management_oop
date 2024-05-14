def demo_data(bank, User, Admin):
    user1 = User(
        "Alice Smith",
        "alice.smith@gmail.com",
        "123 Main St",
        "12345",
        "savings",
    )
    bank.add_user(user1)
    user2 = User(
        "Bob Johnson", "bob.johnson@gmail.com", "456 Elm St", "23456", "current"
    )
    bank.add_user(user2)
    user3 = User(
        "Charlie Brown",
        "charlie.brown@gmail.com",
        "789 Oak Ave",
        "34567",
        "savings",
    )
    bank.add_user(user3)
    user4 = User(
        "Diana Davis", "diana.davis@gmail.com", "1011 Pine Blvd", "45678", "current"
    )
    bank.add_user(user4)
    user5 = User(
        "Evan Garcia",
        "evan.garcia@gmail.com",
        "1213 Maple Ln",
        "56789",
        "savings",
    )
    bank.add_user(user5)

    admin1 = Admin("admin1", "admin1@gmail.com", "1 Admin Lane", "12345")
    bank.add_admin(admin1)
    admin2 = Admin("Jane Smith", "admin2@gmail.com", "2 Admin Ave", "23456")
    bank.add_admin(admin2)
    admin3 = Admin("David Lee", "admin3@gmail.com", "3 Admin St", "34567")
    bank.add_admin(admin3)
