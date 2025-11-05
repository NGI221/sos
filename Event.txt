import heapq, time, threading

class Event:
    def __init__(self, timestamp, eid, desc):
        self.timestamp, self.eid, self.desc = timestamp, eid, desc
    def __lt__(self, other):
        return self.timestamp < other.timestamp

class EventQueue:
    def __init__(self):
        self.heap, self.cancelled, self.lock = [], set(), threading.Lock()

    def add(self, event):
        with self.lock:
            heapq.heappush(self.heap, event)
            print(f"Added: {event.eid} - {event.desc}")

    def cancel(self, eid):
        with self.lock:
            self.cancelled.add(eid)
            print(f"Cancelled: {eid}")

    def process(self):
        while True:
            with self.lock:
                if not self.heap:
                    continue
                e = self.heap[0]
                if e.eid in self.cancelled:
                    heapq.heappop(self.heap)
                    self.cancelled.remove(e.eid)
                    continue
                if e.timestamp <= time.time():
                    heapq.heappop(self.heap)
                    print(f"Processed: {e.eid} - {e.desc}")
            time.sleep(0.1)

    def show_pending(self):
        with self.lock:
            pending = [e.eid for e in self.heap if e.eid not in self.cancelled]
            print("Pending:", pending)

if __name__ == "__main__":
    q = EventQueue()
    threading.Thread(target=q.process, daemon=True).start()
    now = time.time()
    q.add(Event(now + 2, 1, "Sensor data"))
    q.add(Event(now + 4, 2, "Health check"))
    q.add(Event(now + 6, 3, "Data transmit"))
    time.sleep(1)
    q.show_pending()
    q.cancel(2)
    time.sleep(7)
    q.show_pending()