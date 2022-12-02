import time
from plyer import notification

class app:
    def __init__(self):
        self.pomodoro = input('Pomodoro: ')
        self.descanso = input('Descanso: ')
        self.longBreak = input('Descanso largo: ')

        pomodoro = int(self.pomodoro)
        descanso = int(self.descanso)
        longBreak = int(self.longBreak)

        print('##########Pomodoro timer##########')

        while pomodoro >= 0:
            print(f'Pomodoro: {pomodoro}')
            pomodoro -= 1
            time.sleep(60)
            if pomodoro == 0:
                notification.notify(title='Fin de simulación', message='La simulación ha finalizado')
                break
        while descanso >= 0:
            print(f'Descanso: {descanso}')
            descanso -= 1
            time.sleep(60)
            break
        while longBreak >= 0:
            print(f'Descanso largo: {longBreak}')
            longBreak -= 1
            time.sleep(60)
            break
app()