from weboodi.period import Period


def main():
    period = Period()
    print("write exit to end program")
    print("Commands:")
    print("add <course code>")
    print("event <weekday> <time>-<time>")
    print("select")
    print("reset")
    print("exit")
    command = ""
    while command.lower() != "exit":
        command = input("")
        if "add" in command:
            code = command.split(" ")[-1]
            period.add_course_by_code(code)
        elif command == "select":
            period.make_selections()
            print(period.results)
        elif command == "reset":
            period = Period()
        elif "event" in command:
            period.add_block_to_calendar(command[command.index(" ")+1:])