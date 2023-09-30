from dataclasses import dataclass, field


class EmailNotifier:
    def send_email(self, recipient: str, message: str):
        print(f"Sending email to {recipient}: '{message}'")


class SMSNotifier:
    def send_sms(self, phone: str, message: str):
        print(f"Sending SMS to {phone}: '{message}'")


@dataclass
class NotificationSystem:
    recipient: str
    phone: str
    notifiers: list[EmailNotifier | SMSNotifier] = field(default_factory=list)

    def notify(self, message: str) -> None:
        for notifier in self.notifiers:
            if isinstance(notifier, EmailNotifier):
                notifier.send_email(self.recipient, message)
            else:
                notifier.send_sms(self.phone, message)

    def add_notifier(self, notifier: EmailNotifier | SMSNotifier) -> None:
        self.notifiers.append(notifier)


class PaymentSystem(NotificationSystem):
    def start_maintenance(self) -> None:
        self.notify("Maintenance started")


class AuthenticationSystem(NotificationSystem):
    def clear_tokens(self) -> None:
        self.notify("Tokens cleared")


def main() -> None:
    payment_system = PaymentSystem("hi@arjancodes.com", "+31612345678")
    authentication_system = AuthenticationSystem("hi@arjancodes.com", "+31612345678")
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    payment_system.add_notifier(email_notifier)
    payment_system.add_notifier(sms_notifier)
    authentication_system.add_notifier(email_notifier)

    payment_system.start_maintenance()
    authentication_system.clear_tokens()


if __name__ == "__main__":
    main()
