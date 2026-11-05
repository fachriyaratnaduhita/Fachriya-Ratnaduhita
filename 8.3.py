def make_shirt(size, message):
    """Summarize the size and message of the shirt."""
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")

# Using positional arguments
make_shirt("Medium", "Good Mood!")

# Using keyword arguments
make_shirt(size="Large", message="Stay Healthy!")