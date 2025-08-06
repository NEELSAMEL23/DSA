def listQueueOperation(commands, n):
    queue = []
    dequeue = []
    
    for command in commands:
        command = command.split()

        if command[0] == "E":
            queue.append(command[1])
        elif command[0] == "D":
            if queue == []:
                dequeue.append("Empty!")
            else:
                dequeue.append(queue.pop(0))

    return "\n".join(dequeue)
                

n = 4      
commands = ["E 2", "E 3", "D", "D"]
res = listQueueOperation(commands, n)
print(res) 