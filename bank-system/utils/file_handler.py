
import json
class FileHandler:
    def load_account_data():
        try:
            with open("accounts.json", "r") as file:
                lines = json.load(file)
        except FileNotFoundError:
            lines = []
        except json.JSONDecodeError:
            lines = []
        return lines

    def save_account_data(lines):
        with open("accounts.json", "w") as file:
            json.dump(lines, file)
