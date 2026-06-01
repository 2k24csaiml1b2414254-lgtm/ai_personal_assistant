
# In[1]:
OPENAI_API_KEY="paste-your-api-key-here"

# In[2]:
# !pip install openai

# In[3]:
# Prompt => openai model => response
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

response = client.responses.create(
    model="gpt-5.4",
    input="Write a short bedtime story."
)

print(response.output_text)


# In[4]:
response = client.responses.create(
    model="gpt-5.4",
    input=[
        {"role": "user", "content": "a+5=7, find a"},
        {"role": "system", "content": "act like a math teacher"}
    ]
)

print(response.output_text)

# In[5]:
response = client.responses.create(
    model="gpt-5.4",
    input="a+5=7, find a"
)

print(response.output_text)

# In[6]:
response

# In[7]:
# Image
response = client.responses.create(
    model="gpt-5.4",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type" : "input_text",
                    "text": "Tell me the capital of the country to which the flag belongs to in the reference image"
                },
                {
                    "type": "input_image",
                    "image_url": "https://images.pexels.com/photos/3476860/pexels-photo-3476860.jpeg?cs=srgb&dl=pexels-studio-art-smile-218587-3476860.jpg&fm=jpg"
                }
            ]
        }
    ]
)

print(response.output_text)

# ### AI Personal Assistant

# In[8]:
# queries answer
# emails => summarize

class PersonalAssistant:
    def __init__(self):
        print("Hi, I am your AI assistant. How can I help?")

    def ans_query(self):
        question = input("Ask me anything: ")
        
        response = client.responses.create(
            model="gpt-5.4",
            input=[
                {"role": "system", "content": "Act like a helpful personal assistant"},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_output_tokens=512
        )
        
        print(response.output_text.strip())

    def summarize_email(self):
        email_text = input("Paste your email here: ")
        prompt = f"summarize the following email in 2-3 sentences: {email_text}"
        
        response = client.responses.create(
            model="gpt-5.4",
            input=[
                {"role": "system", "content": "Act like an expert email assistant"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_output_tokens=512
        )
        
        print("\n\nSummary: ", response.output_text.strip())

# In[9]:
assistant = PersonalAssistant()

# In[10]:
assistant.ans_query()

# In[11]:
assistant.summarize_email()

# In[12]:
# Sample Email
""" Dear Sir/Madam,

I hope you are doing well.

My name is Himesh, and I am currently pursuing a B.Tech in Artificial Intelligence and Machine Learning. I am writing to express my interest in internship opportunities within your organization.

I have been actively working on AI/ML projects and continuously improving my skills in Python, Machine Learning, Deep Learning, Data Structures & Algorithms, and Web Development. I am eager to apply my knowledge in a practical environment and gain industry experience.

I would be grateful if you could consider my application for any suitable internship positions. I have attached my resume for your review.

Thank you for your time and consideration. I look forward to hearing from you.

Sincerely,

Himesh
B.Tech (AI & ML)
Email:(mailto:your_email@example.com)
Phone: +91 XXXXX XXXXX
 """

# ## Images in OpenAI

# ### Responses API

# In[13]:
import base64 
# images => base64 encoded strings => decode

# In[14]:
response = client.responses.create(
    model="gpt-5",
    input="Generate an image of a highly detailed futuristic spaceship, flying near a nebula",
    tools=[{"type": "image_generation"}]    
)

image_data = [
    output.result
    for output in response.output
    if output.type == "image_generation_call"
]

# decode & store image in a file
if image_data:
    image_base64 = image_data[0]
    with open("spaceship.png", "wb") as f:
        image_bytes = base64.b64decode(image_base64)
        f.write(image_bytes)

# ### Image API

# In[15]:
prompt = "Generate an image of a highly detailed, futuristic spaceship flying near a nebula"

result = client.images.generate(
    model="gpt-image-1.5",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("spaceship-image.png", "wb") as f:
    f.write(image_bytes)

# In[16]:
# EDIT

prompt = "Take the reference image and convert the spaceship color to red"

result = client.images.edit(
    model="gpt-image-1.5",
    prompt=prompt,
    image=[
        open("spaceship-image.png", "rb"),
    ]
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("spaceship-red.png", "wb") as f:
    f.write(image_bytes)

# In[17]:

