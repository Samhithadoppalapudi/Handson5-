
class MinHeap:
    def __init__(self):
        self.heap = []

    # Helper function to calculate parent index using bit manipulation
    def parent(self, i):
        return (i - 1) >> 1  # Equivalent to (i - 1) // 2

    # Helper function to calculate left child index using bit manipulation
    def left_child(self, i):
        return (i << 1) + 1  # Equivalent to 2 * i + 1

    # Helper function to calculate right child index using bit manipulation
    def right_child(self, i):
        return (i << 1) + 2  # Equivalent to 2 * i + 2

    # Function to heapify down the element at index i
    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            # Swap the elements
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # Recursively heapify the affected sub-tree
            self.heapify(smallest)

    # Function to build the heap from an arbitrary list of elements
    def build_min_heap(self, arr):
        self.heap = arr[:]
        for i in range((len(self.heap) - 1) >> 1, -1, -1):  # Start from last non-leaf node
            self.heapify(i)

    # Function to insert a new element into the heap
    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        # Move the element up if it is smaller than its parent
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Function to pop (remove) the minimum element (root)
    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if len(self.heap) > 0:
            self.heap[0] = last_value
            self.heapify(0)

        return min_value

    # Display the current state of the heap
    def display(self):
        print(self.heap)


# Test Example: Demonstrate all the functionality
if __name__ == "__main__":
    heap = MinHeap()

    # Example 1: Build heap from an array
    initial_data = [12, 3, 9, 5, 6, 10, 15]
    print("Building the heap from array:", initial_data)
    heap.build_min_heap(initial_data)
    heap.display()

    # Example 2: Insert elements
    print("\nInserting 1 into the heap:")
    heap.insert(1)
    heap.display()

    print("\nInserting 8 into the heap:")
    heap.insert(8)
    heap.display()

    # Example 3: Pop the minimum element
    print("\nPopping the min element:")
    print(f"Popped min element: {heap.pop_min()}")
    heap.display()

    print("\nPopping the min element again:")
    print(f"Popped min element: {heap.pop_min()}")
    heap.display()
