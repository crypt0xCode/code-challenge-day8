from level3.task31.conference import Conference
from level3.task31.participant import Participant


class RegistrationSystem:
    def __init__(self, conference: Conference, participants: list):
        self.conference = conference
        self.participants = participants


    def __str__(self) -> str:
        return (f'Reg System for Conference \'{str(self.conference)}\'.\n'
                f'Current participants list: {str(self.participants)}')


    def register(self, participant: Participant) -> None:
        """
        Add participant to participants list.

        :param participant: Participant object.
        """
        if self.is_registration_available():
            self.participants.append(str(participant))
        else:
            print(f'Not enough free places for current conference!')


    def is_registration_available(self) -> bool:
        """
        Check registration availability by free places in participants list.

        :return: bool flag.
        """
        return len(self.participants) < self.conference.capacity