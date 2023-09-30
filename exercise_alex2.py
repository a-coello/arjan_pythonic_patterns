from dataclasses import dataclass, field
from functools import partial
from typing import Callable, Protocol

NotificationFn = Callable[[str], None]


def notify_email(recipient: str, message: str) -> None:
    print(f"Sending email to {recipient}: '{message}'")


def notify_sms(phone: str, message: str) -> None:
    print(f"Sending SMS to {phone}: '{message}'")


@dataclass
class NotificationSystem:
    notifiers: list[NotificationFn] = field(default_factory=list)

    def notify(self, message: str) -> None:
        for notifier in self.notifiers:
            notifier(message)

    def add_notifier(self, notifier: NotificationFn) -> None:
        self.notifiers.append(notifier)


class PaymentSystem(NotificationSystem):
    def start_maintenance(self) -> None:
        self.notify("Maintenance started")


class AuthenticationSystem(NotificationSystem):
    def clear_tokens(self) -> None:
        self.notify("Tokens cleared")


def main() -> None:
    payment_system = PaymentSystem()
    authentication_system = AuthenticationSystem()
    email_notifier = partial(notify_email, "hi@arjancodes.co")
    sms_notifier = partial(notify_sms, "+31612345678")

    payment_system.add_notifier(email_notifier)
    payment_system.add_notifier(sms_notifier)
    authentication_system.add_notifier(email_notifier)

    payment_system.start_maintenance()
    authentication_system.clear_tokens()


if __name__ == "__main__":
    main()
