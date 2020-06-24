# processing
class Person:
    def __init__(self, timeArrived: int, prepTime: int, priority: int):
        self.timeArrived = timeArrived
        self.prepTime = prepTime
        self.priority = priority
        self.timeWaited = 0
        self.finishedTime = 0
        self.inQueue = False
        self.beingServed = False
        self.finished = False

    def reportTime(self):
        return self.timeWaited

    def wait(self):
        self.timeWaited += 1

    def served(self):
        self.finishedTime += 1
        if self.finishedTime == self.prepTime:
            self.finished = True
            self.inQueue = False
            self.beingServed = False


def isSomeoneBeingServed(queueOfCustomers: list):
    for customer in queueOfCustomers:
        if customer.beingServed is True:
            return True
    return False


def FCFS(queueOfCustomers: list, numberOfCustomers: int):
    totalTime = 0
    currentTime = 0
    numOfPeopleServed = 0
    # sort customers by priority and time arrived
    queueOfCustomers = sorted(
        queueOfCustomers, key=lambda x: (-x.priority, x.timeArrived)
    )
    while numOfPeopleServed != numberOfCustomers:
        numOfPeopleServed = 0
        for customer in queueOfCustomers:
            if customer.inQueue is True:  # add time to those in queue
                customer.wait()
            if customer.beingServed is True:  # subtract time from those being served
                customer.served()
            if customer.finished is True:  # add finished to people served
                numOfPeopleServed += 1
            if customer.timeArrived <= currentTime:  # set who is in queue
                if customer.finished is False:
                    customer.inQueue = True
        for customer in queueOfCustomers:
            if isSomeoneBeingServed(queueOfCustomers) is False:  # set served
                if customer.inQueue is True and customer.finished is False:
                    customer.beingServed = True
        currentTime += 1  # advance time
    for customer in queueOfCustomers:  # reset objects
        totalTime += customer.timeWaited
        customer.timeWaited = 0
        customer.finishedTime = 0
        customer.inQueue = False
        customer.beingServed = False
        customer.finished = False
    return totalTime / numOfPeopleServed  # potential error, limit decimal places


def STF(queueOfCustomers: list, numberOfCustomers: int):
    totalTime = 0
    currentTime = 0
    numOfPeopleServed = 0
    # sort customers by priority and prepTime
    queueOfCustomers = sorted(queueOfCustomers, key=lambda x: (-x.priority, x.prepTime))
    while numOfPeopleServed != numberOfCustomers:
        numOfPeopleServed = 0
        for customer in queueOfCustomers:
            if customer.inQueue is True:  # add time to those in queue
                customer.wait()
            if customer.beingServed is True:  # subtract time from those being served
                customer.served()
            if customer.finished is True:  # add finished to people served
                numOfPeopleServed += 1
            if customer.timeArrived <= currentTime:  # set who is in queue
                if customer.finished is False:
                    customer.inQueue = True
        for customer in queueOfCustomers:
            if isSomeoneBeingServed(queueOfCustomers) is False:  # set served
                if customer.inQueue is True and customer.finished is False:
                    customer.beingServed = True
        currentTime += 1  # advance time
    for customer in queueOfCustomers:  # reset objects
        totalTime += customer.timeWaited
        customer.timeWaited = 0
        customer.finishedTime = 0
        customer.inQueue = False
        customer.beingServed = False
        customer.finished = False
    return totalTime / numOfPeopleServed  # potential error


# input
queueOfCustomers = []
numberOfCustomers = int(input())
for n in range(numberOfCustomers):
    x, y, z = [int(x) for x in input().split()]
    queueOfCustomers.append(Person(x, y, z))

# output
print("{:.2f}".format(FCFS(queueOfCustomers, numberOfCustomers)))
print("{:.2f}".format(STF(queueOfCustomers, numberOfCustomers)))
