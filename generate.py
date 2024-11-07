from dotenv import load_dotenv
from groq import Groq

# Loads dotenv file
load_dotenv('.env.local')

# Setting up client
client = Groq()

# Generate Function
def generate(syllabus: str, exam: str, time: str, context: str):
    system_prompt = "You are a trainer who has trained several toppers. You are very helpful and very useful when it comes to giving advice. You are often given a specific time and some syllabus and some other important information which can be case sensitive. You must return with an action plan to finish the task at hand and help your students ace the exam using your previous knowledge of the weightage of chapter for whatsoever exam you are asked for. The action plan you return with must be capable of returning maximum marks for the given time allotted."

    user_content = f"Create an action plan for the {exam} exam. The syllabus includes: {syllabus}. You have {time} to prepare. Additional context: {context}."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_content,
            }
        ],
        model="llama3-8b-8192",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )

    print(chat_completion.choices[0].message.content)