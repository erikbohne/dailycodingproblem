"""
may 4th 2023

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
class API_log:
    def __init__(self, N):
        self.order_id = []
        self.cap = N
    
    def record(self, order_id):
        if len(self.order_id) == self.cap:
            self.order_id.remove(self.order_id[0])
            self.order_id.append(order_id)
        else:
            self.order_id.append(order_id)
        
    def get_last(self, i):
        return self.order_id[-i]

log = API_log(3)
log.record(666)
log.record(777)
log.record(888)
log.record(999)
log.record(234)

print([log.get_last(i) for i in range(1, 4)]) # Only outputs the three last order_ids like LIFO
