import copy
from collections import defaultdict

def checkPossibleProject(project, conts):

    conts_assigend = []
    solved = []
    skills = defaultdict(int)
    for cont in conts:
        # We check for a contributor all the 
        # skills and if it can be added to project
        for i, (projSkill, skill_level) in enumerate(project.skills):
            if (projSkill, skill_level) not in solved and (cont.skills[projSkill] >= skill_level or (cont.skills[projSkill] + 1 >= skill_level and skills[projSkill] >= skill_level)):
                conts_assigend.append((projSkill, cont, i, skill_level))
                solved.append((projSkill, skill_level))
                for skill, level in cont.skills.items():
                    skills[skill] = max(skills[skill], level) 
                break

    return conts_assigend
            

