from django.contrib import admin
from .models import BasicInfo, SwImage, JtImage, DtImage, Sfyj, Ypbg, Zhzg,Ypjl,Gz,Gxr
from .resource import BasicInfoResource,SwImageResource, JtImageResource, DtImageResource, SfyjResource, YpbgResource, ZhzgResource, YpjlResource, GzResource,GxrResource,BackoutResource
from import_export.admin import ImportExportModelAdmin



@admin.register(BasicInfo)
class BasicInfoAdmin(ImportExportModelAdmin):
    resource_class = BasicInfoResource
    list_display = ('id','ztrybh','name','id_card','hjdz','ajlb','swdw','swsj','zt','bssw','create_at','updated_by','update_at')
    search_fields = ('ztrybh','name','id_card','ajlb','swdw','swsj','zt','bssw','create_at','updated_by','update_at')
    list_filter = ('ztrybh','name','id_card','ajlb','swdw','swsj','zt','bssw','create_at','updated_by','update_at')
    ordering = ('update_at',)

class BackoutAdmin(ImportExportModelAdmin):
    resource_class = BackoutResource
    list_display = ('id','ztrybh','name','id_card','ajlb','swdw','swsj','zhdw','cxsj','create_at')
    search_fields = ('ztrybh','name','id_card','ajlb','swdw','swsj','zhdw','cxsj','create_at')
    list_filter = ('ztrybh','name','id_card','ajlb','swdw','swsj','zhdw','cxsj','create_at')
    ordering = ('update_at',)

@admin.register(SwImage)
class SwImageAdmin(ImportExportModelAdmin):
    resource_class = SwImageResource
    list_display = ('id','ztrybh', 'swzp','cz','create_at','updated_by','update_at')
    search_fields = ('ztrybh', 'swzp','cz','create_at','updated_by','update_at')
    list_filter = ('ztrybh', 'swzp','cz','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(JtImage)
class JtImageAdmin(ImportExportModelAdmin):
    resource_class = JtImageResource
    list_display = ('id','ztrybh', 'jtbd','cz','create_at','updated_by','update_at')
    search_fields = ('ztrybh', 'cz','create_at','updated_by','update_at')
    list_filter = ('ztrybh', 'cz','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(DtImage)
class DtImageAdmin(ImportExportModelAdmin):
    resource_class = DtImageResource
    list_display = ('id','ztrybh', 'dtbd','cz','create_at','updated_by','update_at')
    search_fields = ('ztrybh', 'cz','create_at','updated_by','update_at')
    list_filter = ('ztrybh', 'cz','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(Sfyj)
class SfyjAdmin(ImportExportModelAdmin):
    resource_class = SfyjResource
    list_display = ('id','swsj','ztrybh','name','id_card','hdsj','sjly','yjxx','cz','create_at','updated_by','update_at')
    search_fields = ('swsj','ztrybh','name','id_card','hdsj','sjly','cz','create_at','updated_by','update_at')
    list_filter = ('swsj','ztrybh','name','id_card','hdsj','sjly','cz','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(Ypbg)
class YpbgAdmin(ImportExportModelAdmin):
    resource_class = YpbgResource
    list_display = ('id','ztrybh','swsj','name','id_card','swdw','sbsj','dqsj','zhdw','zhsj','cxsj','xsfw','fz','zg','create_at','updated_by','update_at')
    search_fields = ('ztrybh','swsj','name','id_card','swdw','sbsj','dqsj','zhdw','zhsj','cxsj','xsfw','fz','zg','create_at','updated_by','update_at')
    list_filter = ('ztrybh','swsj','name','id_card','swdw','sbsj','dqsj','zhdw','zhsj','cxsj','xsfw','fz','zg','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(Zhzg)
class ZhzgAdmin(ImportExportModelAdmin):
    resource_class = ZhzgResource
    list_display = ('id','ztrybh','swsj','name','id_card','swdw','zhdw','fz','create_at','updated_by','update_at')
    search_fields = ('ztrybh','swsj','name','id_card','swdw','zhdw','fz','create_at','updated_by','update_at')
    list_filter = ('ztrybh','swsj','name','id_card','swdw','zhdw','fz','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(Ypjl)
class YpjlAdmin(ImportExportModelAdmin):
    resource_class = YpjlResource
    list_display = ('id','ztrybh','ypnr','ypr','yptp','create_at','updated_by','update_at')
    search_fields = ('ztrybh','ypr','create_at','updated_by','update_at')
    list_filter = ('ztrybh','ypr','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(Gz)
class GzAdmin(ImportExportModelAdmin):
    resource_class = GzResource
    list_display = ('id','ztrybh','gzr','create_at','updated_by','update_at')
    search_fields = ('ztrybh','gzr','create_at','updated_by','update_at')
    list_filter = ('ztrybh','gzr','create_at','updated_by','update_at')
    ordering = ('-update_at',)

@admin.register(Gxr)
class GxrAdmin(ImportExportModelAdmin):
    resource_class = GxrResource
    list_display = ( 'id','ztrybh','name','id_card','gxr_name','gxr_id','hzgx','create_at','updated_by','update_at')
    search_fields = ('ztrybh','name','id_card','gxr_name','gxr_id','hzgx','create_at','updated_by','update_at')
    list_filter = ('ztrybh','name','id_card','gxr_name','gxr_id','hzgx','create_at','updated_by','update_at')
    ordering = ('-update_at',)