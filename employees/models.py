from django.db import models


# <!--
#       •	Таблица, включающая следующие поля и элементы соответственно:
#     o	<Поле без имени> / checkbox (указывает, выбрана ли текущая строка таблицы);
#     o	номер сотрудника / гиперссылка с текстом номера сотрудника;
#     o	имя сотрудника / соответствующий текст;
#     o	должность сотрудника / соответствующий текст;
#     o	дата принятия на работу / соответствующий текст;
#     o	департамент / соответствующий текст;
#     o	“Удалить” / гиперссылка для удаления сотрудников.
#     Заполнить таблицу произвольными данными о сотрудниках (не менее 10 позиций).-->
from django.urls import reverse


class EmployeeModel(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name = "Имя")
    post = models.CharField(max_length=100,
                            verbose_name = "Должность")
    date_of_hiring = models.DateField(verbose_name = "Дата трудоустройства")
    department = models.CharField(max_length=100,
                            verbose_name = "Отдел")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = 'Сорудники'


