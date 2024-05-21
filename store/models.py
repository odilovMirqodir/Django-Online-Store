from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Kategoriya nomi")
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               verbose_name="Kategoriya",
                               related_name='subcategories')

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def get_image(self):
        if self.image:
            return self.image
        else:
            return "https://img.freepik.com/premium-vector/photo-coming-soon_77760-116.jpg"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Kategoriya pk={self.pk}, title={self.title}"

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    price = models.FloatField(verbose_name="Narxi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Saytga qo'yilgan vaqti")
    quantity = models.IntegerField(default=0, verbose_name="Ombordagi soni")
    description = models.TextField(default="bu yerda tez orada ma'lumot bo'ladi",
                                   verbose_name="Mahsulot haqida ma'lumot")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name="Kategoriya",
                                 related_name='products')
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=30, verbose_name="mm dagi o'lchami")
    color = models.CharField(max_length=30, default="Kumush", verbose_name="Rangi/Materiali")

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.first().image.url
            except:
                return "https://img.freepik.com/premium-vector/photo-coming-soon_77760-116.jpg"
        else:
            return "https://img.freepik.com/premium-vector/photo-coming-soon_77760-116.jpg"

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Mahsulot pk={self.pk}, title={self.title}"

    class Meta:
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'


class Gallery(models.Model):
    image = models.ImageField(upload_to='products/', verbose_name="Rasm")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Rasm'
        verbose_name_plural = 'Mahsulotlar galereyasi'


class Review(models.Model):
    text = models.TextField(verbose_name='Izoh matni')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"


class FavoriteProducts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "Tanlangan Mahsulot"
        verbose_name_plural = "Tanlangan mahsulotlar"


class Mail(models.Model):
    mail = models.EmailField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Pochta'
        verbose_name_plural = 'Pochtalar Adresi'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255, default='', verbose_name="Foydalanuvchi ismi")
    last_name = models.CharField(max_length=255, default='', verbose_name='Xaridor familyasi')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Xaridor"
        verbose_name_plural = 'Xaridorlar'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    shipping = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pk) + ' '

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'

    @property
    def get_cart_total_price(self):
        order_product = self.orderproduct_set.all()
        total_price = sum([product.get_total_price for product in order_product])
        return total_price

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        total_quantity = sum([product.quantity for product in order_products])
        return total_quantity


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    addet_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Buyurtma qilingan Mahsulot'
        verbose_name_plural = 'Buyurtma qilingan Mahsulotlar'

    @property
    def get_total_price(self):
        if self.product is not None:
            total_price = self.product.price * self.quantity
            return total_price
        return 0


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name="Shaharlar")
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Yetkazib berish joyi'
        verbose_name_plural = 'Yetkazib beriladigan joylar'


class City(models.Model):
    city_name = models.CharField(max_length=255, verbose_name='SHaharlar nomi')

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = 'Shaharlar'
