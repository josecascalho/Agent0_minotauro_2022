import client
import ast
import random


def reactive_example_1(agent):
    end = False
    while end == False:
        msg = agent.execute("info", "view")
        objects = ast.literal_eval(msg)
        if objects[0] == 'goal':
            agent.execute("command","forward")
            end = True
            print("Found Goal!")
        elif objects[0] == 'obstacle':
            res = random.randint(0,4)
            if res <= 2:
                agent.execute("command", "left")
            else:
                agent.execute("command","right")
        else:
            agent.execute("command","forward")
    input("Press key to exit!")

def reactive_example_2(agent):
    end = False
    msg = agent.execute("command", "set_steps")
    while end == False:
        msg = agent.execute("info","view")
        print("Message:",msg)
        objects = ast.literal_eval(msg)
        if 'obstacle' in objects or 'bomb' in objects:
            agent.execute("command","left")
        else:
            if 'goal' in objects:
                end = True
                print("Found Goal!\n")
            else:
              res = random.randint(0,4)
              if res <= 3:
                  agent.execute("command", "forward")
              else:
                  agent.execute("command","right")
        input("Press key to exit!")

def main():
    agent = client.Client('127.0.0.1', 50001)
    agent.connect()
    random.seed()  # To become true random, a different seed is used! (clock time)

    reactive_example_1(agent)


main()
