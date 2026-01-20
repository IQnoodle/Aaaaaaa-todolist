"""Main entry point for the Todo List application."""

import sys
from auth import AuthManager


class App:
    """Main application class for the Todo List CLI."""

    def __init__(self):
        """Initialize the application."""
        self.running = True
        self.auth_manager = AuthManager("users.json")
        self.current_user = None

    def display_pre_login_menu(self) -> None:
        """Display the pre-login menu and handle user input."""
        while self.running:
            print("\n" + "=" * 40)
            print("Welcome to Todo List Application")
            print("=" * 40)
            print("[1] Login")
            print("[2] Sign Up")
            print("[3] Exit")
            print("=" * 40)

            choice = input("\nEnter your choice (1-3): ").strip()

            if choice == "1":
                self.login()
            elif choice == "2":
                self.sign_up()
            elif choice == "3":
                self.exit_app()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def login(self) -> None:
        """Handle user login."""
        print("\n--- Login ---")
        username = self.auth_manager.login()
        if username:
            self.current_user = username
            print("Redirecting to main menu...")
            # TODO: Implement main menu for authenticated users
        else:
            print("Login cancelled or failed.")

    def sign_up(self) -> None:
        """Handle user sign up."""
        print("\n--- Sign Up ---")
        if self.auth_manager.sign_up():
            print("You can now log in with your new account.")
        else:
            print("Sign up failed.")

    def exit_app(self) -> None:
        """Exit the application."""
        print("\nThank you for using Todo List Application. Goodbye!")
        self.running = False
        sys.exit(0)

    def run(self) -> None:
        """Start the main application loop."""
        self.display_pre_login_menu()


def main() -> None:
    """Application entry point."""
    app = App()
    app.run()


if __name__ == "__main__":
    main()
