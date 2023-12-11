from SimpleStack import Stack  # Import the Stack class from SimpleStack.py

# Test program for the revised Stack class
if __name__ == "__main__":
    max_stack_size = 3
    my_stack = Stack(max_stack_size)

    # Push items onto the stack
    for i in range(max_stack_size):
        my_stack.push(i)
        print(f"Pushed {i} onto the stack. Stack: {my_stack}")

    # Try pushing one more item (should raise an exception)
    try:
        my_stack.push(max_stack_size)
    except Exception as e:
        print(f"Error: {e}")

    # Pop items from the stack
    while not my_stack.isEmpty():
        popped_item = my_stack.pop()
        print(f"Popped {popped_item} from the stack. Stack: {my_stack}")

    # Try popping from an empty stack (should raise an exception)
    try:
        my_stack.pop()
    except Exception as e:
        print(f"Error: {e}")
