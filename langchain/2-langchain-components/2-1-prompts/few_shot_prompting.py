from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"input": "I was charged twice for my subscription this month.", "output": "Billing Issue"},
    {"input": "The app crashes every time I try to log in.", "output": "Technical Problem"},
    {"input": "Can you explain how to upgrade my plan?", "output": "General Inquiry"},
    {"input": "I need a refund for a payment I didn't authorize.", "output": "Billing Issue"},
]

example_template = """
Ticket: {input}
Category: {output}
"""

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template=example_template,
    ),
    prefix=(
        "Classify the following customer support tickets into one of "
        "the categories: 'Billing Issue', 'Technical Problem', or "
        "'General Inquiry'.\n\n"
    ),
    suffix="\nTicket: {user_input}\nCategory:",
    input_variables=["user_input"],
)

print(few_shot_prompt.format(
    user_input="I am unable to connect to the internet using your service."
))



# Output
# Terminal — Output
# Classify the following customer support tickets into one of the categories: 'Billing Issue', 'Technical Problem', or 'General Inquiry'.

#     Ticket: I was charged twice for my subscription this month.
#         Category: Billing Issue

# Ticket: The app crashes every time I try to log in.
#     Category: Technical Problem

# Ticket: Can you explain how to upgrade my plan ?
#     Category : General Inquiry

# Ticket: I need a refund for a payment I didn't authorize.
# Category: Billing Issue

# Ticket: I am unable to connect to the internet using your service.
#     Category: