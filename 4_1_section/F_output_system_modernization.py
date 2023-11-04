def modern_print(message: str, pr_messages: list[str] = []):
    if message not in pr_messages:
        print(message)
        pr_messages.append(message)
