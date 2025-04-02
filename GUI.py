import tkinter as tk
from tkinter import scrolledtext, font
from chatbot.bot import get_response

class AlienChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("👽 Alien Chatbot")
        master.configure(bg='#0a0a1a')
        
        # Custom font
        self.custom_font = font.Font(family='Courier', size=12)
        
        # Chat display (Terminal-style)
        self.chat_log = scrolledtext.ScrolledText(
            master,
            state='disabled',
            width=70,
            height=25,
            wrap=tk.WORD,
            bg='#001122',
            fg='#00ff00',
            insertbackground='green',
            font=self.custom_font,
            padx=10,
            pady=10
        )
        self.chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # User input (Alien-themed)
        self.entry = tk.Entry(
            master,
            width=60,
            bg='#002244',
            fg='white',
            insertbackground='white',
            font=self.custom_font,
            relief=tk.FLAT
        )
        self.entry.grid(row=1, column=0, padx=(10, 5), pady=(0, 10))
        self.entry.bind("<Return>", self._on_enter_pressed)
        self.entry.focus_set()
        
        # Send button (UFO-themed)
        self.send_button = tk.Button(
            master,
            text="🚀 Transmit",
            command=self._send_message,
            bg='#330066',
            fg='white',
            activebackground='#440088',
            activeforeground='white',
            relief=tk.FLAT,
            font=self.custom_font
        )
        self.send_button.grid(row=1, column=1, padx=(5, 10), pady=(0, 10))
        
        # Initial alien greeting
        self._update_chat_log("Zog-7", "*blinking lights* Greetings flesh-bag! Ask your primitive questions!")
        
        # Configure tags for different speakers
        self.chat_log.tag_config('alien', foreground='#00ffff')
        self.chat_log.tag_config('human', foreground='#ffffff')
    
    def _send_message(self):
        user_input = self.entry.get().strip()
        if user_input:
            self._update_chat_log("You", user_input, speaker='human')
            self.entry.delete(0, tk.END)
            
            # Get and display alien response
            response = get_response(user_input)
            self._update_chat_log("Zog-7", response, speaker='alien')
    
    def _on_enter_pressed(self, event):
        self._send_message()
    
    def _update_chat_log(self, sender, message, speaker='human'):
        self.chat_log.config(state='normal')
        
        # Insert sender with appropriate tag
        if speaker == 'alien':
            self.chat_log.insert(tk.END, f"👽 {sender}: ", 'alien')
        else:
            self.chat_log.insert(tk.END, f"🧑 {sender}: ", 'human')
            
        # Insert message
        self.chat_log.insert(tk.END, f"{message}\n\n")
        
        # Auto-scroll and lock
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    
    # Set window icon (optional)
    try:
        root.iconbitmap('alien.ico')  # Add an alien icon if available
    except:
        pass
        
    gui = AlienChatGUI(root)
    root.mainloop()