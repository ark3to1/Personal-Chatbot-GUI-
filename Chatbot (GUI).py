import tkinter as tk
from tkinter import scrolledtext

class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Personal Chatbot")
        master.geometry("400x500")

        # Create and pack the chat display area
        self.chat_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=25)
        self.chat_display.pack(padx=10, pady=10)
        self.chat_display.config(state=tk.DISABLED)

        # Create and pack the input field
        self.input_field = tk.Entry(master, width=40)
        self.input_field.pack(side=tk.LEFT, padx=10)

        # Create and pack the send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

    def send_message(self):
        user_message = self.input_field.get()
        if user_message:
            self.display_message("You: " + user_message)
            self.input_field.delete(0, tk.END)

            #-------------------------------------------------------------------------------------------------------
            if (user_message.lower() == "what is your name?"):
                self.display_message("Bot: My name is Rehman khan.")
            elif (user_message.lower() == "hi"):
                self.display_message("Bot: Hello!")
            elif (user_message.lower() == "how are you?"):
                self.display_message("Bot: I'm good!")
            elif (user_message.lower() == "what is your age?"):
                self.display_message("Bot: My name is 25 years old.")
            elif (user_message.lower() == "from where are you?"):
                self.display_message("Bot: I am from karachi pakistan.")
            elif (user_message.lower() == "tell me something about your education."):
                self.display_message("Bot: Recenlty i have done my graduation from university of karachi.")
            elif (user_message.lower() == "what are your future plans?"):
                self.display_message("Bot: I want to build my own software house which will be the best software house in the world.")
            elif (user_message.lower() == "how many siblings do you have?"):
                self.display_message("Bot: I have 3 brothers and 3 sisters.")
            elif (user_message.lower() == "what is your religion?"):
                self.display_message("Bot: Alhamdulillah i am muslim and i feel proud to be a muslim.")
            elif (user_message.lower() == "what is your favourite color?"):
                self.display_message("Bot: my fav color is purple.")
            elif (user_message.lower() == "what is your favourite sport?"):
                self.display_message("Bot: i love to watch and play soccer and sometimes cricket too")
            elif (user_message.lower() == "Do you like watching movies?"):
                self.display_message("Bot: Yes i like watching movies that have some message in it.")
            elif (user_message.lower() == "Bye"):
                self.display_message("Bot: Nice to meet you.")
            else:
                self.display_message("Bot: I can't understand your question or you are missing something.")
            #-------------------------------------------------------------------------------------------------------
            
            # Here you would typically process the user's message and get a response
            # For now, we'll just echo the message
            # bot_response = "Bot: I received your message: " + user_message
            # self.display_message(bot_response)

    def display_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

root = tk.Tk()
gui = ChatbotGUI(root)
root.mainloop()