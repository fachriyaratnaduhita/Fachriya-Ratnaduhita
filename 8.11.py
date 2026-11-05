


def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Good Morning!", "How are you today?", "Keep study!"]
sent_messages = []

# Passing a copy of the messages list using [:]
send_messages(messages[:], sent_messages)

print("\nFinal Lists:")
print("Messages (Original):", messages)
print("Sent Messages:", sent_messages)