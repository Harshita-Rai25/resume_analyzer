from pdf_reader import extract_text
from analyzer import analyze_resume, calculate_score

resume_path = input("Enter resume path: ")
job_text = input("Enter job description: ")

resume_text = extract_text(resume_path)

found_skills, missing_skills = analyze_resume(resume_text, job_text)
score = calculate_score(found_skills, job_text)

print("\n--- RESULTS ---")

print("\nFound Skills:")
for s in found_skills:
    print("-", s)

print("\nMissing Skills:")
for s in missing_skills:
    print("-", s)

print(f"\nATS Score: {score}%")