from django.db import models
from django.contrib.auth.models import User
# suna comment
# suna comment

class brand(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    def __str__(self):
        return "{0}".format(self.name)


class events_type(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    vaule = models.CharField(max_length=30)


class events(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=40)
    id_type = models.ForeignKey(events_type, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __str__(self):
        return self.name


class country(models.Model):
    id= models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return "{0}".format(self.name)


class postavshik(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    addres = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class category(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class roles(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    vaule = models.IntegerField()
    def __str__(self):
        return self.name


class pesons(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    reg_data = models.DateField(auto_now_add=True)
    id_role = models.CharField(max_length=30)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    second_name = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=150, null=True)
    user_t = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_t")
    def __str__(self):
        return "{0}, {1}".format(self.id, self.first_name)


class product(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE)
    weight = models.IntegerField() # А если мы на развес огурчики продаем?
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    id_postavshik = models.ForeignKey(postavshik,on_delete=models.CASCADE)
    image = models.ImageField()
    about = models.TextField(default="Краткое описание отсутствует")
    html_about = models.CharField(max_length=50, default="")
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    is_popular = models.BooleanField()
    date_add = models.DateField(auto_now_add=True)
    def __str__(self):
        return "ID: {0}, NAME: {1}".format(self.id, self.name)



class storage(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    pr_count = models.ForeignKey(country, on_delete=models.CASCADE)
    date_bg = models.DateField()


class shift_type(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class payments_method(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    value = models.CharField(max_length=40)
    def __str__(self):
        return self.value


class staff_timetable(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    working_day_date = models.DateField()
    id_shift_type = models.ForeignKey(shift_type, on_delete=models.CASCADE)
    id_people = models.ForeignKey(pesons, on_delete=models.CASCADE)


class bonus_card(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    id_people = models.ForeignKey(pesons, on_delete=models.CASCADE)
    number = models.CharField(max_length=30)
    count_bonus = models.IntegerField()
    date_bg = models.DateTimeField(auto_now_add=True)


class sale(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    user = models.ForeignKey(pesons, related_name='user', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    payments_method = models.ForeignKey(payments_method, on_delete=models.CASCADE)
    id_staff = models.ForeignKey(pesons, related_name='id_staff', on_delete=models.CASCADE)


class sale_pos(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    id_sale = models.ForeignKey(sale, on_delete=models.CASCADE)
    count = models.IntegerField()
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # Create your models here.
