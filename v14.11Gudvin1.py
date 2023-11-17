from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.clock import Clock
import webbrowser

class HelloScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Добро пожаловать в HelloFriend!", color=(1, 1, 1, 1))  # Белый цвет текста
        button = Button(text="Привет, приятель", background_color=(0, 0.5, 1, 1))  # Голубой цвет фона кнопки
        button.bind(on_press=self.on_hello_button_press)
        layout.add_widget(label)
        layout.add_widget(button)
        self.add_widget(layout)

        with layout.canvas.before:
            Color(1, 0, 0, 1)  # Красный цвет фона HelloScreen
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

    def on_hello_button_press(self, instance):
        self.manager.current = "registration"

class RegistrationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Зарегистрируйтесь:", color=(1, 0, 0, 1))  # Красный цвет текста
        self.username_input = TextInput(hint_text="Имя пользователя")
        self.password_input = TextInput(hint_text="Пароль", password=True)
        button = Button(text="Зарегистрироваться", background_color=(0, 1, 0, 1))  # Зеленый цвет фона кнопки
        button.bind(on_press=self.on_registration_button_press)
        layout.add_widget(label)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(button)
        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 1)  # Черный цвет фона RegistrationScreen
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

    def on_registration_button_press(self, instance):
        # Здесь вы можете добавить код для обработки регистрации пользователя
        self.manager.current = "wish_execution"

class WishExecutionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        label = Label(text="Привет, приятель!", color=(1, 1, 0, 1))  # Желтый цвет текста
        button_wish = Button(text="Исполнение Вашего желания", background_color=(1, 0.5, 0, 1))  # Оранжевый цвет фона кнопки
        button_exit = Button(text="Выйти из приложения", background_color=(1, 0, 0, 1))  # Красный цвет фона кнопки
        button_wish.bind(on_press=self.on_wish_button_press)
        button_exit.bind(on_press=self.on_exit_button_press)
        layout.add_widget(label)
        layout.add_widget(button_wish)
        layout.add_widget(button_exit)
        self.add_widget(layout)

        with layout.canvas.before:
            Color(0, 0, 0, 1)  # Черный цвет фона WishExecutionScreen
            self.rect = Rectangle(pos=layout.pos, size=layout.size)

    def on_wish_button_press(self, instance):
        webbrowser.open("https://google.com")

    def on_exit_button_press(self, instance):
        popup = Popup(title='Прощайте!',
                      content=Label(text='Приложение закроется через 3 секунды'),
                      auto_dismiss=False)
        popup.open()
        Clock.schedule_once(lambda dt: App.get_running_app().stop(), 3)

class HelloFriendApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HelloScreen(name="hello"))
        sm.add_widget(RegistrationScreen(name="registration"))
        sm.add_widget(WishExecutionScreen(name="wish_execution"))
        return sm

if __name__ == '__main__':
    HelloFriendApp().run()
