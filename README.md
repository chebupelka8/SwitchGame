<p align="center">
  <img src="assets/switch_logo.png"
</p>

<h1></h1>
<p align="center">

  <img src="https://img.shields.io/badge/version-v0.1.0-green">
  <img src="https://img.shields.io/github/license/chebupelka8/Engine">
  <img src="https://img.shields.io/github/commit-activity/t/chebupelka8/Engine"> 
  <img src="https://img.shields.io/github/stars/chebupelka8/Engine">
  <img src="https://img.shields.io/github/watchers/chebupelka8/Engine">
  
</p>

Switch Game - is an Engine to create games based on python. It supports some sprites like a StaticSprite, AnimatedSprite and many useful classes such as Image, Animation, Tileset and other. This project is in development, but you can already use it in your games. 

<h2>Wiki</h2>
<h3>Import</h3>

```python
from SwitchGame import *
```

<h3>How to create window</h3>

```python
from SwitchGame import *


app = WindowLoop(Vec2(1000, 600))

def main():
    while True: # mainloop
        app.update_display()


if __name__ == "__main__":
    main()
```

<h3>Basic class</h3>

```python
from SwitchGame import *


class Main(WindowLoop):
    def __init__(self) -> None:
        super().__init__(Vec2(1000, 600), 165)
    
    def update_events(self, __event) -> None:
        if __event.type == KEYDOWN:
            print("key pressed")

        else:
            super().update_events(__event)
    
    def main(self) -> None:
        while True: # mainloop
            self.update_display()


if __name__ == "__main__":
    Main().main()
```