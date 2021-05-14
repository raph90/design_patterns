# base class
class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


# this is where problems appear.
# We only have one interface to work with
class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok
        pass

    # we can't really do this, because
    # fax still appears on the API

    def fax(self, document):
        pass

    def scan(self, document):
        raise NotImplementedError("Printer cannot scan")
