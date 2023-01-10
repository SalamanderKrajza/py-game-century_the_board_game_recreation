def game_record(self, previous_record = 999, update=False):
    """Method used to display current game record inside history scrollbox or update the record text file if update=True"""
    import datetime
    from modules.controller.add_to_history import add_to_history
    mode = 'w'*(update)+'rt'*(not update)
    c1 = '<font color=\"#600\">' 
    c2 = '</font>'

    path = f'externaldata/record.txt'
    RecordFile = open(path, newline='', mode=mode)
    if update and int(previous_record)>=int(self.Game.turn_no):
        now = datetime.datetime.now()
        HTMLtext = 'You won! The game is finished. This is new record!'
        RecordFile.write(f'{now.year}.{now.month:02d}.{now.day:02d};{now.hour:02d}:{now.minute:02d};{self.Game.turn_no};{self.Game.CurrentPlayer.name}')
    else:
        HTMLtext = f"You won! However, you didn't break the record this time!"
    add_to_history(Ui=self, HTMLtext=HTMLtext)

    RecordFile.close()
    return(previous_record)


def get_game_record_from_file(self):
    with open(f'externaldata/record.txt', newline='', mode='rt') as record_file:
        self.record = record_file.read().split(";")

def generate_record_announcement(self):
    c1 = '<font color=\"#600\">' 
    c2 = '</font>'
    return (
        f'Your goal is to get {c1}{self.Game.riches_maximum} riches{c2} as soon as possible<br>'
        f'Current record is set at {c1}{self.record[2]}{c2} turns by {c1}{self.record[3]}{c2} at {self.record[0]} {self.record[1]}.'
        )
