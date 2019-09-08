from django.db import models
# from django.utils import timezone

# import controllers.fisica

from controllers.solver import doMethod, doRandomMethod, replaceVars, replaceVars2

class Materia(models.Model):
    nombre = models.CharField(max_length=20)
    alias = models.CharField(max_length=20)
    grupos = models.CharField(max_length=20, default="")
    def __str__(self):
        return self.nombre+" "+self.grupos

class Unidad(models.Model):
    numero = models.CharField(max_length=1)
    alias = models.CharField(max_length=5, default="")
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.numero+" "+self.materia.nombre

class Pregunta(models.Model):
    pregunta_txt = models.CharField(max_length=400)
    unidad = models.ForeignKey(
        Unidad,
        on_delete=models.CASCADE,
    )
    metodo = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200, default="", blank="true")

    def __str__(self):
        return self.pregunta_txt

    def getOriginal(self):
        lst_res_o = self.respuestaoriginal_set.all()
        str_res = self.pregunta_txt
        materia = self.unidad.materia.nombre
        res = []

        for ro in lst_res_o:
            str_res = replaceVars(materia, str_res, ro )

        res.append(str_res)
        res.append( doMethod(materia, self.unidad, self.metodo, lst_res_o, str_res) )
        return res

    def getRandom(self, timestamp):
        # print(self)
        res = []
        lst_res_o = self.respuestaaleatoria_set.filter(marca = timestamp)
        materia = self.unidad.materia.nombre
        # print("res rand", lst_res_o)
        str_res = self.pregunta_txt

        for ro in lst_res_o:
            str_res = replaceVars2(materia, str_res, ro )
            # print(getMethod(self.metodo))
        # print(lst_res_o)
        res.append(str_res)
        res.append( doMethod(materia, self.unidad, self.metodo, lst_res_o, str_res) )
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
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return str(self.variable)+" = "+str(self.res)+" : "+self.pregunta.pregunta_txt+"  "+self.generate_method

    def generate_res(self):
        res = doRandomMethod(self.generate_method)
        if(self.mostrar == False and res == "1" or res == "0" ):
            res = ""
        return res


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

class RespuestaOrden(models.Model):
    timestamp = models.CharField(max_length=250)
    orden = models.IntegerField()
    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.orden)+" = "+str(self.pregunta.pregunta_txt)+" ( "+self.timestamp+")"

