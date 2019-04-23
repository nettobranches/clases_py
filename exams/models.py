from django.db import models
# from django.utils import timezone

# import controllers.fisica

from controllers.solver import doMethod, doRandomMethod

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
        res = []

        for ro in lst_res_o:
            if(ro.res == "0"):
                value = ""
            else:
                value = ro.res
            str_res = str_res.replace(str(ro.variable), str(value) )

        res.append(str_res)
        res.append( doMethod(self.materia, self.unidad, self.metodo, lst_res_o, str_res) )
        return res

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
        res.append( doMethod(self.materia, self.unidad, self.metodo, lst_res_o, str_res) )
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
    res = models.CharField(max_length=10)
    generate_method = models.CharField(max_length=100)

    def __str__(self):
        return str(self.variable)+" = "+str(self.res)+" : "+self.pregunta.pregunta_txt

    def generate_res(self):
        return doRandomMethod(self.generate_method)


class RespuestaAleatoria(models.Model):
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
    )
    marca = models.CharField(max_length=250)
    variable = models.CharField(max_length=10)
    res =models.CharField(max_length=100)



    def __str__(self):
        return str(self.variable)+" = "+str(self.res)+" : "+self.pregunta.pregunta_txt
