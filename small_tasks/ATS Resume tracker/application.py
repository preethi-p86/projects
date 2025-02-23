from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
import fitz
import re

# from pdfminer.high_level import extract_text

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

# Function to extract text using PyMuPDF (Fitz)
def extract_text_from_pdf(uploaded_file):
    try:
        uploaded_file.seek(0)  # Reset file pointer before reading
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "\n".join([page.get_text("text") for page in doc])
        return text if text.strip() else "No text found in PDF."
    except Exception as e:
        return f"Error extracting text: {str(e)}"

# Function to extract text using PDFMiner
# def extract_text_from_miner(uploaded_file):
#     try:
#         temp_path = "temp_resume.pdf"
#         with open(temp_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())  # Save uploaded file temporarily

#         text = extract_text(temp_path)
#         os.remove(temp_path)  # Clean up temporary file
#         return text if text.strip() else "No text found in PDF."
#     except Exception as e:
#         return f"Error extracting text with PDFMiner: {str(e)}"

# Function to generate AI response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

# Process PDF as an image for AI
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        uploaded_file.seek(0)  # Reset file pointer
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


def extract_resume_details(text):

    details = {"Name": "Name Not found", "Email ID": "Email ID Not found", "Phone Number": "Phone Number Not found", 
               "LinkedIn": "LinkedIn Not found"}
    
    lines = text.split("\n")  # Split text by new lines
    details["Name"] = lines[0].strip()
    print(details['Name'])


    # pattern = r"\+91\s?-?\d{2,5}\s?\d{2,5}\s?\d{4,}"
    pattern = r"(?:\+?91[-\s]?)?\d{3}[-\s]?\d{3}[-\s]?\d{4}"
    phone_number = re.findall(pattern, text)
    print(phone_number)
    if phone_number:
        phone_number = phone_number[0].replace(' ','').replace('-','')
        details['Phone Number'] = phone_number
    print(phone_number)


    email_pattern = r'[\w\.-]+@[\w\.-]+'
    mail = re.findall(email_pattern, text)[0]
    if mail:
        details['Email ID'] = mail
    print(mail)
    

    linkedin_pattern = r'\S*linkedin\S*'
    linkedin_mentions = re.findall(linkedin_pattern, text)[0]
    if linkedin_mentions:
        print(linkedin_mentions)
        if 'www.' not in linkedin_mentions:
            linkedin_mentions = 'www.' + linkedin_mentions
        if 'http://' in linkedin_mentions:
            linkedin_mentions = 'https://' + linkedin_mentions[8:]
        if 'https://' not in linkedin_mentions:
            linkedin_mentions = 'https://' + linkedin_mentions
    details['LinkedIn'] = linkedin_mentions
    print(linkedin_mentions)


    return details

# Job roles and descriptions
job_and_desc = {
"Data Analyst": 
        """
        Collect, clean, and analyze large datasets to extract insights. Develop reports, dashboards, and visualizations using tools like Power BI, Tableau, or Excel. Perform statistical analysis and predictive modeling using Python or R.
        Work with SQL databases to query and manipulate data. Identify trends and patterns to support business decision-making. Collaborate with stakeholders to understand data requirements.
        """,
"HR Manager": 
        """
        Oversee recruitment, hiring, and onboarding processes. Develop and implement HR policies and procedures. Manage employee relations, conflict resolution, and workplace culture.
        Conduct performance evaluations and training programs. Ensure compliance with labor laws and company regulations. Maintain employee records and handle payroll administration.
        """,
"Web Developer": 
        """
        Design, develop, and maintain websites using HTML, CSS, JavaScript, and frameworks like React or Angular. Optimize web applications for performance, speed, and scalability. Ensure website responsiveness across different devices and browsers.
        Develop backend functionality using Node.js, Django, or other frameworks. Work with databases like MySQL, PostgreSQL, or MongoDB. Troubleshoot and debug web applications.
        """,
"App Developer": 
        """
        Design and develop mobile applications for iOS and Android platforms. Work with programming languages such as Swift, Kotlin, Flutter, or React Native. Optimize app performance and responsiveness.
        Integrate third-party APIs and services. Conduct testing and debugging to ensure app stability. Collaborate with UI/UX designers to improve user experience.
        """
}


jobs = list(job_and_desc.keys())

# Streamlit UI
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

selected_role = st.selectbox("Select the Position Applied For:", jobs)
st.write(f"You selected: {selected_role}")

uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

    text = extract_text_from_pdf(uploaded_file)

    # if not text.strip():
    #     st.error("No text found in the PDF.")
    # else:
    #     st.write("Text extracted successfully!")  

    # all_text = extract_text_from_miner(uploaded_file)

    print(text)
    print('\n*****************\n')
    # print(all_text)

    details = extract_resume_details(text)
    print(details)

    st.markdown("---")  # Adds a horizontal line

    # Display extracted details line by line
    st.write(f"👤 **Name:** {details['Name']}")
    st.write(f"📧 **Email ID:** {details['Email ID']}")
    st.write(f"📞 **Phone Number:** {details['Phone Number']}")
    st.write(f"🔗 **LinkedIn:** {details['LinkedIn']}")

    # Display extracted information with bigger text
    # st.markdown(f"<h4>👤 Name: {details['Name']}</h2>", unsafe_allow_html=True)
    # st.markdown(f"<h4>✉  Email: {details['Email ID']}</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h4>📞 Phone: {details['Phone Number']}</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h4>🔗 LinkedIn: {details['LinkedIn']}</h3>", unsafe_allow_html=True)


submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("Percentage match")



input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_text = job_and_desc.get(selected_role, "No description found.")

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
