from .Contributor import Contributor
from .Project import Project
from collections import defaultdict, OrderedDict

class InputReader:

    def __init__(self, file):
        self.file = file
        
        
    
    def read(self):
        
        contributors = []       

        with open(self.file, "r") as file:

            lines = file.readlines()
            first_line = lines[0].split()
            self.nr_contributors = int(first_line[0])
            self.nr_projects = int(first_line[1])
            idx = 1
            for _ in range(self.nr_contributors):
                curr_line = lines[idx].split()
                
                #
                name = curr_line[0]
                
                nr_skills = int(curr_line[1])
                
                idx+=1

                skill_dict = defaultdict(int)
                for _ in range(nr_skills):
                    curr_line = lines[idx].split()
    
                    skill_name = curr_line[0]
                    skill_level = int(curr_line[1])
                    
                    skill_dict[skill_name] = skill_level

                    idx+=1
                contributor = Contributor(name, skill_dict)            
                
                contributors.append(contributor)
            
            projects = []

            for _ in range(self.nr_projects):
                curr_line = lines[idx].split()
                

                project_name = curr_line[0]
                
                nr_days = int(curr_line[1])
                                
                score = int(curr_line[2])

                best_before = int(curr_line[3])

                nr_roles = int(curr_line[4])

                idx+=1

                skill_dict = OrderedDict()
                for _ in range(nr_roles):
                    curr_line = lines[idx].split()

                    
                    skill_name = curr_line[0]
                    
                    skill_level = int(curr_line[1])
                    
                    skill_dict[skill_name] = skill_level

                    idx+=1
                
                project = Project(project_name, nr_days, score, best_before, skill_dict)
                
                projects.append(project)
            return contributors, projects
