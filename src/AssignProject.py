from src.CheckProject import checkPossibleProject
import copy

def assign_retry_strategy(contributors, projects):
    not_assigned = []
    change = True
    project_cont = []
    while change and len(projects) > 0:
        not_assigned = []
        change = False
        for project in projects:
            # change function name
            assigned_contributors = checkPossibleProject(project, contributors)
            if len(assigned_contributors) == len(project.skills):
                contr = [None]*len(assigned_contributors)
                for (skill, cont, i, level) in assigned_contributors:
                    contr[i] = cont.name
                    if cont.skills[skill] <= level:
                        cont.improve_skill(skill)
                project_cont.append((project.name, contr))
                change = True
            else:
                not_assigned.append(project)
        projects = copy.deepcopy(not_assigned)
    return project_cont

