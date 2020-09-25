from django.db import models


class brand(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()


class events_type(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    vaule = models.CharField(max_length=30)


class events(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=40)
    id_type = models.ForeignKey(events_type, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class country(models.Model):
    id= models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)


class postavshik(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    addres = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)


class category(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)


class roles(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    vaule = models.IntegerField()


class pesons(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    Login = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    reg_data = models.DateField()
    id_role = models.CharField(max_length=30)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    second_name = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=150, null=True)


class product(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    cat_id = models.ForeignKey(category, on_delete=models.CASCADE)
    weight = models.IntegerField() # А если мы на развес огурчики продаем?
    id_country = models.ForeignKey(country, on_delete=models.CASCADE)
    id_postavshik = models.ForeignKey(postavshik,on_delete=models.CASCADE)
    id_events = models.ForeignKey(events, on_delete=models.CASCADE) # Откуда? что это?
    image = models.ImageField()
    about = models.TextField(default="Краткое описание отсутствует")
    html_about = models.CharField(max_length=50, default="")
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)


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
    date_bg = models.DateTimeField()


class sale(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    user = models.ForeignKey(pesons, related_name='user', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField()
    payments_method = models.ForeignKey(payments_method, on_delete=models.CASCADE)
    id_staff = models.ForeignKey(pesons, related_name='id_staff', on_delete=models.CASCADE)


class sale_pos(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    id_sale = models.ForeignKey(sale, on_delete=models.CASCADE)
    count = models.IntegerField()
    id_product = models.ForeignKey(product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    # Create your models here.
