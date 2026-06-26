# analyzer.py

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "excel",
    "power bi",
    "tableau",
    "java",
    "c++",
    "git",
    "docker"
]


def analyze_resume(resume_text, job_text):
    resume_text = resume_text.lower()
    job_text = job_text.lower()

    required_skills = [
        skill for skill in SKILLS
        if skill in job_text
    ]

    found_skills = [
        skill for skill in required_skills
        if skill in resume_text
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_text
    ]

    return found_skills, missing_skills


def calculate_score(found_skills, job_text):
    job_text = job_text.lower()

    required_skills = [
        skill for skill in SKILLS
        if skill in job_text
    ]

    if len(required_skills) == 0:
        return 0

    score = (len(found_skills) / len(required_skills)) * 100

    return round(score, 2)