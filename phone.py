class Phone:
    
    def __init__(self, name, battery, screen, status, is_active):
        self.name = name
        self.battery = battery
        self.screen = screen
        self.status = status
        self.is_active = is_active

    def check_status(self):
        if self.status == "active":
            return self.status
        else:
            return False
    