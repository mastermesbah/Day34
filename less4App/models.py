from django.db import models

from datetime import datetime

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Employee Name", max_length=100)
    email = models.EmailField("Email Address", max_length=100)
    # dob = models.DateTimeField("Date of Birth",default=datetime.now, blank=True,help_text="Format: yyyy/mm/dd")
    dob = models.DateTimeField("Date of Birth",help_text="Format: yyyy/mm/dd")
    salary = models.FloatField("Monthly Salary")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "employees"
