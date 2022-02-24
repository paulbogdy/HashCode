class InputReader:

    def __init__(self, file):
        self.file = file
        
    
    def read(self):
        
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
                for _ in range(nr_skills):
                    curr_line = lines[idx].split()
                    #
                    skill_name = curr_line[0]
                    #
                    skill_level = int(curr_line[1])
                    
                    idx+=1
                
            for _ in range(self.nr_projects):
                curr_line = lines[idx].split()
                
                #
                project_name = curr_line[0]
                
                #
                nr_days = int(curr_line[1])
                
                #
                score = int(curr_line[2])

                #
                best_before = int(curr_line[3])

                nr_roles = int(curr_lines[4])

                idx+=1
                for _ in range(nr_roles):
                    curr_line = lines[idx].split()

                    #
                    skill_name = curr_line[0]
                    #
                    skill_level = int(curr_line[1])
                    
                    idx+=1

