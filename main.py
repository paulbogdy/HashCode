from src.InputReader import InputReader
from src.AssignProject import *

def write_solution(project_cont, file_name):
    with open(file_name + ".out", "w") as f:
        f.write("{}\n".format(len(project_cont)))
        for (project, assignation) in project_cont:
            f.write(project + "\n")
            print(assignation.values())
            for cont in assignation.values():
                f.write(cont + " ")
            f.write("\n")


if __name__ == "__main__":
    #print(list(map(str, contributors)))
    #print(list(map(str, projects)))
    #print(assign_retry_strategy(contributors, projects))
    for letter in "b":
        reader = InputReader(letter + ".txt")
        contributors, projects = reader.read()
        for cont in contributors:
            print(cont.name)
        write_solution(assign_retry_strategy(contributors, projects), letter)
        print("Solved :" + letter)
