class Project:

    def __init__(self, name, nr_days, score, best_before, skills):

        self.name = name
        self.nr_days = nr_days
        self.score = score
        self.best_before = best_before
        self.skills = skills
    
    def __str__(self):

        return self.name + " " + str(self.nr_days) + "\n" + str(self.skills) + "\n"
