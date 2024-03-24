import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk

class MoodMosaicChatbot:
    def __init__(self, master):
        self.master = master
        master.title("MoodMosaic Chatbot")
        master.iconphoto(True, tk.PhotoImage(file="D:\\3-2\\Minor Project\\MoodMosaic.png"))

        # Load logos
        self.bot_logo = Image.open("D:\\3-2\\Minor Project\\Bot_logo.png")
        self.user_logo = Image.open("D:\\3-2\\Minor Project\\user_logo.png")
        self.bot_logo = self.bot_logo.resize((30, 30), Image.LANCZOS)  # Update resampling method
        self.user_logo = self.user_logo.resize((30, 30), Image.LANCZOS)  # Update resampling method
        self.bot_logo = ImageTk.PhotoImage(self.bot_logo)
        self.user_logo = ImageTk.PhotoImage(self.user_logo)

        # Create chat display area
        self.chat_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, bg="black", fg="white")
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create input area
        self.input_frame = tk.Frame(master, bg="black")
        self.input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        self.input_entry = tk.Entry(self.input_frame, bg="black", fg="white", insertbackground="white")
        self.input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.input_entry.bind("<Return>", self.send_message)
        self.input_entry.focus_set()  # Set focus to the input entry

        # Create send button
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, bg="black", fg="white")
        self.send_button.pack(side=tk.RIGHT, padx=(0, 10))

        # Initialize conversation
        self.current_question = 0
        self.conversation = [
            ("Hello! How are you feeling today?", None),
            ("That's great! Good mood needs a good song. Here's your playlist.", "happy"),
            ("I'm sorry to hear that. Let's try to find some music to lift your spirits.", "sad"),
            ("It's okay to feel that way. Would you like to talk about it?", "upset"),
            ("I understand. Let's focus on something positive. What are you grateful for today?", "grateful"),
            ("That's understandable. How can I support you right now?", "stressed"),
            ("I'm here to listen. What's on your mind?", None),
            ("Thank you for sharing. Remember, it's okay to not be okay. If you need support, please reach out.", None)
        ]
        self.ask_question()

    def ask_question(self):
        question, _ = self.conversation[self.current_question]
        self.display_message("Chatbot:", question, self.bot_logo)

    def send_message(self, event=None):
        message = self.input_entry.get().strip().lower()
        if message:
            self.display_message("User:", message, self.user_logo)
            self.input_entry.delete(0, tk.END)
            self.current_question += 1
            if self.current_question < len(self.conversation):
                self.ask_question()
            else:
                messagebox.showinfo("Chatbot", "I recommend listening to some feel-good songs. Music can help improve your mood. Goodbye! Take care.")
                self.master.destroy()

    def display_message(self, username, message, logo):
        self.chat_display.image_create(tk.END, image=logo)
        self.chat_display.insert(tk.END, "\n" + username + " " + message + "\n\n", ('username', 'message'))
        self.chat_display.see(tk.END)

root = tk.Tk()
root.configure(background='black')
app = MoodMosaicChatbot(root)
app.chat_display.tag_configure('username', font=('Helvetica', 10, 'bold'), foreground='gray')
app.chat_display.tag_configure('message', font=('Helvetica', 10), foreground='white')
root.mainloop()
