def game_record(self, previous_record = 999, update=False):
    """Method used to display current game record inside history scrollbox or update the record text file if update=True"""
    import datetime
    from modules.controller.add_to_history import add_to_history
    mode = 'w'*(update)+'rt'*(not update)
    c1 = '<font color=\"#600\">' 
    c2 = '</font>'

    path = f'externaldata/record.txt'
    RecordFile = open(path, newline='', mode=mode)

    if update == False:
        record = RecordFile.read().split(";")
        HTMLtext = (
            f'Your goal is to get {c1}{self.Game.riches_maximum} riches{c2} as soon as possible<br>'
            f'Current record is set at {c1}{record[2]}{c2} turns by {c1}{record[3]}{c2} at {record[0]} {record[1]}.')
        previous_record = record[2]
    else:
        now = datetime.datetime.now()
        HTMLtext = 'You won! The game is finished. This is new record!'
        RecordFile.write(f'{now.year}.{now.month:02d}.{now.day:02d};{now.hour:02d}:{now.minute:02d};{self.Game.turn_no};{self.Game.CurrentPlayer.name}')
    add_to_history(Ui=self, HTMLtext=HTMLtext)

    RecordFile.close()
    return(previous_record)
