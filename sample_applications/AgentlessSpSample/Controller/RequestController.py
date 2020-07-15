from abc import ABC, abstractmethod


class RequestController(ABC):

    @abstractmethod
    def handle(self, request):
        pass
