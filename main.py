import arcade
import arcade.gui
import random

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Wordle - Created in Python by Dylan James"
PRIMARY_BACK_GROUND_COLOR = arcade.color.DARK_SLATE_BLUE

secondary_back_ground_color = arcade.color.SAND


class MenuView(arcade.View):
    def set_mouse_platform_visible(self, platform_visible=None):
        pass

    def setup(self):
        pass

    def __init__(self):
        super().__init__()

        # UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # background color
        arcade.set_background_color(PRIMARY_BACK_GROUND_COLOR)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        start_button = arcade.gui.UIFlatButton(text="Start Wordle", width=200)
        self.v_box.add(start_button.with_space_around(bottom=20))

        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=20))

        @start_button.event("on_click")
        def on_click_start(event):
            if event:
                wordle_view = WordleView()
                wordle_view.setup()
                self.window.show_view(wordle_view)

        @settings_button.event("on_click")
        def on_click_settings(event):
            if event:
                settings_view = SettingView()
                settings_view.setup()
                self.window.show_view(settings_view)

        @quit_button.event("on_click")
        def on_click_exit(event):
            if event:
                arcade.exit()

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()


class WordleView(arcade.View):
    def __init__(self):
        super().__init__()

        # UI manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Current button index
        self.row = 1
        self.column = 1
        self.current = "a1"

        f = open("words.txt", 'r')
        self.word = str(random_line(f)).strip().lower()
        # print(self.word)
        f.close()

        self.game_active = True

        self.words = []
        with open("words.txt", 'r') as file:
            for line in file:
                self.words.append(line.strip().lower())

        # Background color
        global secondary_back_ground_color
        arcade.set_background_color(secondary_back_ground_color)
        self.normal_button_texture = arcade.load_texture(":resources:gui_basic_assets/button_square_blue_pressed.png")
        self.pressed_button_texture = arcade.load_texture(":resources:gui_basic_assets/button_square_blue.png")
        self.green_normal_button_texture = arcade.load_texture("project_resources/button_square_green.png")
        self.blue_normal_button_texture = arcade.load_texture("project_resources/button_square_blue2.png")
        self.gray_normal_button_texture = arcade.load_texture("project_resources/button_square_gray.png")

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()
        self.h_box1 = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box2 = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box3 = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box4 = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box5 = arcade.gui.UIBoxLayout(vertical=False)
        self.h_box6 = arcade.gui.UIBoxLayout(vertical=False)

        # Create the buttons
        # A
        self.a1 = arcade.gui.UITextureButton(width=40, height=45, texture=self.normal_button_texture)
        self.h_box1.add(self.a1.with_space_around(left=10, right=10))

        self.a2 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box1.add(self.a2.with_space_around(left=10, right=10))

        self.a3 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box1.add(self.a3.with_space_around(left=10, right=10))

        self.a4 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box1.add(self.a4.with_space_around(left=10, right=10))

        self.a5 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box1.add(self.a5.with_space_around(left=10, right=10))

        self.v_box.add(self.h_box1.with_space_around(bottom=10))

        # B

        self.b1 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box2.add(self.b1.with_space_around(left=10, right=10))

        self.b2 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box2.add(self.b2.with_space_around(left=10, right=10))

        self.b3 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box2.add(self.b3.with_space_around(left=10, right=10))

        self.b4 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box2.add(self.b4.with_space_around(left=10, right=10))

        self.b5 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box2.add(self.b5.with_space_around(left=10, right=10))

        self.v_box.add(self.h_box2.with_space_around(bottom=10))

        # C

        self.c1 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box3.add(self.c1.with_space_around(left=10, right=10))

        self.c2 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box3.add(self.c2.with_space_around(left=10, right=10))

        self.c3 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box3.add(self.c3.with_space_around(left=10, right=10))

        self.c4 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box3.add(self.c4.with_space_around(left=10, right=10))

        self.c5 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box3.add(self.c5.with_space_around(left=10, right=10))

        self.v_box.add(self.h_box3.with_space_around(bottom=10))

        # D
        self.d1 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box4.add(self.d1.with_space_around(left=10, right=10))

        self.d2 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box4.add(self.d2.with_space_around(left=10, right=10))

        self.d3 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box4.add(self.d3.with_space_around(left=10, right=10))

        self.d4 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box4.add(self.d4.with_space_around(left=10, right=10))

        self.d5 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box4.add(self.d5.with_space_around(left=10, right=10))

        self.v_box.add(self.h_box4.with_space_around(bottom=10))

        # E

        self.e1 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box5.add(self.e1.with_space_around(left=10, right=10))

        self.e2 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box5.add(self.e2.with_space_around(left=10, right=10))

        self.e3 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box5.add(self.e3.with_space_around(left=10, right=10))

        self.e4 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box5.add(self.e4.with_space_around(left=10, right=10))

        self.e5 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box5.add(self.e5.with_space_around(left=10, right=10))

        self.v_box.add(self.h_box5.with_space_around(bottom=10))

        # F

        self.f1 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box6.add(self.f1.with_space_around(left=10, right=10))

        self.f2 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box6.add(self.f2.with_space_around(left=10, right=10))

        self.f3 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box6.add(self.f3.with_space_around(left=10, right=10))

        self.f4 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box6.add(self.f4.with_space_around(left=10, right=10))

        self.f5 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
        self.h_box6.add(self.f5.with_space_around(left=10, right=10))

        self.v_box.add(self.h_box6.with_space_around(bottom=10))

        self.game_messages = arcade.gui.UILabel(text="Game Messages:", width=100, height=100,
                                                text_color=arcade.color.BLUE, bold=True)
        self.v_box.add(self.game_messages.with_space_around(top=20, bottom=20))
        self.game_messages.fit_content()

        self.restart_button = arcade.gui.UIFlatButton(text="Restart", width=150, height=50)
        self.v_box.add(self.restart_button.with_space_around(bottom=10))

        self.back_button = arcade.gui.UIFlatButton(text="Main Menu", width=150, height=50)
        self.v_box.add(self.back_button)

        # @restart_button.event("on_click")
        @self.restart_button.event("on_click")
        def on_click_restart(event):
            if event:
                for row in range(1, 7):
                    for column in range(1, 6):
                        button = self.get_button_object(row, column)
                        button.text = ""
                        button.texture = self.normal_button_texture

                words_file = open("words.txt", 'r')
                self.word = str(random_line(words_file)).strip().lower()
                print(self.word)
                f.close()
                self.row = 1
                self.column = 1
                self.game_active = True

                self.set_message_text("Game Messages:")

        @self.back_button.event("on_click")
        def on_click_back(event):
            if event:
                menu_view = MenuView()
                menu_view.setup()
                self.window.show_view(menu_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def setup(self):
        pass

    def on_show(self):
        """ Called when switching to this view"""
        # arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def next_button(self):
        if self.column + 1 <= 6:
            self.column += 1

    def previous_button(self):
        if self.column - 1 >= 1:
            self.column -= 1
            self.set_text("", False)

    def get_button_object(self, row, column):
        x = "a"
        if row == 1:
            x = "a"
        elif row == 2:
            x = "b"
        elif row == 3:
            x = "c"
        elif row == 4:
            x = "d"
        elif row == 5:
            x = "e"
        elif row == 6:
            x = "f"

        button_name = x + str(column)
        try:
            button = getattr(self, button_name)
            return button
        except AttributeError:
            return False

    def set_text(self, text, pressed):
        if not self.get_button_object(self.row, self.column):
            return
        button = self.get_button_object(self.row, self.column)
        button.text = str(text)
        if pressed:
            button.texture = self.pressed_button_texture
        else:
            button.texture = self.normal_button_texture
            button.trigger_full_render()

    def set_message_text(self, text):
        self.game_messages.text = text
        self.game_messages.fit_content()

    def parse_row(self):
        if not self.column == 6:
            return
        word = ""
        buttons = []
        for column in range(1, 6):
            button = self.get_button_object(self.row, column)
            word += button.text
            buttons.append(button)
        if word not in self.words:
            self.set_message_text("Game Messages: Word not in list")
            return
        if word == self.word:
            for button in buttons:
                button.texture = self.green_normal_button_texture
                button.trigger_full_render()
            self.set_message_text("Game Messages: Correct!")
            self.game_active = False
            return
        index = 0
        for letter in word:
            if letter in self.word:
                indices = [i for i in range(len(self.word)) if self.word[i] == letter]
                if index in indices:
                    buttons[index].texture = self.green_normal_button_texture
                else:
                    buttons[index].texture = self.blue_normal_button_texture
            else:
                buttons[index].texture = self.gray_normal_button_texture
            index += 1
        self.set_message_text("Game Messages:")

        self.row = self.row + 1
        self.column = 1

        if self.row == 7:
            self.game_active = False
            self.set_message_text("Game Messages: Game Over!")

    def on_key_press(self, key, _modifiers):
        if self.game_active:
            if 97 <= key <= 122:
                self.set_text(chr(key), True)
                self.next_button()
            if key == 65288:
                self.previous_button()
            if key == 65293:
                self.parse_row()

    def on_hide_view(self):
        self.manager.disable()


class SettingView(arcade.View):
    def __init__(self):
        super().__init__()

        # UI manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Background color
        arcade.set_background_color(PRIMARY_BACK_GROUND_COLOR)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        self.dark_mode = False
        self.dark_mode_button = arcade.gui.UIFlatButton(text="Enable Dark Mode", width=150)
        self.back_button = arcade.gui.UIFlatButton(text="Back", width=150)
        self.v_box.add(self.dark_mode_button)
        self.v_box.add(self.back_button.with_space_around(top=20))

        global secondary_back_ground_color
        if secondary_back_ground_color == arcade.color.BLACK:
            self.dark_mode = True
            self.dark_mode_button.text = "Disable Dark Mode"

        @self.dark_mode_button.event("on_click")
        def on_click_dark_mode(event):
            if event:
                global secondary_back_ground_color
                if not self.dark_mode:
                    self.dark_mode = True
                    self.dark_mode_button.text = "Disable Dark Mode"
                    secondary_back_ground_color = arcade.color.BLACK
                else:
                    self.dark_mode = False
                    self.dark_mode_button.text = "Enable Dark Mode"
                    secondary_back_ground_color = arcade.color.SAND

        @self.back_button.event("on_click")
        def on_click_back(event):
            if event:
                menu_view = MenuView()
                menu_view.setup()
                self.window.show_view(menu_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def setup(self):

        pass

    def on_show(self):
        """ Called when switching to this view"""
        # arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_hide_view(self):
        self.manager.disable()


def random_line(file):
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = aline
    return line


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
