# main.py
import json
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (360, 640)

ROASTS = [
    "You call that an answer? Pathetic.",
    "Wrong. Try not to embarrass us both.",
    "Another failure. Even the chalk feels sorry.",
    "Close, but no. Come back when your brain warms up.",
    "You were brave. That’s the only compliment I can give."
]

WIN_LINES = [
    "**Victory is carved by the relentless.**",
    "**You answered — the battlefield remembers.**",
    "**Good. You survived another question.**"
]

def load_formulas(path="formulas.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

class QuizScreen(BoxLayout):
    def __init__(self, formulas, **kwargs):
        super().__init__(orientation="vertical", padding=12, spacing=12, **kwargs)
        self.formulas = formulas
        self.keys = list(formulas.keys())
        self.lives = 3
        self.build_ui()
        self.next_question()

    def build_ui(self):
        self.title = Label(text="Formula Warrior", font_size='24sp', size_hint_y=None, height=40)
        self.add_widget(self.title)

        self.qlabel = Label(text="", halign="center", valign="middle")
        self.qlabel.bind(size=self.qlabel.setter('text_size'))
        self.add_widget(self.qlabel)

        self.input = TextInput(hint_text="Type the label or RHS exactly", multiline=False, size_hint_y=None, height=40)
        self.add_widget(self.input)

        btn_layout = BoxLayout(size_hint_y=None, height=44, spacing=8)
        self.submit_btn = Button(text="Submit", on_press=self.on_submit)
        self.next_btn = Button(text="Skip", on_press=lambda *_: self.next_question())
        btn_layout.add_widget(self.submit_btn)
        btn_layout.add_widget(self.next_btn)
        self.add_widget(btn_layout)

        self.status = Label(text="Lives: 3", size_hint_y=None, height=30)
        self.add_widget(self.status)

        self.msg = Label(text="", size_hint_y=None, height=120)
        self.add_widget(self.msg)

    def next_question(self, *_):
        self.input.text = ""
        self.current_key = random.choice(self.keys)
        self.current_val = self.formulas[self.current_key]
        if random.choice([True, False]):
            self.mode = "rhs"
            self.qlabel.text = f"What's the RHS of: [b]{self.current_key}[/b] ?"
        else:
            self.mode = "lhs"
            self.qlabel.text = f"Which formula has RHS = [b]{self.current_val}[/b] ?"
        self.status.text = f"Lives: {self.lives}"
        self.msg.text = ""

    def on_submit(self, *_):
        ans = self.input.text.strip()
        if not ans:
            self.msg.text = "Type something, soldier."
            return

        correct = False
        if self.mode == "rhs":
            if ans.lower() == self.current_val.lower():
                correct = True
        else:
            if ans.lower() == self.current_key.lower():
                correct = True

        if correct:
            self.msg.text = random.choice(WIN_LINES)
            self.lives = min(3, self.lives + 1)
            self.next_question()
            return
        else:
            self.lives -= 1
            roast = random.choice(ROASTS)
            self.msg.text = f"[color=ff3333]{roast}[/color]\nCorrect: {self.current_key} = {self.current_val}"
            self.status.text = f"Lives: {self.lives}"
            if self.lives <= 0:
                self.game_over()

    def game_over(self):
        self.msg.text = "**You have been defeated. Train and return.**"
        self.input.disabled = True
        self.submit_btn.disabled = True
        self.next_btn.text = "Restart"
        self.next_btn.bind(on_press=self.on_restart)

    def on_restart(self, *_):
        self.lives = 3
        self.input.disabled = False
        self.submit_btn.disabled = False
        self.next_btn.text = "Skip"
        self.next_btn.unbind(on_press=self.on_restart)
        self.next_question()

class FormulaApp(App):
    def build(self):
        formulas = load_formulas()
        return QuizScreen(formulas)

if __name__ == "__main__":
    FormulaApp().run()
