import time
import picoscroll as scroll

scroll.init()

while True:
    scroll.scroll_text("LUKB Schnuppertag", 128, 80)
    time.sleep(1)
