import os

def generate_latex_cv(name, title, contact_info, education, experience, skills):
    content = f"""
\\documentclass[a4paper,10pt]{{article}}
\\usepackage[left=1in, right=1in, top=1in, bottom=1in]{{geometry}}
\\usepackage{{enumitem}}

\\pagestyle{{empty}}
\\setlength{{\\parindent}}{{0pt}}

\\begin{{document}}

\\begin{{center}}
\\textbf{{\\LARGE {name}}} \\\\
{title} \\\\
{contact_info}
\\end{{center}}

\\section*{{Education}}
{format_list(education)}

\\section*{{Experience}}
{format_list(experience)}

\\section*{{Skills}}
{format_list(skills)}

\\end{{document}}
"""

    return content

def format_list(items):
    return "\n".join([f"\\item {item}" for item in items])

def save_to_latex(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Sample CV data
    name = "Zeeshan Ali"
    title = "Software Engineer"
    contact_info = "Email: john.doe@example.com\nPhone: (123) 456-7890"
    education = ["B.S. in Computer Science, University XYZ, 20XX-20XX"]
    experience = [
        "Software Engineer, ABC Corp, 20XX-present",
        "Intern, XYZ Inc, 20XX-20XX"
    ]
    skills = ["Python", "Java", "Web Development", "Database Management"]

    # Generate LaTeX content
    latex_content = generate_latex_cv(name, title, contact_info, education, experience, skills)

    # Save to a .tex file
    save_to_latex(latex_content, "cv.tex")

    print("CV generated successfully. You can use a LaTeX compiler to generate a PDF.")
