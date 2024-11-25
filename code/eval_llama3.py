from transformers import pipeline
import torch

model_id = "meta-llama/Llama-3.2-1B-Instruct"

pipe = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",
)

with open('data/ze_templates.txt', 'r') as file:
    dataset = file.readlines()

messages = [
    {"role": "system", "content": "What should [MASK] be? Just answer in one word, do not directly use perple's name."},
]

results = []

for line in dataset:
    messages.append({"role": "user", "content": line.strip()})

    terminators = [
        pipe.tokenizer.eos_token_id,
        pipe.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    outputs = pipe(
        messages,
        max_new_tokens=256,
        eos_token_id=terminators,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
    )

    assistant_response = outputs[0]["generated_text"][-1]["content"]
    results.append(assistant_response)


    messages.pop()

with open('res/llama-3.2-1b/ze_results.txt', 'w') as file:
    for result in results:
        file.write(result + '\n')

print("The results have been saved!")
