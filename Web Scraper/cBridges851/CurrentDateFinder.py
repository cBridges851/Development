from datetime import date

class CurrentDateFinder():
    def __init__(self):
        pass

    def find(self):
        currentDate = date.today()
        day = currentDate.day

        return day