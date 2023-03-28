class Estudante:
    def __init__(self, aluno, matematica, portugues, falta):
        self.aluno = aluno
        self.matematica = matematica
        self.portugues = portugues
        self.falta = falta

    @property
    def portugues(self):
        return self.portugues

    @portugues.setter
    def portugues(self, portugues):
        self.portugues = portugues

    @property
    def aluno(self):
        return self.aluno

    @aluno.setter
    def aluno(self, aluno):
        self.aluno = aluno

    @property
    def matematica(self):
        return self.matematica

    @matematica.setter
    def matematica(self, matematica):
        self.matematica = matematica

    @property
    def faltas(self):
        return self.faltas

    @faltas.setter
    def faltas(self, faltas):
        self.faltas = faltas


estudante1 = Estudante('Rafael', '8.5', '7.0', '3')

print(estudante1.aluno)
print(estudante1.portugues)
print(estudante1.matematica)
print(estudante1.falta)
