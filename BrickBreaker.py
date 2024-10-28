import tkinter as tk
import random

class BrickBreaker:
    def __init__(self, master):
        self.master = master
        self.master.title("Brick Breaker")
        
        self.canvas = tk.Canvas(master, width=400, height=300, bg="black")
        self.canvas.pack()
        
        self.score = 0  # متغیر امتیاز
        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        self.paddle = self.canvas.create_rectangle(150, 280, 250, 290, fill="blue")
        self.ball = self.canvas.create_oval(190, 250, 210, 270, fill="red")  # موقعیت اولیه توپ
        self.ball_dx = 2
        self.ball_dy = -2
        self.bricks = self.create_bricks()
        
        self.master.bind("<Left>", self.move_paddle)
        self.master.bind("<Right>", self.move_paddle)
        self.update()

    def create_bricks(self):
        bricks = []
        for i in range(5):
            for j in range(8):
                x1 = j * 50
                y1 = i * 20
                brick = self.canvas.create_rectangle(x1, y1, x1 + 50, y1 + 20, fill="green")
                bricks.append(brick)
        return bricks

    def reset_game(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.canvas.delete("all")
        self.bricks = self.create_bricks()
        self.ball = self.canvas.create_oval(190, 250, 210, 270, fill="red")  # Reset ball position
        self.ball_dx = 2
        self.ball_dy = -2
        self.paddle = self.canvas.create_rectangle(150, 280, 250, 290, fill="blue")
        self.update()

    def move_paddle(self, event):
        if event.keysym == "Left":
            self.canvas.move(self.paddle, -20, 0)
        elif event.keysym == "Right":
            self.canvas.move(self.paddle, 20, 0)

        # Limit paddle movement within canvas
        paddle_pos = self.canvas.coords(self.paddle)
        if paddle_pos[0] < 0:
            self.canvas.move(self.paddle, -paddle_pos[0], 0)
        elif paddle_pos[2] > 400:
            self.canvas.move(self.paddle, 400 - paddle_pos[2], 0)

    def update(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_pos = self.canvas.coords(self.ball)

        # Check for wall collisions
        if ball_pos[0] <= 0 or ball_pos[2] >= 400:
            self.ball_dx *= -1
        if ball_pos[1] <= 0:
            self.ball_dy *= -1
        if ball_pos[3] >= 300:  # Ball fell
            self.end_game("Game Over!")  # Call end_game method when the ball falls

        # Check for paddle collision
        paddle_pos = self.canvas.coords(self.paddle)
        if (ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and 
            ball_pos[3] >= paddle_pos[1]):
            self.ball_dy *= -1
            self.ball_dx = random.choice([-2, 2])
            self.canvas.move(self.ball, 0, -5)

        # Check for brick collisions
        for brick in self.bricks:
            if self.check_collision(ball_pos, self.canvas.coords(brick)):
                self.canvas.delete(brick)
                self.bricks.remove(brick)
                self.ball_dy *= -1
                self.update_score(10)  # افزایش امتیاز به ازای شکستن آجر
                
                if self.score >= 200:
                    self.ball_dx *= 1.5  # افزایش سرعت توپ
                    self.reset_game()  # ریست کردن بلوک‌ها
                
                break

        self.master.after(20, self.update)

    def check_collision(self, ball_pos, brick_pos):
        return (ball_pos[2] >= brick_pos[0] and ball_pos[0] <= brick_pos[2] and
                ball_pos[1] <= brick_pos[3] and ball_pos[3] >= brick_pos[1])

    def update_score(self, points):
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")  # بروزرسانی متن امتیاز

    def end_game(self, message):
        self.canvas.create_text(200, 150, text=message, fill="red", font=("Arial", 24))
        self.canvas.create_text(200, 180, text=f"Final Score: {self.score}", fill="white", font=("Arial", 16))
        self.master.unbind("<Left>")
        self.master.unbind("<Right>")
        
if __name__ == "__main__":
    root = tk.Tk()
    game = BrickBreaker(root)
    root.mainloop()
