# A 3rd party demo contributed by Github user AK391. This is not implemented by Microsoft and Microsoft do not own any IP with this implementation and associated demo. 
# Microsoft has not tested the generation of this demo and is not responsible for any offensive or biased generation from this demo. 
# Please contact the creator for any potential issue. 


from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import gradio as gr

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
grammar_tokenizer = AutoTokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")
grammar_model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/grammar_error_correcter_v1")

text_session = []
chat_history_ids = None

def dialogpt(text):
     # encode the new user input, add the eos_token and return a tensor in Pytorch
    global chat_history_ids
    text_session.append(text)
    # text_input = tokenizer.eos_token.join(text_session)
    # text_session += text+tokenizer.eos_token
    new_user_input_ids = tokenizer.encode(text+tokenizer.eos_token, return_tensors='pt')
    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if chat_history_ids is not None else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(bot_input_ids, max_length=5000, pad_token_id=tokenizer.eos_token_id)
    print("The text is ", [text])
    # tokenized_phrases = grammar_tokenizer([text], return_tensors='pt', padding=True)
    # corrections = grammar_model.generate(**tokenized_phrases)
    # corrections = grammar_tokenizer.batch_decode(corrections, skip_special_tokens=True)
    # print("The corrections are: ", corrections)

    # pretty print last ouput tokens from bot
    output =  tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    print("The outout is :", output)
    text_session.append(output)
    return '\n'.join(text_session)+'\n\n'+feedback(text)


def feedback(text):
    tokenized_phrases = grammar_tokenizer([text], return_tensors='pt', padding=True)
    corrections = grammar_model.generate(**tokenized_phrases)
    corrections = grammar_tokenizer.batch_decode(corrections, skip_special_tokens=True)
    print("The corrections are: ", corrections)
    if corrections[0] == text:
        feedback = f'Looks good! Keep up the good work'
    else:
        feedback = f'\'{corrections[0]}\' might be a little better'
    return f'FEEDBACK:  {feedback}'


inputs = gr.inputs.Textbox(lines=1, label="Input Text")
outputs =  [gr.outputs.Textbox(label="Conversation")]

title = "A Conversational Agent for Language Learning"
description = "A quick roof of concepy using Gradio and a possible starting point for the hackathon"
article = "<p style='text-align: center'><a href='https://docs.google.com/presentation/d/11fiO91MKZVgNoQJh5pn3Tw8-inHe6XbWYB2r1f701WI/edit?usp=sharing'> A conversational agent for Language learning</a> | <a href='https://github.com/ConorNugent/gradio-chatbot-demo'>Github Repo</a></p>"
examples = [
            ["Hi, how are you?"],
            ["How far away is the moon?"],
]


gr.Interface([dialogpt], inputs, outputs, title=title, description=description, article=article, examples=examples).launch(debug=True)