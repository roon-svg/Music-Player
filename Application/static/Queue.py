# This is where
class Queue:
    def __init__(self, max_size):
        self.queue = [None] * max_size  # Fixed-size array
        self.max_size = max_size # Sets the maximum size of the Queue
        self.front = -1  # Tracks the front element
        self.rear = -1   # Tracks the rear element
        self.size = 0    # Tracks the current number of elements
        self.pointer = 0 # Gets the current song

    # If the queue is it will return 0
    def is_empty(self):
        return self.size == 0

    # If the Queue is full then this function will return the maximum allowed size
    def is_full(self):
        return self.size == self.max_size

    # This adds a new element into the queue
    def enqueue(self, value):
        if self.is_full():
            return

        if self.is_empty():
            # First element to be enqueued
            self.front = 0
            self.rear = 0
        else:
            # Move rear to the next position in a circular manner
            self.rear = (self.rear + 1) % self.max_size

        # Insert the new value and update the size
        self.queue[self.rear] = value
        self.size += 1

    # This removes the element at the back fo the queu
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None

        value_to_return = self.queue[self.front]
        self.queue[self.front] = None  # Clear the dequeued position

        if self.front == self.rear:
            # Queue becomes empty after this dequeue
            self.front = -1
            self.rear = -1
        else:
            # Move front to the next position in a circular manner
            self.front = (self.front + 1) % self.max_size

        self.size -= 1
        print(f"Dequeued: {value_to_return}")
        return value_to_return
    
    # This returns the size of the queue
    def QueueSize(self):
        return self.size
    
    # This moves the pointer into the next element in the queue
    def next_element(self):
        try:
            self.pointer = self.pointer + 1
            if self.queue[self.pointer] == None:
                self.pointer = self.rear
        except:
            self.pointer = self.rear
        return self.queue[self.pointer]

    # This moves the pointer into the previous element in the queue
    def previous_element(self):
        try:
            self.pointer = self.pointer - 1
            if self.queue[self.pointer] == None:
                self.pointer = self.front
        except:
            self.pointer = self.front
        return self.queue[self.pointer]
    
    # This returns the element in the pointer
    def element_pointer(self):
        return str(self.queue[self.pointer])
    
    # This returns the elements in the queue as a python list
    def queue_elements(self):
        return self.queue