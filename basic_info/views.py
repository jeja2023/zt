
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, Sum, IntegerField, F
from django.db.models.functions import Coalesce
from django.db import connection
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import YpbgForm, ZtQueryForm, YzQueryForm, BsQueryForm
from .models import BasicInfo,Backout,SwImage,JtImage,DtImage,Sfyj,Ypbg,Zhzg,Ypjl,Gxr,Gz
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, QueryDict
from django.views.decorators.http import require_http_methods
import json
import random
import plotly.graph_objs as go
from plotly.offline import plot


def execute_raw_query(sql, params=()):
    """执行原生SQL查询并返回结果"""
    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
@login_required
@csrf_exempt
def home(request):
    combined_results = zgtj_data()  # 获取数据
    chart_html = create_chart(combined_results)  # 创建图表
    today = timezone.now().date()
    objects = Ypbg.objects.filter(dqsj__date=today)
    reminders = []
    for obj in objects:
        if obj.dqsj:
            dqsj_local = timezone.make_aware(obj.dqsj.replace(tzinfo=None), timezone.get_current_timezone())
            if dqsj_local.date() == today:
                reminders.append(f" {obj.ztrybh} 的上报到期时间是今天！")

    # 限制提醒条数为最多5条
    reminders = reminders[:5]
    return render(request, "home.html", {'chart_html': chart_html,'reminders': reminders})

#@login_required
def get_page_obj(queryset, request, per_page=15):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

@login_required
def zt(request):
    objects = BasicInfo.objects.filter(zt="在逃").order_by('-create_at')
    page_obj = get_page_obj(objects, request)
    return render(request, "zt.html", {'page_obj': page_obj})

@login_required
def gz_cancel(request, pk):
    if request.method == "POST":
        attention_record = get_object_or_404(Gz, id=pk, gzr=request.user.username)
        attention_record.delete()
        return redirect('basic_info:attention')
    return redirect('basic_info:attention')

#@login_required
def cx(request):
    objects = Backout.objects.all().order_by('-create_at')
    page_obj = get_page_obj(objects, request)
    return render(request, "cx.html", {'page_obj': page_obj})

#@login_required
def yz(request):
    objects = BasicInfo.objects.filter(zt="已抓获").order_by('-create_at')
    page_obj = get_page_obj(objects, request)
    return render(request, "yz.html", {'page_obj': page_obj})

#@login_required
def bs(request):
    objects = BasicInfo.objects.filter(bssw="是").order_by('-create_at')
    page_obj = get_page_obj(objects, request)
    return render(request, "bs.html", {'page_obj': page_obj})

#@login_required
def gxr(request):
    sql="""
        select basic_info_gxr.*,basic_info_basicinfo.id_card
        from basic_info_gxr
        inner join basic_info_basicinfo
        on basic_info_gxr.id_card = basic_info_basicinfo.id_card
        where basic_info_basicinfo.zt='在逃'
        order by create_at desc
    """
    objects = execute_raw_query(sql)
    page_obj = get_page_obj(objects, request)
    return render(request, "gxr.html", {'page_obj': page_obj})

#@login_required
def ypjl(request):
    sql="""
        select basic_info_ypjl.*,basic_info_basicinfo.ztrybh
        from basic_info_ypjl
        inner join basic_info_basicinfo
        on basic_info_ypjl.ztrybh = basic_info_basicinfo.ztrybh
        where basic_info_basicinfo.zt='在逃'
        order by create_at desc
    """
    objects = execute_raw_query(sql)
    page_obj = get_page_obj(objects, request)
    return render(request, "ypjl.html", {'page_obj': page_obj})

#@login_required
def sfyj(request):
    sql="""
        select basic_info_sfyj.*,basic_info_basicinfo.ztrybh
        from basic_info_sfyj
        inner join basic_info_basicinfo
        on basic_info_sfyj.ztrybh = basic_info_basicinfo.ztrybh
        where basic_info_basicinfo.zt='在逃'
        order by create_at desc
    """
    objects = execute_raw_query(sql)
    page_obj = get_page_obj(objects, request)
    return render(request, "sfyj.html", {'page_obj': page_obj})

