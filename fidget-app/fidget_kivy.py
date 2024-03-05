from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.core.window import Window

class Fidget(App):
    def build(self):
        Window.clearcolor = (0.59215686274, 0.87058823529, 1, 0.75)
        Window.softinput_mode = "below_target"
        # Desktop - Window.size = (750, 1000)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 1)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        self.fidget_text = Label(
                            text = "Fidget App",
                            color = "#000000"
                            )
        self.window.add_widget(self.fidget_text)

        self.slider_horizontal_no_trail = Slider(
                                            orientation = "horizontal",
                                            min = -100,
                                            max = 100,
                                            value = 25
                                        )
        self.window.add_widget(self.slider_horizontal_no_trail)

        self.slider_horizontal_trail = Slider(
                                            orientation = "horizontal",
                                            value_track = True,
                                            value_track_color = [1, 0, 0, 1],
                                            min = -100,
                                            max = 100,
                                            value = 25
                                        )
        self.window.add_widget(self.slider_horizontal_trail)

        self.slider_vertical_no_trail = Slider(
                                            orientation = "vertical",
                                            min = -1200,
                                            max = 1200,
                                            value = 75
                                        )
        self.window.add_widget(self.slider_vertical_no_trail)

        self.slider_vertical_trail = Slider(
                                            orientation = "vertical",
                                            value_track = True,
                                            value_track_color = [1, 0, 0, 1],
                                            min = -1200,
                                            max = 1200,
                                            value = 75
                                        )
        self.window.add_widget(self.slider_vertical_trail)

        self.text_input_singleline_text = Label(
                                        text = "Singleline Text Input",
                                        color = "#000000"
                                    )
        self.window.add_widget(self.text_input_singleline_text)

        self.text_input_singleline = TextInput(
                                        multiline = False,
                                        padding_y = (20, 20),
                                        size_hint = (1, 0.5),
                                        hint_text = "Singleline"
                                        )
        self.window.add_widget(self.text_input_singleline)

        self.text_input_multiline_text = Label(
                                            text = "Multiline Text Input",
                                            color = "#000000"
                                        )
        self.window.add_widget(self.text_input_multiline_text)

        self.text_input_multiline = TextInput(
                                        multiline = True,
                                        padding_y = (20, 20),
                                        size_hint = (1, 0.5),
                                        hint_text = "Multiline"
                                    )
        self.window.add_widget(self.text_input_multiline)

        self.fidget_button = Button(
                                text="Button",
                                size_hint = (1, 0.5),
                                bold = True,
                                background_color="#038388",
                                background_normal=""
                            )
        self.window.add_widget(self.fidget_button)

        return self.window

if __name__ == "__main__":
    Fidget().run()