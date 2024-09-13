from groq import Groq
import json

client = Groq(
    api_key="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"
)

def parserfn(message):
    result = ''
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are an AI bot designed to act as a professional for parsing resumes. You are given with resume and your job is to extract the following information from the resume:\\n    and return in the same json{'Name': 'PRADEEPA S', 'Email': 'pradeepas19102004@gmail.com', 'PhoneNumber': '+91 9994357443', 'Location': 'Thottiyavalsu, Namakkal.', 'GitHub': 'Username not mentioned', 'LinkedIn': 'https://www.linkedin.com/in/pradeepa-s-56a572259/', 'CareerObjective': 'Motivated and detail-oriented fresher aiming to start a career as a Full Stack Developer. Eager to utilize my academic background in Artificial Intelligence and Machine Learning, combined with strong problem-solving skills, to build innovative and efficient web applications. Passionate about learning new technologies and contributing to a collaborative team environment.', 'Education': [{'Institution': 'Kongu Engineering College', 'Year': '2022-2026', 'Degree': 'B.Tech in Artificial Intelligence and Machine Learning', 'Results': 'CGPA till 3rd semester: 8.89'}, {'Institution': 'Sri Vidya Mandir Matric Hr. Sec. School, Gurusamipalayam', 'Year': '2022', 'Degree': 'HSC', 'Results': 'Achieved 93%'}, {'Institution': 'Sri Vidya Mandir Matriculation School, Kurukapuram', 'Year': '2020', 'Degree': 'SSLC', 'Results': 'Achieved 97%'}], 'Projects': [{'ProjectName': 'Weather Prediction Using Classification, Regression, and Time Forecasting', 'Description': 'Utilized Python, scikit-learn, and time series forecasting for weather prediction.'}, {'ProjectName': 'Blood Group and Gender Prediction Using Fingerprint', 'Description': 'Applied deep learning algorithms (ResNet, VGGNet, CNN) to predict blood group and gender from fingerprints using TensorFlow and Keras.'}, {'ProjectName': 'Video Captioning Full Stack Project', 'Description': 'Developed a video captioning application using React, Next.js, and AWS for backend machine learning models and storage.'}], 'ProgrammingLanguages': ['Java Programming', 'SQL Programming'], 'WebTechnologies': ['Web Development'], 'ToolsandFrameworks': [], 'Databases': [], 'OtherSkills': ['Machine Learning', 'Python', 'Java Programming', 'Web Development', 'SQL Programming', 'C'], 'Interests': {'Hobbies': []}, 'Achievements':  {'Achievement1':'Secured second place in aptitude in the intra-college technical symposiuobile Department at Kongu Engineering College.','Achievement2':''}, 'Experience': [{'Position': 'Web Development Intern', 'Company': 'InTernPe Company', 'Location': 'Unknown', 'Dates': 'May 2024 - June 2024', 'Description': 'Unknown'}], 'CareerLevel': '','Certifications':''} classify it in 4 which are Fresher who have no experience,Beginner who have 1 to 3 years of experience,Mid level who have 3 to 10 years of experience,and Senior level who have more than 10 years of Experience,claculate experience from all work experience and give only the level without years dont cut of the carrer.If skills are given Classify the skills according to the given fields.If achievements or leaderships are given fetch them correctly and into Achievements.If any cources or certficatios are mentioned add it into certifications.If the information is not present ignore it and under any circumstances do not use any fake information or dummy information and only give the json formatted data as it will be used for  json decoding purposes in order to avoid syntax errors\nDont give any insights or \"here is the extracted information in JSON format\" or something like this\n"},
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        result += chunk.choices[0].delta.content or ""

    # Debugging the result before returning it
    print("Generated result:", result)

    # Attempting to parse the result to ensure it's valid JSON
    try:
        # Replace single quotes with double quotes for JSON compatibility
        result = result.replace("'", '"')

        # Fix common issues like missing commas or incorrect formatting
        result = result.replace('}"{', '}, {')  # Handling cases where objects are concatenated improperly

        # Load the JSON data
        json_data = json.loads(result)

        # Return a properly formatted JSON string
        return json.dumps(json_data, indent=4)  # Indent for readability

    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        # Print the problematic part of the result for debugging
        error_position = e.pos if e.pos is not None else 0
        print("Problematic JSON segment:", result[max(0, error_position-100):error_position+100])
        # Return the raw result if JSON decoding fails
        return result

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # Return the raw result if any other unexpected error occurs
        return result
