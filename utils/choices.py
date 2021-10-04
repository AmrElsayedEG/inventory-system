# list of all choices
from django.db import models

# User Type Choices
class UserTypeChoices(models.IntegerChoices):
    ADMIN = 1, 'Admin'
    MANAGER = 2, 'Manager'
    STORE_KEEPER = 3, 'Store Keeper'
    REPRESENTATIVE = 4, 'Representative'

# Gender Choices
class GenderChoices(models.IntegerChoices):
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'

# Offer Status
class OutDeliveryStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    IN_PROGRESS = 'in_progress', 'In Progress'
    CANCELED = 'canceled', 'Canceled'
    DELIVERED = 'delivered', 'Delivered'

class OutProductType(models.TextChoices):
    BOXES = 'boxes', 'Boxes'
    ITEMS = 'items', 'Items'

class PaymentMethodType(models.TextChoices):
    CASH = 'cash', 'Cash'
    POSTPAID = 'postpaid', 'Postpaid'