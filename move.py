import shutil
import os
import time

class Move:

    def __init__(self, src, dst, secs):
        self.secs = secs
        self.base = os.environ['HOME']
        self.base_src = f'{self.base}/{src}'
        self.base_dst = f'{self.base}/{dst}'

    def get_archives(self):
        return os.listdir(self.base_src)

    def verify_dir(self):
        return os.path.isdir(self.base_dst)

    def create_dirs(self):
        if not self.verify_dir():
            try:
                dirs = ['Images', 'Arquives', 'Movies','Olters']
                os.mkdir(self.base_dst)
                for d in dirs:
                    os.mkdir(f'{self.base_dst}/{d}')
            except Exception:
                print('Erro: Not created directory.')
        else:
            pass
    
    def move_arquives(self):
        images_extensions = ['.jpg', '.png', '.jpeg']
        arquives_extensions = ['.pdf', '.txt', '.doc', '.docx', '.csv', '.xls', '.xlsx']
        movies_extensions = ['.m4v', '.mp4', '.3gp', '.mkv','.avi']

        arquives = self.get_archives()
        self.create_dirs()

        for arq in arquives:
            if not arq.startswith('.'):
                _, ext = os.path.splitext(arq)
                ext = str(ext).lower()
                if ext in images_extensions:
                   source = f'{self.base_src}/{arq}'
                   destine = f'{self.base_dst}/Images/{arq}'
                   shutil.move(source,destine)
                elif ext in arquives_extensions:
                   source = f'{self.base_src}/{arq}'
                   destine = f'{self.base_dst}/Arquives/{arq}'
                   shutil.move(source,destine)
                elif ext in movies_extensions:
                   source = f'{self.base_src}/{arq}'
                   destine = f'{self.base_dst}/Movies/{arq}'
                   shutil.move(source,destine)
                else:
                   source = f'{self.base_src}/{arq}'
                   destine = f'{self.base_dst}/Olters/{arq}'
                   shutil.move(source,destine)

    def mainloop(self):
        while True:
            self.move_arquives()
            time.sleep(self.secs)


if __name__ == '__main__':
    mover = Move('Downloads', 'Desktop/Movido', 1)
    mover.mainloop()