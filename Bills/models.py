from django.db import models


# Create your models here.
# 创建记账本数据表
class bill(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, verbose_name="记账本id")
    time = models.DateTimeField(db_column='time', verbose_name="记账时间")
    amount = models.IntegerField(db_column="amount", verbose_name="金额(分)")
    memo = models.CharField(db_column="memo", max_length=100, verbose_name="备注")

    # 重写方法
    def __str__(self):
        return str(self.memo)

    class Meta:
        verbose_name = "记账表"
        managed = False
        db_table = 'bill'
