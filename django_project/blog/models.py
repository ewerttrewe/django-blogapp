from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	#jezeli damy DateTimeField(auto_now=True) to za kazdym razem kiedy zostanie wykonana zmiana czas dodania postu ulegnie zmianie do aktualnej daty
	#jezeli damy DateTimeField(auto_now_add=True) to wtedy zostanei zapamietana tylko data podczas ktorej zostal stworzony post a kazda zmiana nie bedzie mozliwa
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__ (self):
		return self.title
	
	""" 
	zeby moc w jakis sposob powiedziec browserowi ze chcemy konkretny post
	mozemy uzyc reverse. Rozni sie tym od redirecta ze redirect przerzuca nas
	do specjalnie wyznaczonego routa, natomiast reverse
	zwroci cala sciezke URL jako string do tego routa i dlatego chcemy reverse
	bo korzystamy z klasy i ona zrobi to za nas i sama nas zredirectuje	
	"""
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})



