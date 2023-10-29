from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class Handler(ABC):
    """
    Abstract base class for a handler in a chain of responsibility.

    A handler can be part of a chain of responsibility, where each handler in the chain has the opportunity to handle a
    request. If a handler cannot handle the request, it passes the request on to the next handler in the chain.

    Attributes:
        next (Optional[Handler]): The next handler in the chain.

    Methods:
        set_next(handler: Handler) -> None: Set the next handler in the chain.
        handle_click_event() -> None: Handle a click event by attempting to handle it with this handler. If this
            handler cannot handle the event, it passes the event on to the next handler in the chain.
        on_click() -> bool: Handle a click event. This method should be implemented by subclasses.
    """

    def __init__(self):
        self.next: Optional[Handler] = None

    def set_next(self, handler: "Handler") -> None:
        """Set the next handler in the chain."""
        self.next = handler

    def handle_click_event(self) -> None:
        """Handle a click event by attempting to handle it with this handler. If this handler cannot handle the event,
        it passes the event on to the next handler in the chain."""
        try:
            if self.on_click() and self.next:
                self.next.handle_click_event()
        except AttributeError:
            pass

    @abstractmethod
    def on_click(self) -> bool:
        """Handle a click event. This method should be implemented by subclasses."""
        pass


@dataclass
class Button(Handler):
    name: str = "button"
    disabled: bool = False

    def on_click(self) -> bool:
        if self.disabled:
            return True
        print(f"Button [{self.name}] handling click.")
        return False


@dataclass
class Panel(Handler):
    name: str = "panel"
    disabled: bool = False

    def on_click(self) -> bool:
        return True


@dataclass
class Window(Handler):
    name: str = "window"

    def on_click(self) -> bool:
        print(f"Window [{self.name}] handling click.")
        return True


def main() -> None:
    button = Button(name="my_button", disabled=False)
    panel = Panel(name="my_panel", disabled=False)
    window = Window(name="my_window")

    # setup the chain of responsibility
    button.set_next(panel)
    panel.set_next(window)

    button.disabled = True

    button.handle_click_event()


if __name__ == "__main__":
    main()
