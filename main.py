import matplotlib.pyplot as plt
from datetime import datetime

class HabitTracker:
    def __init__(self):
        self.habits = {}

    def add_habit(self, habit_name):
        if habit_name not in self.habits:
            self.habits[habit_name] = {'dates': [], 'statuses': []}
            print(f"Habit '{habit_name}' added successfully.")
        else:
            print(f"Habit '{habit_name}' already exists.")

    def mark_complete(self, habit_name):
        if habit_name in self.habits:
            self.habits[habit_name]['dates'].append(datetime.now().date())
            self.habits[habit_name]['statuses'].append('completed')
            print(f"Habit '{habit_name}' marked as completed.")
        else:
            print(f"Habit '{habit_name}' does not exist.")

    def visualize_progress(self):
        for habit_name, data in self.habits.items():
            dates = data['dates']
            statuses = data['statuses']
            streak = 0
            streaks = []

            if not dates or not statuses:
                print(f"Habit '{habit_name}' has no completed or skipped days. Skipping visualization.")
                continue

            for status in statuses:
                if status == 'completed':
                    streak += 1
                else:
                    streaks.append(streak)
                    streak = 0
                streaks.append(streak)

            plt.plot(dates, streaks, label=habit_name)

        plt.xlabel('Date')
        plt.ylabel('Streak')
        plt.title('Habit Tracker Progress')
        plt.legend()
        plt.show()

def main():
    tracker = HabitTracker()

    while True:
        print("\n===== Habit Tracker Menu =====")
        print("1. Add Habit")
        print("2. Mark Habit as Completed")
        print("3. Visualize Progress")
        print("4. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            habit_name = input("Enter the name of the habit you want to add: ")
            tracker.add_habit(habit_name)
        elif choice == '2':
            habit_name = input("Enter the name of the habit you completed: ")
            tracker.mark_complete(habit_name)
        elif choice == '3':
            if tracker.habits:
                tracker.visualize_progress()
            else:
                print("No habits added yet. Please add habits first.")
        elif choice == '4':
            print("Exiting Habit Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