#@login_required
def sw(request):
    sql="""
        select basic_info_swimage.*,basic_info_basicinfo.ztrybh
        from basic_info_swimage
        inner join basic_info_basicinfo
        on basic_info_swimage.ztrybh = basic_info_basicinfo.ztrybh
        where basic_info_basicinfo.zt='在逃' and basic_info_swimage.cz='本人'
        order by create_at desc
    """
    objects = execute_raw_query(sql)
    page_obj = get_page_obj(objects, request)
    return render(request, 'sw.html', {'page_obj': page_obj})

#@login_required
def jt(request):
    sql="""
        select basic_info_jtimage.*,basic_info_basicinfo.ztrybh
        from basic_info_jtimage
        inner join basic_info_basicinfo
        on basic_info_jtimage.ztrybh = basic_info_basicinfo.ztrybh
        where basic_info_basicinfo.zt='在逃' and basic_info_jtimage.cz='确认'
        order by create_at desc
    """
    objects = execute_raw_query(sql)
    page_obj = get_page_obj(objects, request)
    return render(request, 'jt.html', {'page_obj': page_obj})

#@login_required
def dt(request):
    sql="""
        select basic_info_dtimage.*,basic_info_basicinfo.ztrybh
        from basic_info_dtimage
        inner join basic_info_basicinfo
        on basic_info_dtimage.ztrybh = basic_info_basicinfo.ztrybh
        where basic_info_basicinfo.zt='在逃' and basic_info_dtimage.cz='确认'
        order by create_at desc
    """
    objects = execute_raw_query(sql)
    page_obj = get_page_obj(objects, request)
    return render(request, 'dt.html', {'page_obj': page_obj})


def details(request, pk):
    ztrybh = get_object_or_404(BasicInfo, pk=pk)
    user = request.user.username
    attention_records = Gz.objects.filter(ztrybh=ztrybh)
    ztrybh.is_followed = any(user in record.gzr.split(',') for record in attention_records)
    return render(request, 'detail.html', {'ztrybh': ztrybh, 'pk': pk})

def add_attention(request, pk):
    if request.method == 'POST':
        user = request.user.username
        # 获取对应的 BasicInfo 对象
        ztrybh = get_object_or_404(BasicInfo, pk=pk)
        # 创建关注记录，并将 BasicInfo 对象的 ztrybh 字段写入 Gz 表
        Gz.objects.create(ztrybh=ztrybh, gzr=user)  # 使用 BasicInfo 对象的 ztrybh 字段
        return JsonResponse({'status': 'success', 'action': 'followed'})


def cancel_attention(request, pk):
    if request.method == 'POST':
        user = request.user.username
        # 获取对应 pk 的 ztrybh
        ztrybh = get_object_or_404(BasicInfo, pk=pk).ztrybh
        # 使用 ztrybh 和 gzr 两个字段来查询对应的 Gz 记录
        gz_record = get_object_or_404(Gz, ztrybh=ztrybh, gzr=user)
        # 删除该记录
        gz_record.delete()
        return JsonResponse({'status': 'success', 'action': 'unfollowed'})


def attention(request):
    user = request.user.username
    attention_records = Gz.objects.filter(gzr=user).order_by('-create_at')
    basic_info_dict = {info.ztrybh: info for info in BasicInfo.objects.all()}
    for record in attention_records:
        record.basic_info = basic_info_dict.get(record.ztrybh)
    page_obj = get_page_obj(attention_records, request)
    return render(request, "attention.html", {'page_obj': page_obj})

def basic_details(request, pk):
    ztrybh=get_object_or_404(BasicInfo,pk=pk)
    sw_images = SwImage.objects.filter(ztrybh=ztrybh, cz="本人").order_by('-create_at')
    objs=BasicInfo.objects.filter(ztrybh=ztrybh)
    return render(request, 'basic_detail.html', {'objs':objs, 'sw_images': sw_images, 'pk': pk})

