import matplotlib.pyplot as plt

class DigitalWellnessAnalyzer:

    def __init__(self):
        self.screen_time = {}

    def collect_data(self):
        print("\n===== DIGITAL WELLNESS & SCREEN TIME ANALYZER =====\n")

        apps = [
            "YouTube",
            "Instagram",
            "WhatsApp",
            "Gaming",
            "Netflix",
            "Study Apps"
        ]

        for app in apps:
            hours = float(input(f"Enter daily hours spent on {app}: "))
            self.screen_time[app] = hours

    def calculate_total_time(self):
        return sum(self.screen_time.values())

    def most_used_app(self):
        return max(self.screen_time, key=self.screen_time.get)

    def productivity_score(self):
        study_hours = self.screen_time["Study Apps"]
        total_hours = self.calculate_total_time()

        score = (study_hours / total_hours) * 100

        return round(score, 2)

    def wellness_level(self):

        score = self.productivity_score()

        if score >= 50:
            return "Excellent"

        elif score >= 30:
            return "Good"

        else:
            return "Needs Improvement"

    def generate_report(self):

        print("\n========== DIGITAL WELLNESS REPORT ==========\n")

        for app, time in self.screen_time.items():
            print(f"{app} : {time} Hours")

        print("\n-------------------------------------")
        print("Total Screen Time :", self.calculate_total_time(), "Hours")
        print("Most Used App     :", self.most_used_app())
        print("Productivity Score:", self.productivity_score(), "%")
        print("Wellness Level    :", self.wellness_level())
        print("-------------------------------------")

    def show_bar_chart(self):

        apps = list(self.screen_time.keys())
        hours = list(self.screen_time.values())

        plt.figure(figsize=(8, 5))
        plt.bar(apps, hours, color="skyblue")

        plt.title("App Wise Screen Time Analysis")
        plt.xlabel("Applications")
        plt.ylabel("Hours")

        plt.grid(True)

        plt.show()

    def show_pie_chart(self):

        apps = list(self.screen_time.keys())
        hours = list(self.screen_time.values())

        plt.figure(figsize=(7, 7))

        plt.pie(
            hours,
            labels=apps,
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Screen Time Distribution")

        plt.show()


# Main Program

obj = DigitalWellnessAnalyzer()

obj.collect_data()

obj.generate_report()

obj.show_bar_chart()

obj.show_pie_chart()