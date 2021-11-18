class DaysCalendar(models.model):
    day = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Day of the week must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Meals(models.model):
    meal = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Meal name must be greater than 1 character")]
    )
    dairyf = models.PositiveIntegerField()
    glutenf = models.PositiveIntegerField()
    nutf = models.PositiveIntegerField()
    soyf = models.PositiveIntegerField()
    scheduled = models.ForeignKey('DaysCalendar', on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.nickname
