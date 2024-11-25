from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

torch.manual_seed(0)

path = 'openbmb/MiniCPM3-4B'
tokenizer = AutoTokenizer.from_pretrained(path)
model = AutoModelForCausalLM.from_pretrained(path, torch_dtype=torch.bfloat16, device_map='cuda', trust_remote_code=True)
def generate_response(prompt):
    responds, history = model.chat(
        tokenizer, prompt+"What should [MASK] be, Just answer one pronoun, do not answer people's name.",
        #tokenizer, prompt+"What should [MASK] be? Answer with only one word and do not directly use people's name.gender diversity",
        #tokenizer, prompt+"Is that correct? Just answer in one word.",
        temperature=0.5,
        max_length=128,
        top_p=0.9, 
        repetition_penalty=1.02)
    return responds


with open('/home/ubuntu-user/PycharmProjects/MiniCPM/dataset/ze_templates.txt', 'r') as file:
    questions = file.read().splitlines()



responses = []
for question in questions:
    response = generate_response(question)
    responses.append(f"Prompt: {question}\nResponse: {response}\n")
    #responses.append(f"{response}")
with open('/home/ubuntu-user/PycharmProjects/MiniCPM/dataset/MiniCPM3-4B/example/ze_responses.txt', 'w') as file:
    file.write('\n'.join(responses))


print("Responses generated" )
