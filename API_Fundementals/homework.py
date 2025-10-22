#  Build a Bored Activity CLI App
import re 


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
            print("Use options 1–3 to generate and then save an activity.")

        elif choice == "5":
            view_saved_activities()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1–6.")


# ------------------------------------------------------------
# Program Entry Point
# ------------------------------------------------------------
if __name__ == "__main__":
    main()