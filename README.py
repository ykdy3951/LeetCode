import os
import sys
from bs4 import BeautifulSoup
import pdb

# README creator

def create_readme():
    # Create README.md
    with open("README.md", "w") as f:
        f.write("# LeetCode\n")
        f.write("Collection of LeetCode questions to ace the coding interview!\n\n")
        f.write("## Table of Contents\n")
        f.write("| # | Title | Solution | Difficulty |\n")
        f.write("|---| ----- | -------- | ---------- |\n")

        # Get all files in the directory
        folders = os.listdir()
        # Sort the files
        folders.sort()
        # Remove unwanted files
        folders.remove(".git")
        folders.remove("README.md")
        folders.remove("run.py")
        folders.remove("practice")
        for folder in folders:
            # Get the folder name
            files = os.listdir(folder)
            files.remove("README.md")
            # Open the README.md file
            with open(f"{folder}/README.md", "r") as f2:
                lines = f2.readlines()
                # Get the title, solution and difficulty
                bs = BeautifulSoup(lines[0], "html.parser")
                title_info = list(bs.find("h2").text.split(". "))
                title_number = title_info[0]
                title = title_info[1]
                problem_url = bs.find("a")["href"]
                difficulty = bs.find("h3").text
                solutions = []
                for file in files:
                    if file.endswith(".py"):
                        solutions.append("[Python](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".java"):
                        solutions.append("[Java](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".cpp"):
                        solutions.append("[C++](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".go"):
                        solutions.append("[Go](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".js"):
                        solutions.append("[JavaScript](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".swift"):
                        solutions.append("[Swift](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".sql"):
                        solutions.append("[SQL](./" + os.path.join(folder, file) + ")")
                    elif file.endswith(".rs"):
                        solutions.append("[Rust](./" + os.path.join(folder, file) + ")")
                    else:
                        print(f"Unknown file type: {file}")
                
                # Write to README.md
                f.write(f"| {title_number} | [{title}]({problem_url}) | {', '.join(solutions)} | {difficulty} |\n")
                



if __name__ == "__main__":
    create_readme()