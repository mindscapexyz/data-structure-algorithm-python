import tasks
import printer
import random
import queues


def simulation(num_seconds, pages_per_minute):
    lab_printer = printer.Printer(pages_per_minute)
    print_queue = queues.Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = tasks.Task(current_second)
            print("New task with current sec:", current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print(
        f"Average Wait %6.2f secs %3d tasks remaining.",
        average_wait,
        print_queue.size(),
    )


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
