def checkPossibleProject(project, conts):

    conts_assigend = []

    for cont in conts:
        # We check for a contributor all the 
        # skills and if it can be added to project
        for projSkill in project.skills:
            if cont.skills[projSkill] >= project.skills[projSkill]:
                conts_assigend.append((projSkill, cont))
                break

    return conts_assigend
            

