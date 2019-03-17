from django.db import models
# from django.utils import timezone

# import controllers.fisica

from controllers.solver import doMethod

class Pregunta(models.Model):
    pregunta_txt = models.CharField(max_length=400)
    materia = models.CharField(max_length=200)
    metodo = models.CharField(max_length=200)
    unidad = models.CharField(max_length=1)

    def __str__(self):
        return self.pregunta_txt

    def getOriginal(self):
        lst_res_o = self.respuestaoriginal_set.all()
        str_res = self.pregunta_txt

        for ro in lst_res_o:
            str_res = str_res.replace(str(ro.variable), str(ro.res) )

        # print(lst_res_o)
        return str_res

    def getRandom(self, timestamp):
        # print(self)
        res = []
        lst_res_o = self.respuestaaleatoria_set.filter(marca = timestamp)
        # print("res rand", lst_res_o)
        str_res = self.pregunta_txt

        for ro in lst_res_o:
            str_res = str_res.replace(str(ro.variable), str(ro.res) )
            # print(getMethod(self.metodo))
        # print(lst_res_o)
        res.append(str_res)
        res.append( doMethod(self.materia, self.unidad, self.metodo, lst_res_o) )
        return res

    def resultado(self):
        return 0
        # do_method(self.metodo)

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
        return str(self.variable)+" = "+str(self.res)+" : "+self.pregunta.pregunta_txt


class RespuestaAleatoria(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
    )
    marca = models.CharField(max_length=250)
    variable = models.CharField(max_length=10)
    res = models.IntegerField()


    def __str__(self):
        return str(self.variable)+" = "+str(self.res)+" : "+self.pregunta.pregunta_txt
