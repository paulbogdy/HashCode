
def checkPossibleProject(project, conts):

    conts_assigend = []

    for cont in conts:
        # We check for a contributor all the 
        # skills and if it can be added to project
        for projSkill in project.skills:
            if cont.skills[projSkill] >= project.skills[projSkill]:
                cont.skills[projSkill] += 1
                conts_assigend.append(cont)

    return conts_assigend
            

if __name__ == "__main__":
    pass
    