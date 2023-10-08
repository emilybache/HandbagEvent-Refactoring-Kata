import approvaltests

from handbag import *


def print_event(success: bool, event: Event) -> str:
    if event is None:
        return f"Success: {success}, Event: None"
    return f"""
Success: {success}
Event(
    type: {event.type}
    size: {event.size}
    status_code: {event.status_code}
    checksum: {event.checksum}
    payload: {event.payload}
    has_checksum: {event.has_checksum}
)
    """


def test_trendy_shoulder_bag():
    input = Handbag(1, "H&M", "Trendy", "Shoulder", 0.55)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_trendy_clutch_bag():
    input = Handbag(1, "Zara", "Trendy", "Clutch", 0.2)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_trendy_fixed_bag():
    input = Handbag(1, "Esprit", "Trendy", "Fixed", 0.2)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_bad_market_fit():
    input = Handbag(1, "Debenhams", "Trendy", "Clutch", 0.35)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_dead_brand():
    input = Handbag(1, "Debenhams", "Trendy", "Shoulder", 4)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_luggage():
    input = Handbag(4, "Samsonite", "Traveller", "Trolley", 60)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_small_luggage():
    input = Handbag(2, "Samsonite", "Trendy", "Box", 10)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_many_compartments():
    input = Handbag(14, "Esprit", "Traveller", "Rucksack", 20)
    output = Event(0, 0, 0, 0, "", False)
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))


def test_missing_output():
    input = Handbag(1, "H&M", "Trendy", "Shoulder", 0.55)
    output = None
    success = init_handbag_event(input, output)
    approvaltests.verify(print_event(success, output))
