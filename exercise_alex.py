from dataclasses import dataclass, field
from typing import Protocol


class Notifier(Protocol):
    def notify(self, message: str) -> None:
        ...


@dataclass
class EmailNotifier:
    recipient: str

    def notify(self, message: str):
        print(f"Sending email to {self.recipient}: '{message}'")


@dataclass
class SMSNotifier:
    phone: str

    def notify(self, message: str):
        print(f"Sending SMS to {self.phone}: '{message}'")


@dataclass
class NotificationSystem:
    notifiers: list[Notifier] = field(default_factory=list)

    def notify(self, message: str) -> None:
        for notifier in self.notifiers:
            notifier.notify(message)

    def add_notifier(self, notifier: Notifier) -> None:
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
    email_notifier = EmailNotifier("hi.arjancodes.com")
    sms_notifier = SMSNotifier("+31612345678")

    payment_system.add_notifier(email_notifier)
    payment_system.add_notifier(sms_notifier)
    authentication_system.add_notifier(email_notifier)

    payment_system.start_maintenance()
    authentication_system.clear_tokens()


if __name__ == "__main__":
    main()
