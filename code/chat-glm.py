from transformers import AutoTokenizer, AutoModel

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()
model = model.eval()

# Function to read questions from a file
def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        questions = file.readlines()
    return questions

# Function to write responses to a file
def save_responses(file_path, responses):
    with open(file_path, 'w', encoding='utf-8') as file:
        for response in responses:
            file.write(response + '\n')

# Load questions from 'questions.txt'
questions = load_questions('dataset/ae_templates.txt')

# Generate responses for each question
responses = []
i = 0
for question in questions:
    question = question.strip()  # Remove any leading/trailing whitespace
    response, history = model.chat(tokenizer, question + "What should [MASK] be? Just answer one word.", history=[])
    responses.append(response)
    print(i)
    i = i + 1

# Save responses to 'answers.txt'
save_responses('res/ae.txt', responses)

print("All questions processed and answers saved.")

