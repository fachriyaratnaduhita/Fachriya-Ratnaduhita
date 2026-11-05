def make_shirt(size='Large', message='I love Python'):
    """Summarize the shirt details with default values."""
    print(f"The shirt size is {size} and it has the message: '{message}' printed on it.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size='Medium')

# Custom size and custom message
make_shirt(size='Small', message='Sunday Morning')