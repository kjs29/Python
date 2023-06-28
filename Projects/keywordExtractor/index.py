# import gradio as gr
# from functions import histogram, sort_by_value, delete_useless_words
# from applications import data_analyst_1, data_analyst_2, i_have_a_dream

# # Assuming data_analyst_1, data_analyst_1, iHaveADream are defined somewhere in your code

# def key_word_extractors(text, trim, *exclude):
#     excluded_words = [
#         '',     'Must',     'a',      'all',
#         'also', 'an',       'and',    'are',
#         'as',   'be',       'for',    'from',
#         'have', 'in',       'is',     'more',
#         'of',   'on',       'one',    'or',
#         'our',  'required', 'that',   'the',
#         'this', 'to',       'we',     'where',
#         'who',  'with',     'within', 'work',
#         'you',  'your'
#     ]
    
#     for each in exclude:
#         excluded_words.append(each) 

#     string = delete_useless_words(text, excluded_words)

#     hist = histogram(string)

#     answer = sort_by_value(hist, trim)

#     return answer


# demo = gr.Interface(
#     fn=key_word_extractors,
#     inputs=gr.Textbox(lines=10, placeholder='Place your job description'),
#     outputs="text")
    
# demo.launch()

# print(f"Data Analyst 1: {key_word_extractors(data_analyst_1, 6, 'role')}")
# print(f"Data Analyst 2: {key_word_extractors(data_analyst_2, 8)}")
# print(f"I have a dream speech: {key_word_extractors(i_have_a_dream, 10)}")

import gradio as gr

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2

demo = gr.Interface(
    calculator,
    [
        "number", 
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="Toy Calculator",
    description="Here's a sample toy calculator. Allows you to calculate things like $2+2=4$",
)
demo.launch()
