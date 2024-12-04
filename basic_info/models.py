from datetime import timedelta
from django.db import models
from login.models import CustomUser


def swzp_image_upload_path(instance, filename):
    # 使用 instance.basic_info.ztrybh 来动态生成路径
    return f'image/sw_images/{instance.ztrybh}/{filename}'
def jtbd_image_upload_path(instance, filename):
    # 使用 instance.basic_info.ztrybh 来动态生成路径
    return f'image/jt_images/{instance.ztrybh}/{filename}'
def dtbd_image_upload_path(instance, filename):
    # 使用 instance.basic_info.ztrybh 来动态生成路径
    return f'image/dt_images/{instance.ztrybh}/{filename}'
def yp_image_upload_path(instance, filename):
    # 使用 instance.basic_info.ztrybh 来动态生成路径
    return f'image/yp_images/{instance.ztrybh}/{filename}'

class BasicInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    name = models.CharField(max_length=50, verbose_name="姓名",blank=True,null=True)
    id_card = models.CharField(max_length=50, verbose_name="身份证号码",blank=True,null=True)
    hjdz = models.CharField(max_length=100, verbose_name="户籍地址",blank=True,null=True)
    ajlb = models.CharField(max_length=50, verbose_name="案件类别",blank=True,null=True)
    jyaq = models.CharField(max_length=5000, verbose_name="简要案情",blank=True,null=True)
    swdw = models.CharField(max_length=50, verbose_name="上网单位",blank=True,null=True)
    swsj = models.DateTimeField(verbose_name="上网时间",blank=True,null=True)
    xxzjbh = models.CharField(max_length=50, verbose_name="信息主键编号", blank=True, null=True)
    zt = models.CharField(max_length=50, verbose_name="状态", default='在逃',blank=True,null=True,choices=[("在逃", "在逃"),("已抓获", "已抓获")])
    bssw = models.CharField( max_length=50,verbose_name="本市上网",blank=True,null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True,null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '在逃人员信息'
        verbose_name_plural = verbose_name
        indexes=[
            models.Index(fields=['ztrybh']),
        ]

    def save(self,*args, **kwargs):
        if self.swdw is None or not any(city in (self.swdw or '') for city in ["无锡市公安局", "江阴市公安局", "宜兴市公安局"]):
            self.bssw="否"
        else:
            self.bssw="是"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ztrybh}"

