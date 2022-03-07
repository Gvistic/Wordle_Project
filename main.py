import arcade
import arcade.gui

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Wordle - Created in Python by Dylan James"
PRIMARY_BACK_GROUND_COLOR = arcade.color.DARK_SLATE_BLUE


class MenuView(arcade.View):
    def set_mouse_platform_visible(self, platform_visible=None):
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
            print("Settings:", event)

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

        # Background color
        arcade.set_background_color(arcade.color.GOLD)
        self.normal_button_texture = arcade.load_texture(":resources:gui_basic_assets/button_square_blue_pressed.png")
        self.pressed_button_texture = arcade.load_texture(":resources:gui_basic_assets/button_square_blue.png")

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
        self.a1 = arcade.gui.UITextureButton(text="", width=40, height=45, texture=self.normal_button_texture)
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
        if self.column >= 5 and self.row < 6:
            self.row += 1
            self.column = 1
        elif self.row <= 6 and self.column < 5:
            self.column += 1
        else:
            self.column = 1
            self.row = 1

    def previous_button(self):
        if self.column == 5:
            self.row -= 1
        if self.column - 1 > 1:
            self.column -= 1
        else:
            self.column = 1
        self.set_text("", False)

    def set_text(self, text, pressed):
        x = "a"
        if self.row == 1:
            x = "a"
        elif self.row == 2:
            x = "b"
        elif self.row == 3:
            x = "c"
        elif self.row == 4:
            x = "d"
        elif self.row == 5:
            x = "e"
        elif self.row == 6:
            x = "f"

        button_name = x + str(self.column)
        button = getattr(self, button_name)
        button.text = str(text)
        if pressed:
            button.texture = self.pressed_button_texture
        else:
            button.texture = self.normal_button_texture
            button.trigger_full_render()

    def on_key_press(self, key, _modifiers):
        if 97 <= key <= 122:
            self.set_text(chr(key), True)
            self.next_button()
        if key == 65288:
            self.previous_button()

    def on_hide_view(self):
        self.manager.disable()


def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
