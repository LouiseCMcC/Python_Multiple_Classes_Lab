class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return len(self.queue)
    
    
    def add_to_queue(self, new_passenger):
        self.queue.append(new_passenger)

    def clear(self):
        self.queue.clear()

    def pick_up_from_stop(self, bus_stop1):
        for passenger in bus_stop1.queue:
            self.passengers.append(passenger)
        bus_stop1.queue.clear()
