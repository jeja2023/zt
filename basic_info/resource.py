from .models import BasicInfo,SwImage,JtImage,DtImage,Sfyj,Ypbg,Zhzg,Ypjl,Gz,Gxr,Backout
from import_export.resources import ModelResource

class BasicInfoResource(ModelResource):
    class Meta:
        model = BasicInfo
        fields = ('id','ztrybh','name','id_card','hjdz','ajlb','swdw','swsj')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','name','id_card','hjdz','ajlb','swdw','swsj')  # 指定导出字段的顺序

class BackoutResource(ModelResource):
    class Meta:
        model = Backout
        fields = ('id','ztrybh','name','id_card','ajlb','swdw','swsj','zhdw','cxsj')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','name','id_card','ajlb','swdw','swsj''zhdw','cxsj')  # 指定导出字段的顺序

class SwImageResource(ModelResource):
    class Meta:
        model = SwImage
        fields = ('id', 'ztrybh', 'swzp','cz')  # 指定要导入导出的字段
        export_order = ('id', 'ztrybh', 'swzp','cz')  # 指定导出字段的顺序

class JtImageResource(ModelResource):
    class Meta:
        model = JtImage
        fields = ('id', 'zrtybh','jtbd','cz')  # 指定要导入导出的字段
        export_order = ('id', 'zrtybh','jtbd','cz' )  # 指定导出字段的顺序

class DtImageResource(ModelResource):
    class Meta:
        model = DtImage
        fields = ('id', 'ztrybh', 'dtbd','cz')  # 指定要导入导出的字段
        export_order = ('id', 'ztrybh', 'dtbd','cz')  # 指定导出字段的顺序

class SfyjResource(ModelResource):
    class Meta:
        model = Sfyj
        fields = ('id','ztrybh','swsj','name','id_card','hdsj','sjly','yjxx','cz')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','swsj','name','id_card','hdsj','sjly','yjxx','cz')  # 指定导出字段的顺序

class YpbgResource(ModelResource):
    class Meta:
        model = Ypbg
        fields = ('id','ztrybh','swsj','name','id_card','swdw','sbsj','dqsj','zhdw','zhsj','cxsj','xsfw','fz','zg')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','swsj','name','id_card','swdw','sbsj','dqsj','zhdw','cxsj','zhsj','xsfw','fz','zg')  # 指定导出字段的顺序

class ZhzgResource(ModelResource):
    class Meta:
        model = Zhzg
        fields = ('id','ztrybh','swsj','name','id_card','swdw','zhdw','fz')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','swsj','name','id_card','swdw','zhdw','fz')  # 指定导出字段的顺序

class YpjlResource(ModelResource):
    class Meta:
        model = Ypjl
        fields = ('id','ztrybh','ypnr','yptp','ypr')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','ypnr','yptp','ypr')  # 指定导出字段的顺序

class GzResource(ModelResource):
    class Meta:
        model = Gz
        fields = ('id','ztrybh','gzr')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','gzr')  # 指定导出字段的顺序

class GxrResource(ModelResource):
    class Meta:
        model = Gxr
        fields = ('id','ztrybh','name','id_card','gxr_name','gxr_id','hzgx')  # 指定要导入导出的字段
        export_order = ('id','ztrybh','name','id_card','gxr_name','gxr_id','hzgx')  # 指定导出字段的顺序