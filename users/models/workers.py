from django.db import models

class Worker(models.Model):
    user = models.ForeignKey('users.User', related_name='_user_worker', on_delete=models.CASCADE)
    store = models.ForeignKey('store.Store', on_delete=models.CASCADE)
    salary = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'worker'
        verbose_name = 'worker'
        verbose_name_plural = 'workers'

    def __str__(self) -> str:
        return self.user.get_identity()