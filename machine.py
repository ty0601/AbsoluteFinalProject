from fsm import TocMachine


def create_machine():
    machine = TocMachine(
        states=["user", "play1", "play2", "play3", "play4", "read1", "read2", "read3", "read4", "fsm"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "play1",
                "conditions": "is_going_to_play",
            },
            {
                "trigger": "advance",
                "source": "play1",
                "dest": "play2",
                "conditions": "is_going_to_play",
            },
            {
                "trigger": "advance",
                "source": "play2",
                "dest": "play3",
                "conditions": "is_going_to_play",
            },
            {
                "trigger": "advance",
                "source": "play3",
                "dest": "play4",
                "conditions": "is_going_to_play",
            },
            {
                "trigger": "advance",
                "source": "play4",
                "dest": "play4",
                "conditions": "is_going_to_play",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "read1",
                "conditions": "is_going_to_read",
            },
            {
                "trigger": "advance",
                "source": "read1",
                "dest": "read2",
                "conditions": "is_going_to_read",
            },
            {
                "trigger": "advance",
                "source": "read2",
                "dest": "read3",
                "conditions": "is_going_to_read",
            },
            {
                "trigger": "advance",
                "source": "read3",
                "dest": "read4",
                "conditions": "is_going_to_read",
            },
            {
                "trigger": "advance",
                "source": "read4",
                "dest": "read4",
                "conditions": "is_going_to_read",
            },
            {
                "trigger": "advance",
                "source": ["user", "play1", "play2", "play3", "play4", "read1", "read2", "read3", "read4"],
                "dest": "user",
                "conditions": "is_going_to_reset",
            },
            {
                "trigger": "advance",
                "source": ["play1", "play2", "play3", "play4"],
                "dest": "read1",
                "conditions": "is_going_to_read",
            },
            {
                "trigger": "advance",
                "source": ["read1", "read2", "read3", "read4"],
                "dest": "play1",
                "conditions": "is_going_to_play",
            },
            {
                "trigger": "advance",
                "source": "user",
                "dest": "fsm",
                "conditions": "is_going_to_fsm",
            },
            {"trigger": "go_back", "source": "fsm", "dest": "user"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine
