import subprocess
import typing as t
from dataclasses import dataclass
from enum import Enum


class Sound(Enum):
    BASSO = "Basso"
    BLOW = "Blow"
    BOTTLE = "Bottle"
    FROG = "Frog"
    FUNK = "Funk"
    GLASS = "Glass"
    HERO = "Hero"
    MORSE = "Morse"
    PING = "Ping"
    POP = "Pop"
    PURR = "Purr"
    SOSUMI = "Sosumi"
    SUBMARINE = "Submarine"
    TINK = "Tink"

    def play(self) -> None:
        args = ["afplay", f"/System/Library/Sounds/{self.value}.aiff"]
        subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


@dataclass
class Notification:

    message: str
    title: t.Optional[str] = None
    subtitle: t.Optional[str] = None
    sound: t.Optional[Sound] = None

    def __str__(self) -> str:
        """Convert the class to an applescript."""
        osascript = f'display notification "{self.message}"'

        if self.title is not None:
            osascript += f' with title "{self.title}"'

        if self.subtitle is not None:
            osascript += f' subtitle "{self.subtitle}"'

        if self.sound is not None:
            osascript += f' sound name "{self.sound.value}"'

        return osascript

    def send(self) -> subprocess.Popen[bytes]:
        """Send the notification."""
        args = ["/usr/bin/osascript", "-e", f"{self}"]
        output = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if output.returncode:
            raise Exception("An error occurred.")
        return output


def notify(
    message: str,
    title: t.Optional[str] = None,
    subtitle: t.Optional[str] = None,
    sound: t.Optional[str] = None,
) -> None:
    """Send an AppleScript notification."""

    sound_ = sound if sound is None else Sound(sound.title())
    notification = Notification(message, title, subtitle, sound_)
    notification.send()


def play_sound(sound: str) -> None:
    """Play a sound."""
    sound_ = sound if sound is None else Sound(sound.title())
    sound_.play()


__all__ = ["notify", "play_sound"]
