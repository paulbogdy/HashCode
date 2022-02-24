from src.InputReader import InputReader

if __name__ == "__main__":
    reader = InputReader("a.txt")
    contributors, projects = reader.read()
    print(list(map(str, contributors)))
    print(list(map(str, projects)))
