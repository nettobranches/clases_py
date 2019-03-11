from django.db import models
from django.utils import timezone



class Pregunta(models.Model):
    pregunta_txt = models.CharField(max_length=400)
    materia = models.CharField(max_length=200)
    metodo = models.CharField(max_length=200)

    def __str__(self):
        return self.pregunta_txt

    def getOriginal(self):
        lst_res_o = self.respuestaoriginal_set.all()
        str_res = self.pregunta_txt

        for ro in lst_res_o:
            str_res = str_res.replace(str(ro.variable), str(ro.res) )

        # print(lst_res_o)
        return str_res

    def getRandom(self):
        lst_res_o = self.respuestaaleatoria_set.all()
        str_res = self.pregunta_txt

        for ro in lst_res_o:
            str_res = str_res.replace(str(ro.variable), str(ro.res) )

        # print(lst_res_o)
        return str_res

    def resultado(self):
        return self.metodo

class RespuestaOriginal(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
    )
    variable = models.CharField(max_length=10)
    res = models.IntegerField()
    limite_inicial = models.IntegerField()
    limite_final = models.IntegerField()

    def __str__(self):
        return str(self.res)

class RespuestaAleatoria(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
    )
    marca = models.CharField(max_length=250)
    variable = models.CharField(max_length=10)
    res = models.IntegerField()


    def __str__(self):
        return self.pregunta.pregunta_txt
