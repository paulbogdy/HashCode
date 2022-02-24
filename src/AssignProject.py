from src.CheckProject import checkPossibleProject


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
                contr = project.skills
                for (skill, cont) in assigned_contributors:
                    contr[skill] = cont.name
                    cont.improve_skill(skill)
                project_cont.append((project.name, contr))
                change = True
            else:
                not_assigned.append(project)
        projects = not_assigned
    return project_cont

