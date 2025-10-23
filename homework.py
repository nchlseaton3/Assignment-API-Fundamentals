#  Build a Bored Activity CLI App
# Create a Python file called homework.py
# Build a CLI menu that lets users choose different options
# Use the Bored API to get activity suggestions
# Handle user input and make appropriate API requests
# Test your menu system thoroughly
# Bored API: https://bored-api.appbrewery.com

import requests 

# Function 1: Get a random Activity

def get_random_activity():
    """Get a completely random activity suggestion."""
    try:
        response = requests.get("https://bored-api.appbrewery.com/random")
        response.raise_for_status()
        data = response.json()

        print("\nRandom Activity Suggestion:")
        print(f"Activity: {data['activity']}")
        print(f"Type: {data['type']}")
        print(f"Participants: {data['participants']}")
        print("Ready to try it?")

        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching activity:", e)
        return None
    
# Function 2: Get Activity by type

def get_activity_by_type():
    """Let user choose an activity type and get a suggestion."""
    activity_types = [
        "education", "recreational", "social", "diy",
        "charity", "cooking", "relaxation", "music", "busywork"
    ]
    print("\nAvailable Types:")
    for i, t in enumerate(activity_types, 1):
        print(f"{i}. {t}")

    choice = input("Choose an activity type (1-9): ")

    if not choice.isdigit() or not (1 <= int(choice) <= len(activity_types)):
        print("Invalid selection.")
        return None

    selected_type = activity_types[int(choice) - 1]

    try:
        response = requests.get(
            "https://bored-api.appbrewery.com/filter",
            params={"type": selected_type},
        )
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            suggestion = data[0]
            print(f"\nActivity: {suggestion['activity']}")
            print(f"Type: {suggestion['type']}")
            print(f"Participants: {suggestion['participants']}")
            return suggestion
        else:
            print("No activities found for that type.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error fetching activity:", e)
        return None



# CLI Menu System

def show_menu():
    print("\nBored Activity Finder")
    print("=" * 21)
    print("1. Get a random activity")
    print("2. Get activity by type")
    print("3. Get activity by participants")
    print("4. Save my favorite activities (after generating one)")
    print("5. View my saved activities")
    print("6. Exit")


def main():
    print("Welcome to the Bored Activity Finder!")

    while True:
        show_menu()
        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            activity = get_random_activity()
            if activity:
                save = input("Save this activity? (y/n): ").lower()
                if save == "y":
                    save_favorite_activity(activity)

        elif choice == "2":
            activity = get_activity_by_type()
            if activity:
                save = input("Save this activity? (y/n): ").lower()
                if save == "y":
                    save_favorite_activity(activity)

        elif choice == "3":
            activity = get_activity_by_participants()
            if activity:
                save = input("Save this activity? (y/n): ").lower()
                if save == "y":
                    save_favorite_activity(activity)

        elif choice == "4":
            print("Use options 1-3 to generate and then save an activity.")

        elif choice == "5":
            view_saved_activities()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1-6.")


# Program Entry Point

if __name__ == "__main__":
    main()