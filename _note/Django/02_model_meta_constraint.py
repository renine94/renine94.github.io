# Django App단과 DB단에 직접 데이터 넣을때도 에러 나도록 변경하는 meta 설정



class CategoryNameChoices(models.TextChoices):
    """ 카테고리 종류 """

    COSMETIC = "COSMETIC", "Cosmetic"
    FOOD = "FOOD", "Food"
    BOOK = "BOOK", "Book"


class Category(models.Model):
    category_name = models.CharField(choices=CategoryNameChoices.choices, max_length=250, null=True)
    something_price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_category_name_valid",
                check=models.Q(category_name__in=CategoryNameChoices.values),
            ),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_something_price_valid",
                check=models.Q(something_price__gte=0),
            )
        ]

    def __str__(self):
        return f"<Category {self.category_name} {self.something_price}>"