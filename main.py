import tkinter as tk
from PIL import ImageTk, Image
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Rock Paper Scissor')
        self.root.geometry('800x680')
        self.root.resizable(False, False)

        # Initialize scores and round count
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 5

        # Create Canvas
        self.canvas = tk.Canvas(root, width=800, height=680, bg="#f0f0f0")
        self.canvas.pack()

        # Load Images
        self.load_images()

        # Display Initial Images
        self.display_initial_images()

        # Display Scores
        self.display_scores()

        # Create Buttons
        self.create_buttons()

    def load_images(self):
        # Load and resize images
        self.default_image = self.load_and_resize_image("default.jpeg", (300, 300))
        self.default_image_flipped = self.load_and_resize_image("default.jpeg", (300, 300), flip=True)

        self.rock_image = self.load_and_resize_image("rock.jpeg", (300, 300))
        self.rock_image_flipped = self.load_and_resize_image("rock.jpeg", (300, 300), flip=True)

        self.paper_image = self.load_and_resize_image("paper.jpeg", (300, 300))
        self.paper_image_flipped = self.load_and_resize_image("paper.jpeg", (300, 300), flip=True)

        self.scissor_image = self.load_and_resize_image("scissor.jpeg", (300, 300))
        self.scissor_image_flipped = self.load_and_resize_image("scissor.jpeg", (300, 300), flip=True)

        self.selection_image = self.load_and_resize_image("selection.jpg", (300, 130))

    def load_and_resize_image(self, path, size, flip=False):
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            if flip:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            return ImageTk.PhotoImage(img)
        except IOError:
            print(f"Error: Unable to load image at path '{path}'. Please check the file.")
            return None

    def display_initial_images(self):
        # Display player and computer default images
        self.player_image_id = self.canvas.create_image(50, 100, anchor=tk.NW, image=self.default_image)
        self.computer_image_id = self.canvas.create_image(450, 100, anchor=tk.NW, image=self.default_image_flipped)

        # Display selection images
        self.player_selection_id = self.canvas.create_image(50, 450, anchor=tk.NW, image=self.selection_image)
        self.computer_selection_id = self.canvas.create_image(450, 450, anchor=tk.NW, image=self.selection_image)

    def display_scores(self):
        # Display player and computer scores
        self.score_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.score_frame.place(x=250, y=20)

        self.player_score_label = tk.Label(self.score_frame, text=f"Player: {self.player_score}", font=('Arial', 16), bg="#f0f0f0")
        self.player_score_label.grid(row=0, column=0, padx=20)

        self.computer_score_label = tk.Label(self.score_frame, text=f"Computer: {self.computer_score}", font=('Arial', 16), bg="#f0f0f0")
        self.computer_score_label.grid(row=0, column=1, padx=20)

        self.rounds_label = tk.Label(self.score_frame, text=f"Rounds: {self.rounds_played}/{self.max_rounds}", font=('Arial', 16), bg="#f0f0f0")
        self.rounds_label.grid(row=0, column=2, padx=20)

    def create_buttons(self):
        # Create Rock, Paper, Scissor, and Clear buttons
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.place(x=40, y=545)

        self.rock_btn = tk.Button(button_frame, text='Rock', width=10, command=lambda: self.play_game('rock'))
        self.rock_btn.grid(row=0, column=0, padx=10, pady=10)

        self.paper_btn = tk.Button(button_frame, text='Paper', width=10, command=lambda: self.play_game('paper'))
        self.paper_btn.grid(row=0, column=1, padx=10, pady=10)

        self.scissor_btn = tk.Button(button_frame, text='Scissor', width=10, command=lambda: self.play_game('scissor'))
        self.scissor_btn.grid(row=0, column=2, padx=10, pady=10)

        self.clear_btn = tk.Button(button_frame, text='Clear', width=10, command=self.clear)
        self.clear_btn.grid(row=0, column=3, padx=10, pady=10)

    def play_game(self, player_choice):
        if self.rounds_played >= self.max_rounds:
            return  # Prevent playing more than max rounds

        # Increment the round count
        self.rounds_played += 1
        self.rounds_label.config(text=f"Rounds: {self.rounds_played}/{self.max_rounds}")

        # Map choices to numbers
        choices = ['rock', 'paper', 'scissor']
        computer_choice = random.choice(choices)

        # Update images based on choices
        self.update_images(player_choice, computer_choice)

        # Determine result
        result = self.determine_winner(player_choice, computer_choice)

        # Update scores and display result
        self.update_result(result)

        # Check if max rounds are reached
        if self.rounds_played >= self.max_rounds:
            self.end_game()

    def update_images(self, player_choice, computer_choice):
        # Update player image
        player_image = self.get_image(player_choice)
        if player_image:
            self.canvas.itemconfigure(self.player_image_id, image=player_image)
            self.canvas.image = player_image  # Prevent garbage collection

        # Update computer image
        computer_image = self.get_flipped_image(computer_choice)
        if computer_image:
            self.canvas.itemconfigure(self.computer_image_id, image=computer_image)
            self.canvas.image_flipped = computer_image  # Prevent garbage collection

    def get_image(self, choice):
        if choice == 'rock':
            return self.rock_image
        elif choice == 'paper':
            return self.paper_image
        elif choice == 'scissor':
            return self.scissor_image
        else:
            return self.default_image

    def get_flipped_image(self, choice):
        if choice == 'rock':
            return self.rock_image_flipped
        elif choice == 'paper':
            return self.paper_image_flipped
        elif choice == 'scissor':
            return self.scissor_image_flipped
        else:
            return self.default_image_flipped

    def determine_winner(self, player, computer):
        if player == computer:
            return 'Draw'
        elif (player == 'rock' and computer == 'scissor') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissor' and computer == 'paper'):
            return 'You Won'
        else:
            return 'Computer Won'

    def update_result(self, result):
        # Remove previous result if exists
        self.canvas.delete('result')

        # Update scores
        if result == 'You Won':
            self.player_score += 1
        elif result == 'Computer Won':
            self.computer_score += 1

        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")

        # Display new result
        self.canvas.create_text(400, 600, text=f"Result: {result}",
                                fill="black", font=('Arial', 24, 'bold'), tag='result')

    def clear(self):
        # Reset images to default
        self.canvas.itemconfigure(self.player_image_id, image=self.default_image)
        self.canvas.itemconfigure(self.computer_image_id, image=self.default_image_flipped)

        # Reset scores and rounds
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.player_score_label.config(text=f"Player: {self.player_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")
        self.rounds_label.config(text=f"Rounds: {self.rounds_played}/{self.max_rounds}")

        # Remove result and final result texts
        self.canvas.delete('result')
        self.canvas.delete('final_result')

    def end_game(self):
        # Determine the overall winner
        if self.player_score > self.computer_score:
            final_result = "You are the overall winner!"
        elif self.player_score < self.computer_score:
            final_result = "Computer is the overall winner!"
        else:
            final_result = "It's a draw overall!"

        # Display final result
        self.canvas.create_text(400, 650, text=final_result, fill="black", font=('Arial', 24, 'bold'), tag='final_result')

        # Schedule the game to reset after 3 seconds (3000 milliseconds)
        self.root.after(3000, self.reset_game)

    def reset_game(self):
        # Remove final result text
        self.canvas.delete('final_result')

        # Reset the game to initial state
        self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
