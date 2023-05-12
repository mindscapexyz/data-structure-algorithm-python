import queues


def hot_potato(name_list, num):
    sim_queue = queues.Queue()
    for name in name_list:
        sim_queue.enqueue(name)
        print(name)

    while sim_queue.size() > 1:
        for i in range(num):
            x = sim_queue.dequeue()
            print("Dequeue and enqqued is: ", x)
            sim_queue.enqueue(x)

        z = sim_queue.dequeue()
        print("Gone forever:", z)

    return print("Survivor:", sim_queue.dequeue())


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 3))
