import keyboard
import threading


class Key:
    pressed_keys = set()
    
    @classmethod
    def get_pressed(cls):
        def handle_key_press(event):
            if event.event_type == keyboard.KEY_DOWN:
                cls.pressed_keys.add(event.name)
            if event.event_type == keyboard.KEY_UP:
                cls.pressed_keys.pop(event.name)
        
        keyboard.on_press(callback=handle_key_press)
        keyboard.on_release(callback=handle_key_press)
        threading.Thread(target=keyboard.wait, args=(1,)).start()
        return cls.pressed_keys

    def __del__(self):
        keyboard.unhook_all()  # Заменено на удаление всех обратных вызовов
    # def __del__(self):
    #     keyboard.remove_hook(handle_key_press)

# import threading

# class Key:
#     def __init__(self):
#         self.pressed_keys = []

#     def get_pressed(self):
#         thread = threading.Thread(target=self.__check_keys)
#         thread.start()
#         return self.pressed_keys

#     def __check_keys(self):
#         while True:
#             keys = pygame.key.get_pressed()
#             for key in keys:
#                 if pygame.key.get_pressed(key):
#                     self.pressed_keys.append(key)