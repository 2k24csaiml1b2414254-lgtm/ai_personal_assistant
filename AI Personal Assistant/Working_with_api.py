
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
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)


# In[4]:
response = client.responses.create(
    model="gpt-5.4",
    input=[
        {"role": "user", "content": "a+2=7, find a"},
        {"role": "system", "content": "act like a math teacher"}
    ]
)

print(response.output_text)

# In[5]:
response = client.responses.create(
    model="gpt-5.4",
    input="a+2=7, find a"
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
""" Dear Shradha Ma'am,

I hope this email finds you well.  I am reaching out to request a meeting at a time convenient for you to discuss the performance of our tech team over the past quarter.

Over the past few months, the team has been working on several critical projects, and I would like to review both our achievements and areas where we can improve. This discussion will help us identify opportunities for increased efficiency, address any challenges the team may be facing, and ensure we are aligned with organizational objectives.

Please let me know your availability in the coming week, and I will be happy to coordinate a time that works best for you. I anticipate that the meeting will take approximately 30–45 minutes, and I will prepare a brief overview of the team’s performance metrics for our discussion.

Thank you for your time and consideration. I look forward to our conversation and to collaboratively identifying ways to strengthen our tech team’s performance.

Warm regards,
Rahul Kumar
Project Manager """

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

