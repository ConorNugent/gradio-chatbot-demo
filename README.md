# A conversational agent for language learning

Some optional initial scaffolding for the chabot hackaton challenge. The intial components are based on [DialoGPT](https://huggingface.co/transformers/model_doc/dialogpt.html) and [Gramformer]( https://github.com/PrithivirajDamodaran/Gramformer)


<img width="1365" alt="Screenshot 2021-09-06 at 15 19 37" src="https://user-images.githubusercontent.com/228645/132231439-b31f08bc-5575-474d-9b5a-59afaaa68846.png">

# Installation & running

To install the requirements `pip install -r requirements.txt`

To run the gradio and kick start the client run `python gradio_demo.py` and then hit http://127.0.0.1:7860/

Gradio can be a little slow to start and especially so the first time when the models are downloaded. You should see 'Running locally at: http://127.0.0.1:7860/' in the prompt once everything is ready

# Known crappiness
This is just a quick proof of concept that is intended as a starting point. Having said that here are some known areas of ugliness 

- The text box doesn't clear out on submit  (you will need to clear the text to input the next line in the conversation)

- The conversation state is stored globally 

- The conversation craps out after a max number of tokens is reached. This should be an easy fix

# Interacting with the client

Just input some text and click submit

<img width="1369" alt="Screenshot 2021-09-06 at 15 50 34" src="https://user-images.githubusercontent.com/228645/132234844-3f879236-0a53-4780-87b7-603e2dd0172c.png">

The client will update the conversation with a reply from the bot and some feedback. To keep the conversation going just clear out the text, add a new response and click submit 

<img width="1377" alt="Screenshot 2021-09-06 at 15 51 05" src="https://user-images.githubusercontent.com/228645/132234857-960c2573-a0a0-4107-9d3d-a13d841d3277.png">



