from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Data from SWETHA's Resume ---
RESUME_DATA = {
    "name": "SWETHA. M",
    "email": "swetha004.m@gmail.com",
    "phone": "+91 82206 93721",
    "linkedin": "swetha", # Using the provided LinkedIn alias
    "objective": "MCA graduate with expertise in programming, database management, AI, and full-stack development, aspiring to build a career in academia as a professor, focusing on student mentorship and impactful research.",
    
    "education": [
        {"degree": "Master of Computer Applications (MCA)", "institution": "University College of Engineering, BIT Campus - Trichy", "period": "2024-2026", "score": "CGPA: 8.56"},
        {"degree": "Bachelor of Computer Applications (BCA)", "institution": "Dr. Kalaingar Government Arts College - Kulithalai", "period": "2021-2024", "score": "CGPA: 8.00"},
        {"degree": "Higher Secondary Certificate", "institution": "Government Girls Higher Secondary School - Kulithalai", "period": "2020-2021", "score": "Percentage: 86"},
    ],
    
    "projects": [
        {"title": "Agentic AI Model - College Admission Agent", "description": "AI model developed for handling complex college admission queries.", "year": "2025"},
        {"title": "Generative AI Recipe Application", "description": "Gemini + Streamlit app creating dynamic and customizable recipes.", "year": "2025"},
        {"title": "Unemployment Analysis in India Dashboard", "description": "A Power BI dashboard analyzing regional unemployment trends and indicators.", "year": "2024"},
        {"title": "Conference Website Development", "description": "Developed official website for a university chemistry department's AICTE conference.", "year": "2025"},
        {"title": "Android Movies Update App", "description": "Android application for movie updates using XML and Java.", "year": "2025"},
    ],
    
    "skills": {
        "languages": ["Python", "JavaScript", "HTML", "CSS", "PHP", "SQL"],
        "databases": ["MySQL", "Microsoft SQL Server", "MongoDB"],
        "frameworks_tools": ["VS Code", "Git/GitHub", "Power BI", "Microsoft 365", "Canva", "MySQL Workbench"],
        "ai_ml": ["GenAI (Google Cloud)", "Generative AI", "Responsible AI"]
    },
    
    "internships": [
        {"role": "Front-End Development", "company": "IBM & Edunet Foundation", "period": "Aug - Sep 2025"},
        {"role": "Web Development (PHP & SQL)", "company": "Apex Technologies", "period": "Aug - Sep 2025"},
        {"role": "AI & Cloud Internship", "company": "IBM & Edunet Foundation", "period": "Jul - Aug 2025"},
    ],

    "certifications": [
        "GenAI Certification - Google Cloud",
        "Full Stack Web Development Course [Ongoing] - Udemy",
        "Microsoft 365 Training and Power BI",
        "Generative AI, Democratization of AI, Responsible AI - ATAL FDP Program"
    ]
}


@app.route('/')
def index():
    """Renders the main portfolio page with resume data."""
    # Pass the RESUME_DATA dictionary to the index.html template
    return render_template('index.html', data=RESUME_DATA)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handles the contact form submission."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # --- Placeholder for Data Handling/Emailing ---
        print("\n--- New Contact Submission Received ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}\n")
        
        # Redirect to the success page
        return redirect(url_for('success'))

    # If GET request, display the contact form
    return render_template('contact.html')

@app.route('/success')
def success():
    """Renders the success confirmation page."""
    return render_template('success.html')

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)