class Backout(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    name = models.CharField(max_length=50, verbose_name="姓名",blank=True,null=True)
    id_card = models.CharField(max_length=50, verbose_name="身份证号码",blank=True,null=True)
    ajlb = models.CharField(max_length=50, verbose_name="案件类别",blank=True,null=True)
    swdw = models.CharField(max_length=50, verbose_name="上网单位",blank=True,null=True)
    swsj = models.DateTimeField(verbose_name="上网时间",blank=True,null=True)
    zhdw = models.CharField(max_length=50, verbose_name="抓获单位",blank=True,null=True)
    cxsj = models.DateTimeField(verbose_name="撤销时间",blank=True,null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    class Meta:
        verbose_name = '在逃人员信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.ztrybh}"

class Ypjl(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    ypnr = models.TextField( verbose_name="研判记录",blank=True,null=True)
    yptp = models.ImageField(upload_to=yp_image_upload_path, verbose_name="研判记录图片", max_length=255,blank=True, null=True)
    ypr = models.CharField(max_length=50, verbose_name="研判人")
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = '研判记录'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"

class SwImage(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    swzp = models.ImageField(upload_to=swzp_image_upload_path, verbose_name="上网图片", max_length=255,blank=True,null=True)
    cz = models.CharField(max_length=50, verbose_name="处置", choices=[("本人","本人"),("非本人","非本人")],default="本人")
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '上网图片'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"

class JtImage(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    jtbd = models.ImageField(upload_to=jtbd_image_upload_path, verbose_name="静态比对图片", max_length=255,blank=True,null=True)
    cz = models.CharField(max_length=50, verbose_name="处置", blank=True,choices=[("排除","排除"),("已抓获","已抓获"),("确认","确认")],default="确认")
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '静态比对图片'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"

class DtImage(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    dtbd = models.ImageField(upload_to=dtbd_image_upload_path, verbose_name="动态比对图片", max_length=255,blank=True,null=True)
    cz = models.CharField(max_length=50, verbose_name="处置", blank=True,choices=[("排除","排除"),("已抓获","已抓获"),("确认","确认")],default="确认")
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '动态比对图片'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"


class Sfyj(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    swsj = models.DateField(verbose_name="上网日期", blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name="姓名", blank=True,null=True)
    id_card = models.CharField(max_length=20, verbose_name="身份证号码",blank=True,null=True)
    hdsj = models.DateTimeField(verbose_name="活动时间",blank=True, null=True)
    sjly = models.CharField(max_length=50, verbose_name="数据来源", blank=True,null=True)
    yjxx = models.CharField(max_length=5000, verbose_name="预警信息",blank=True,null=True)
    cz = models.CharField(max_length=50, verbose_name="处置",blank=True,null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '身份信息预警'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"

class Ypbg(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    name = models.CharField(max_length=50, verbose_name="姓名", blank=True,null=True)
    id_card = models.CharField(max_length=20, verbose_name="身份证号码",blank=True,null=True)
    swdw = models.CharField(max_length=50, verbose_name="上网单位", blank=True,null=True)
    swsj = models.DateTimeField(verbose_name="上网时间", blank=True, null=True)
    sbdw = models.CharField(max_length=50, verbose_name="上报单位", blank=True,null=True)
    sbsj = models.DateTimeField(verbose_name="上报时间",blank=True, null=True)
    dqsj = models.DateTimeField(verbose_name="到期时间",blank=True, null=True)
    zhdw = models.CharField(max_length=50, verbose_name="抓获单位", blank=True, null=True)
    zhsj = models.DateTimeField(verbose_name="抓获时间",blank=True, null=True)
    cxsj = models.DateTimeField(verbose_name="撤销时间", blank=True, null=True)
    xsfw = models.CharField(max_length=50, verbose_name="线索范围", blank=True,null=True)
    fz = models.CharField(max_length=50, verbose_name="分值", blank=True,null=True)
    zg = models.CharField(max_length=50, verbose_name="战果认定", blank=True,null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '研判报告'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def save(self, *args, **kwargs):
        if self.sbsj:
            self.dqsj = self.sbsj + timedelta(days=60)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ztrybh}"

class Zhzg(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    name = models.CharField(max_length=50, verbose_name="姓名", blank=True,null=True)
    id_card = models.CharField(max_length=20, verbose_name="身份证号码", blank=True,null=True)
    swdw = models.CharField(max_length=50, verbose_name="上网单位", blank=True,null=True)
    swsj = models.DateField(verbose_name="上网日期", blank=True, null=True)
    zhdw = models.CharField(max_length=50, verbose_name="抓获单位", blank=True,null=True)
    cxsj = models.DateTimeField(verbose_name="抓获时间", blank=True, null=True)
    fz = models.CharField(max_length=50, verbose_name="分值", blank=True,null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '抓获战果'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"

class Gz(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    gzr = models.CharField(max_length=50, verbose_name="关注人", blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = '关注'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]
        unique_together = ('ztrybh', 'gzr')

    def __str__(self):
        return f"{self.ztrybh}"

class Gxr(models.Model):
    id = models.AutoField(primary_key=True)
    ztrybh = models.CharField(max_length=50, verbose_name="在逃人员编号",db_index=True)
    name = models.CharField(max_length=50, verbose_name="姓名", blank=True,null=True)
    id_card = models.CharField(max_length=20, verbose_name="身份证号码",blank=True,null=True)
    gxr_name = models.CharField(max_length=50, verbose_name="关系人姓名", blank=True, null=True)
    gxr_id = models.CharField(max_length=18, verbose_name="关系人身份证号码",blank=True,null=True)
    hzgx = models.CharField(max_length=50, verbose_name="关系人与户主关系", blank=True,null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updated_by = models.CharField(max_length=50, verbose_name="更新人", blank=True, null=True)
    update_at =models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = '在逃关系人'
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['ztrybh']),
        ]

    def __str__(self):
        return f"{self.ztrybh}"