from typing import NamedTuple, Union
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

# import midi_abstraction

Instrument = NamedTuple("Instrument", [("name", str), ("code", int)])


class Instruments:
    BONGO = Instrument("bongo", 0)
    KEYBOARD = Instrument("keyboard", 1)
    MEOW = Instrument("meow", 3)
    CYMBAL = Instrument("cymbal", 4)
    MARIMBA = Instrument("marimba", 4)
    TAMBOURINE = Instrument("tambourine", 6)
    COWBELL = Instrument("cowbell", 7)


Key = NamedTuple("Key", [("name", str), ("code", int)])


class Keys:
    ONE = Key("one", 1)
    TWO = Key("two", 2)
    THREE = Key("three", 3)
    FOUR = Key("four", 4)
    FIVE = Key("five", 5)
    SIX = Key("six", 6)
    SEVEN = Key("sven", 7)
    EIGHT = Key("eight", 8)
    NINE = Key("nine", 9)
    ZERO = Key("zero", 0)
    SPACE = Key("space", 0)
    A = Key("a", 1)
    D = Key("d", 0)
    C = Key("c", 1)
    Q = Key("q", 1)
    W = Key("w", 2)
    E = Key("e", 3)
    R = Key("r", 4)
    T = Key("t", 5)
    Y = Key("y", 6)
    Z = Key("z", 6)
    U = Key("u", 7)
    I = Key("i", 8)
    O = Key("o", 9)
    P = Key("p", 0)
    B = Key("b", 1)
    F = Key("f", 1)


Note = NamedTuple("Note", [("name", str), ("instrument", Instrument), ("key", Key)])


class Notes:
    C = Note("c", Instruments.KEYBOARD, Keys.ONE)
    CS = Note("cs", Instruments.KEYBOARD, Keys.TWO)
    D = Note("d", Instruments.KEYBOARD, Keys.THREE)
    DS = Note("d", Instruments.KEYBOARD, Keys.FOUR)
    E = Note("e", Instruments.KEYBOARD, Keys.FIVE)
    F = Note("f", Instruments.KEYBOARD, Keys.SIX)
    FS = Note("fs", Instruments.KEYBOARD, Keys.SEVEN)
    G = Note("g", Instruments.KEYBOARD, Keys.EIGHT)
    GS = Note("gs", Instruments.KEYBOARD, Keys.NINE)
    A = Note("a", Instruments.KEYBOARD, Keys.ZERO)


class BongoNote:
    _delayValue: int
    _browser: Firefox
    _value: Note

    def __init__(self, browser: Firefox, val: Note) -> None:
        self._browser = browser
        self._value = val
        self._delayValue = 0

    def _play_state(self, state: bool):
        k = self._value.key
        i = self._value.instrument
        s = "true" if state else "false"
        self._browser.execute_script(f"$.play({i.code}, {k.code}, {s})")

    def play(self, delay: Union[None, int] = None, repeat: Union[None, int] = None):
        """
        Plays this note, with a delay defaulting to 0.1 (in seconds),
        and the number of times to repeat.
        """
        self._delayValue = delay or 0.1
        for _ in range(0, repeat or 1):
            self._play_state(True)
            sleep(self._delayValue)
            self._play_state(False)


class Bongo:
    browser: Firefox

    def __init__(self):
        opts = Options()
        opts.set_headless()
        self.browser = Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get("https://bongo.cat")

    def note(self, note: Note):
        return BongoNote(self.browser, note)

    def end(self):
        self.browser.close()
