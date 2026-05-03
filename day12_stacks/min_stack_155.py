class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
    
if __name__ == "__main__":
    st = MinStack()

    st.push(5)
    st.push(3)
    st.push(7)
    st.push(2)

    print("Current Min:", st.getMin())  # 2

    st.pop()
    print("Top:", st.top())             # 7
    print("Current Min:", st.getMin())  # 3