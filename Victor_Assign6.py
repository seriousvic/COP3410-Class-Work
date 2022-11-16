# COP3410 Assignment 6
# Victor Burgos
# Date 4/1/2022

###################################
# R-6.3
def transfer(S, T):
    for i in range(len(S)):
        T.append(S.pop())
    return T


S = ["1", "2", "3", "4"]
print("Our initial stack is", S)
T = []
T = transfer(S, T)
print("And our new stack is", T)
