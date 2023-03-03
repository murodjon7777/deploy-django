from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    text=models.TextField()
    # doc=models.ForeignKey(upload_to='docx/',blank=True,null=True)
    pdf=models.FileField(upload_to='pdf/',blank=True,null=True)
    pdfAll=models.FileField(upload_to='pdf/',blank=True,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    
    
    
    
    def __str__(self) -> str:
        return self.first_name