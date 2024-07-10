class buahhhh:
    def __init__(Self, nama, warna, rasa):
        Self.nama = nama
        Self.warna = warna
        Self.rasa = rasa
    def get_Nama(Self):
        return Self.nama
    def get_Warna(Self):
        return Self.warna
    def get_Rasa(Self):
        return Self.rasa
    def info(self):
        return f'Nama : {self.nama}, Warna : {self.warna}, Rasa : {self.rasa}'
    
class Mangga(buahhhh):
    def __init__(Self, nama, warna, rasa, vitamin):
        super().__init__(nama, warna, rasa)
        Self.vitamin = vitamin
    def info_buah(self):
        return f'{super().info()}, vitamin : {self.vitamin}' 
    
object = Mangga('Mangga','Kuning', 'Manis', 'C')
print(object.info_buah())