#@login_required
def gxr_details(request, pk):
    ztrybh=get_object_or_404(BasicInfo,pk=pk)
    gxr_objs= Gxr.objects.filter(ztrybh=ztrybh).order_by('-create_at')
    page_obj = get_page_obj(gxr_objs, request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # 如果是AJAX请求，只返回部分HTML
        return render(request, 'gxr_detail.html', {'page_obj': page_obj})
    return render(request, 'detail.html', {'page_obj': page_obj})

#@login_required
def ypjl_details(request, pk):
    ztrybh=get_object_or_404(BasicInfo,pk=pk)
    ypjl_objs= Ypjl.objects.filter(ztrybh=ztrybh).order_by('-create_at')
    page_obj = get_page_obj(ypjl_objs, request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # 如果是AJAX请求，只返回部分HTML
        return render(request, 'ypjl_detail.html', {'page_obj': page_obj,'ztrybh': ztrybh})
    return render(request, 'detail.html', {'page_obj': page_obj})

@login_required
def add_ypjl(request, pk):
    ztrybh = get_object_or_404(BasicInfo, pk=pk)
    if request.method == 'POST':
        ypnr = request.POST.get('ypnr')
        yptp = request.FILES.get('yptp')
        # 这里可以添加其他字段
        Ypjl.objects.create(
            ztrybh=ztrybh,
            ypnr=ypnr,
            yptp=yptp,
            ypr=request.user,  # 记录当前用户
        )
        return redirect('basic_info:details', pk=pk)  # 重定向回详情页面

    return render(request, 'add_ypjl.html', {'pk': pk})

def view_ypjl(request, pk):
    record = get_object_or_404(Ypjl, pk=pk)  # 根据主键获取记录
    return render(request, 'view_ypjl.html', {'record': record})  # 渲染详情模板

#@login_required
def sfyj_details(request, pk):
    ztrybh=get_object_or_404(BasicInfo,pk=pk)
    sfyj_objs= Sfyj.objects.filter(ztrybh=ztrybh).order_by('-create_at')
    page_obj = get_page_obj(sfyj_objs, request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # 如果是AJAX请求，只返回部分HTML
        return render(request, 'sfyj_detail.html', {'page_obj': page_obj})
    return render(request, 'detail.html', {'page_obj': page_obj})

#@login_required
def sw_image_details(request, pk):
    ztrybh = get_object_or_404(BasicInfo,pk=pk)
    images = SwImage.objects.filter(ztrybh=ztrybh,cz="本人").order_by('-create_at')
    page_obj = get_page_obj(images, request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # 如果是AJAX请求，只返回部分HTML
        return render(request, 'sw_detail.html', {'page_obj': page_obj})
    return render(request, 'detail.html', {'page_obj': page_obj})

#@login_required
def jt_image_details(request, pk):
    ztrybh = get_object_or_404(BasicInfo,pk=pk)
    images = JtImage.objects.filter(ztrybh=ztrybh,cz="确认").order_by('-create_at')
    page_obj = get_page_obj(images, request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # 如果是AJAX请求，只返回部分HTML
        return render(request, 'jt_detail.html', {'page_obj': page_obj})
    return render(request, 'detail.html', {'page_obj': page_obj})

#@login_required
def dt_image_details(request, pk):
    ztrybh = get_object_or_404(BasicInfo,pk=pk)
    images = DtImage.objects.filter(ztrybh=ztrybh,cz="确认").order_by('-create_at')
    page_obj = get_page_obj(images, request)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # 如果是AJAX请求，只返回部分HTML
        return render(request, 'dt_detail.html', {'page_obj': page_obj})
    return render(request, 'detail.html', {'page_obj': page_obj})

#@login_required
def ypbg(request):
    objects = Ypbg.objects.all().order_by('-sbsj')
    page_obj = get_page_obj(objects, request)
    return render(request, "ypbg.html", {'page_obj': page_obj})

#@login_required
def ypzg(request):
    objects = Ypbg.objects.filter(zg="是").exclude(fz=0)
    page_obj = get_page_obj(objects, request)
    return render(request, "ypzg.html", {'page_obj': page_obj})

#@login_required
def zhzg(request):
    objects = Zhzg.objects.exclude(fz=0).order_by('-cxsj')
    page_obj = get_page_obj(objects, request)
    return render(request, "zhzg.html", {'page_obj': page_obj})

def zgtj_data():
    # 从 Ypbg 表中获取上报单位和研判战果总分
    ypzg_fz = Ypbg.objects.filter(Q(sbdw__icontains="无锡市公安局")|Q(sbdw__icontains="江阴市公安局")|Q(sbdw__icontains="宜兴市公安局"), zg="是").annotate(zgdw=F("sbdw")).values("zgdw").annotate(
        total_ypzg=Coalesce(Sum('fz', output_field=IntegerField()), 0)
    )
    # 从 Zhzg 表中获取抓获单位和抓获战果总分
    zhzg_fz = Zhzg.objects.annotate(zgdw=F("zhdw")).values("zgdw").annotate(
        total_zhzg=Coalesce(Sum('fz', output_field=IntegerField()), 0)
    )
    combined_results = {}

    # 添加研判战果总分
    for ypfz in ypzg_fz:
        unit = ypfz['zgdw']
        score = ypfz['total_ypzg']  # 确保使用正确的键
        combined_results[unit] = {'total_ypzg': score, 'total_zhzg': 0}

    # 添加抓获战果总分
    for zhfz in zhzg_fz:
        unit = zhfz['zgdw']
        score = zhfz['total_zhzg']  # 确保使用正确的键
        if unit in combined_results:
            combined_results[unit]['total_zhzg'] += score
        else:
            combined_results[unit] = {'total_ypzg': 0, 'total_zhzg': score}

    # 计算总分
    for unit, scores in combined_results.items():
        scores['total_score'] = scores['total_ypzg'] + scores['total_zhzg']

    return combined_results

def hsl_to_rgb(h, s, l):
    """将 HSL 转换为 RGB 并返回 rgba 格式"""
    s /= 100
    l /= 100
    c = (1 - abs(2 * l - 1)) * s  # 色度
    x = c * (1 - abs((h / 60) % 2 - 1))  # 主要色度
    m = l - c / 2  # 最小色度

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    r = (r + m) * 255
    g = (g + m) * 255
    b = (b + m) * 255

    return f"rgba({int(r)}, {int(g)}, {int(b)}, 0.7)"  # 使用 0.7 透明度

def generate_distinct_colors(n):
    """生成动态区分的颜色并转换为 rgba 格式"""
    colors = []
    for _ in range(n):
        h = random.randint(0, 360)  # 色相（0-360）
        s = random.uniform(0.6, 0.9)  # 饱和度（0.6-0.9）
        l = random.uniform(0.4, 0.6)  # 亮度（0.4-0.6）
        rgba_color = hsl_to_rgb(h, s * 100, l * 100)  # 转换为 rgba 格式
        colors.append(rgba_color)
    return colors

def create_chart(combined_results):
    # 准备图表数据
    sorted_data=sorted(combined_results.items(), key=lambda x: x[1]['total_score'], reverse=True)
    sorted_data=sorted_data[:8]
    categories=[key.replace('江苏省无锡市公安局','').replace('江苏省','') for key in [item[0] for item in sorted_data]]
    total_scores = [item[1]['total_score'] for item in sorted_data]

    # 动态生成柱子数量的颜色
    colors = generate_distinct_colors(len(categories))

    # 创建柱状图
    bar = go.Bar(
        x=categories,  # 设置 X 轴为战果单位
        y=total_scores,  # 设置 Y 轴为总分
        marker=dict(color=colors),  # 设置每根柱子的颜色
        text=total_scores,
    )

    layout = go.Layout(
        title={'text':"各分局追逃总分柱状图",
             'x':0.5,
        }, # 图表标题
        xaxis=dict(title={'text':"战果单位"}, tickfont=dict(size=10)),  # X 轴设置
        yaxis=dict(title="战果总分(单位：分)",dtick=100),  # Y 轴设置
        hovermode="closest",  # 设置悬浮显示
        width=800,  # 设置宽度
        height=250,  # 设置高度
        paper_bgcolor="rgba(0, 0, 0, 0)",
        plot_bgcolor="rgba(0, 0, 0, 0)",
        margin=dict(l=100,r=50,t=50,b=70),
        autosize=True,
    )

    # 生成图表的 HTML 和 JavaScript 内容
    chart_html = plot({
        'data': [bar],
        'layout': layout
    }, output_type='div',config={'displayModeBar': False, 'responsive': True})

    return chart_html

def zgtj(request):
    combined_results = zgtj_data()  # 获取数据
    objects = sorted([{'zgdw': unit, **data} for unit, data in combined_results.items()],key=lambda x: x['total_score'],reverse=True)
    page_obj = get_page_obj(objects, request)
    return render(request, "zgtj.html", {'page_obj': page_obj})

def check_due_date(date_to_check):
    """检查日期是否为今天"""
    if date_to_check:
        date_local = timezone.make_aware(date_to_check.replace(tzinfo=None), timezone.get_current_timezone())
        return date_local.date() == timezone.now().date()
    return False

def ypdb(request):
    today = timezone.now().date()  # 获取今天的日期
    objects = Ypbg.objects.all()

    reminders = []
    filtered_objects = []

    for obj in objects:
        if check_due_date(obj.dqsj):
            reminders.append(f"提醒: {obj.ztrybh} 的上报到期时间是今天！")
            filtered_objects.append(obj)

    # 限制提醒条数为最多5条
    reminders = reminders[:5]
    page_obj = get_page_obj(filtered_objects, request)

    return render(request, "ypdb.html", {
        'page_obj': page_obj,
        'reminders': reminders,
        'today': today
    })

#@login_required
@require_http_methods(["POST"])
def update_sw_cz(request):
    data = json.loads(request.body)
    image_id = data.get('id')
    action = data.get('action')

    try:
        if action == 'exclude':
            sw_obj=SwImage.objects.get(id=image_id)
            sw_obj.cz="2"
            sw_obj.save()
        return JsonResponse({'success': True})
    except SwImage.DoesNotExist:
        return JsonResponse({'success': False, 'error': '在逃人员不存在。'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

#@login_required
@require_http_methods(["POST"])
def update_jt_cz(request):
    data = json.loads(request.body)
    image_id = data.get('id')  # 使用 image_id 定位具体记录
    action = data.get('action')

    if not image_id or not action:
        return JsonResponse({'success': False, 'error': '缺少必要参数。'})

    try:
        # 定位目标记录
        jt_obj = JtImage.objects.get(id=image_id)
        ztrybh = jt_obj.ztrybh

        if action == 'exclude':
            # 仅更新当前记录状态为 "排除"
            jt_obj.cz = '排除'
            jt_obj.save()
        elif action == 'captured':
            # 更新所有 ztrybh 相同的记录为 "已抓获"
            JtImage.objects.filter(ztrybh=ztrybh).update(cz='已抓获')
            # 更新 BasicInfo 中对应的状态为 "已抓获"
            BasicInfo.objects.filter(ztrybh=ztrybh).update(zt='已抓获')
        else:
            return JsonResponse({'success': False, 'error': '无效的操作类型。'})

        return JsonResponse({'success': True})
    except JtImage.DoesNotExist:
        return JsonResponse({'success': False, 'error': '记录不存在。'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': f'未知错误: {str(e)}'})

#@login_required
@require_http_methods(["POST"])
def update_dt_cz(request):
    data = json.loads(request.body)
    image_id = data.get('id')  # 使用 image_id 定位具体记录
    action = data.get('action')

    if not image_id or not action:
        return JsonResponse({'success': False, 'error': '缺少必要参数。'})

    try:
        # 定位目标记录
        dt_obj = DtImage.objects.get(id=image_id)
        ztrybh = dt_obj.ztrybh

        if action == 'exclude':
            # 仅更新当前记录状态为 "排除"
            dt_obj.cz = '排除'
            dt_obj.save()
        elif action == 'captured':
            # 更新所有 ztrybh 相同的记录为 "已抓获"
            DtImage.objects.filter(ztrybh=ztrybh).update(cz='已抓获')
            # 更新 BasicInfo 中对应的状态为 "已抓获"
            BasicInfo.objects.filter(ztrybh=ztrybh).update(zt='已抓获')
        else:
            return JsonResponse({'success': False, 'error': '无效的操作类型。'})

        return JsonResponse({'success': True})
    except DtImage.DoesNotExist:
        return JsonResponse({'success': False, 'error': '记录不存在。'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': f'未知错误: {str(e)}'})

#@login_required
@require_http_methods(['POST'])
def update_basic_zt(request):
    data = json.loads(request.body)
    ztrybh = data.get('ztrybh')

    try:
        sfyj_objects = Sfyj.objects.filter(ztrybh=ztrybh)
        for sfyj_obj in sfyj_objects:
            sfyj_obj.cz= '已抓获'
            sfyj_obj.save()

        basic_info_objs = BasicInfo.objects.filter(ztrybh=ztrybh)
        for basic_info_obj in basic_info_objs:
            basic_info_obj.zt = '已抓获'
            basic_info_obj.save()

        return JsonResponse({'success': True, 'disposition': '已抓获'})
    except Sfyj.DoesNotExist:
        return JsonResponse({'success': False, 'error': '在逃人员不存在。'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

#@login_required
def add_ypbg(request):
    if request.method == 'POST':
        form = YpbgForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('basic_info:ypbg')
    else:
        form = YpbgForm()
    return render(request, 'add_ypbg.html', {'form': form})

#@login_required
def zt_filter(request):
    form = ZtQueryForm(request.GET or None)
    results = BasicInfo.objects.filter(zt="在逃")

    if form.is_valid():
        ztrybh = form.cleaned_data.get('ztrybh')
        name = form.cleaned_data.get('name')
        id_card = form.cleaned_data.get('id_card')
        ajlb = form.cleaned_data.get('ajlb')
        swdw = form.cleaned_data.get('swdw')
        swsj = form.cleaned_data.get('swsj')

        filters = Q()
        if ztrybh:
            filters &= Q(ztrybh__icontains=ztrybh)
        if name:
            filters &= Q(name__icontains=name)
        if id_card:
            filters &= Q(id_card__icontains=id_card)
        if ajlb:
            filters &= Q(ajlb__icontains=ajlb)
        if swdw:
            filters &= Q(swdw__icontains=swdw)
        if swsj:
            try:
                if len(swsj) == 4:  # 只输入年份
                    year = int(swsj)
                    filters &= Q(swsj__year=year)
                elif len(swsj) == 7:  # 输入年份和月份
                    year, month = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month)
                elif len(swsj) == 10:  # 输入年份和月份和日期
                    year, month, day = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month, swsj__day=day)
            except ValueError:
                pass  # 处理无效输入
        results = results.filter(filters).order_by('id')
    query_dict = request.GET.copy()
    if 'page' in query_dict:
        del query_dict['page']
    query_params=query_dict.urlencode()
    paginator = Paginator(results, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'zt.html', {'form': form, 'page_obj': page_obj, 'query_params': query_params})

#@login_required
def yz_filter(request):
    form = YzQueryForm(request.GET or None)
    results = BasicInfo.objects.filter(zt="已抓获")

    if form.is_valid():
        ztrybh = form.cleaned_data.get('ztrybh')
        name = form.cleaned_data.get('name')
        id_card = form.cleaned_data.get('id_card')
        ajlb = form.cleaned_data.get('ajlb')
        swdw = form.cleaned_data.get('swdw')
        swsj = form.cleaned_data.get('swsj')

        filters = Q()
        if ztrybh:
            filters &= Q(ztrybh__icontains=ztrybh)
        if name:
            filters &= Q(name__icontains=name)
        if id_card:
            filters &= Q(id_card__icontains=id_card)
        if ajlb:
            filters &= Q(ajlb__icontains=ajlb)
        if swdw:
            filters &= Q(swdw__icontains=swdw)
        if swsj:
            try:
                if len(swsj) == 4:  # 只输入年份
                    year = int(swsj)
                    filters &= Q(swsj__year=year)
                elif len(swsj) == 7:  # 输入年份和月份
                    year, month = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month)
                elif len(swsj) == 10:  # 输入年份和月份和日期
                    year, month, day = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month, swsj__day=day)
            except ValueError:
                pass  # 处理无效输入

        results = results.filter(filters).order_by('id')
    query_dict = request.GET.copy()
    if 'page' in query_dict:
        del query_dict['page']
    query_params=query_dict.urlencode()
    paginator = Paginator(results, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'yz.html', {'form': form, 'page_obj': page_obj, 'query_params': query_params})

#@login_required
def bs_filter(request):
    form = BsQueryForm(request.GET or None)
    results = BasicInfo.objects.filter(bssw="是")

    if form.is_valid():
        ztrybh = form.cleaned_data.get('ztrybh')
        name = form.cleaned_data.get('name')
        id_card = form.cleaned_data.get('id_card')
        ajlb = form.cleaned_data.get('ajlb')
        swdw = form.cleaned_data.get('swdw')
        swsj = form.cleaned_data.get('swsj')

        filters = Q()
        if ztrybh:
            filters &= Q(ztrybh__icontains=ztrybh)
        if name:
            filters &= Q(name__icontains=name)
        if id_card:
            filters &= Q(id_card__icontains=id_card)
        if ajlb:
            filters &= Q(ajlb__icontains=ajlb)
        if swdw:
            filters &= Q(swdw__icontains=swdw)
        if swsj:
            try:
                if len(swsj) == 4:  # 只输入年份
                    year = int(swsj)
                    filters &= Q(swsj__year=year)
                elif len(swsj) == 7:  # 输入年份和月份
                    year, month = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month)
                elif len(swsj) == 10:  # 输入年份和月份和日期
                    year, month, day = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month, swsj__day=day)
            except ValueError:
                pass  # 处理无效输入

        results = results.filter(filters).order_by('id')
    query_dict = request.GET.copy()
    if 'page' in query_dict:
        del query_dict['page']
    query_params=query_dict.urlencode()
    paginator = Paginator(results, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bs.html', {'form': form, 'page_obj': page_obj, 'query_params': query_params})

def cx_filter(request):
    form = ZtQueryForm(request.GET or None)
    results = Backout.objects.all()

    if form.is_valid():
        ztrybh = form.cleaned_data.get('ztrybh')
        name = form.cleaned_data.get('name')
        id_card = form.cleaned_data.get('id_card')
        ajlb = form.cleaned_data.get('ajlb')
        swdw = form.cleaned_data.get('swdw')
        swsj = form.cleaned_data.get('swsj')

        filters = Q()
        if ztrybh:
            filters &= Q(ztrybh__icontains=ztrybh)
        if name:
            filters &= Q(name__icontains=name)
        if id_card:
            filters &= Q(id_card__icontains=id_card)
        if ajlb:
            filters &= Q(ajlb__icontains=ajlb)
        if swdw:
            filters &= Q(swdw__icontains=swdw)
        if swsj:
            try:
                if len(swsj) == 4:  # 只输入年份
                    year = int(swsj)
                    filters &= Q(swsj__year=year)
                elif len(swsj) == 7:  # 输入年份和月份
                    year, month = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month)
                elif len(swsj) == 10:  # 输入年份和月份和日期
                    year, month, day = map(int, swsj.split('-'))
                    filters &= Q(swsj__year=year, swsj__month=month, swsj__day=day)
            except ValueError:
                pass  # 处理无效输入

        results = results.filter(filters).order_by('id')
    query_dict = request.GET.copy()
    if 'page' in query_dict:
        del query_dict['page']
    query_params=query_dict.urlencode()
    paginator = Paginator(results, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cx.html', {'form': form, 'page_obj': page_obj, 'query_params': query_params})

