

// 按钮跳转事件处理
document.getElementById('logout-btn').addEventListener('click', function () {
    // 确认退出操作
    if (confirm('您确定要退出吗？')) {
        // 发送退出请求，可以是重定向到登出视图的 URL
        window.location.href = '/logout/'; // 替换为你的登出 URL
    }
});

document.getElementById('btn-zt').addEventListener('click', function () {
    window.open('/info/zt/', '_blank');
});

document.getElementById('btn-yz').addEventListener('click', function () {
    window.open('/info/yz/', '_blank');
});

document.getElementById('btn-bs').addEventListener('click', function () {
    window.open('/info/bs/', '_blank');
});

document.getElementById('btn-cx').addEventListener('click', function () {
    window.open('/info/cx/', '_blank');
});

document.getElementById('btn-attention').addEventListener('click', function () {
    window.open('/info/attention/', '_blank');
});

document.getElementById('btn-jt').addEventListener('click', function () {
    window.open('/info/jt/', '_blank');
});

document.getElementById('btn-dt').addEventListener('click', function () {
    window.open('/info/dt/', '_blank');
});

document.getElementById('btn-tj').addEventListener('click', function () {
    window.open('/info/ypbg/', '_blank');
});

document.getElementById('btn-db').addEventListener('click', function () {
    window.open('/info/ypdb/', '_blank');
});

document.getElementById('btn-yjxx').addEventListener('click', function () {
    window.open('/info/sfyj/', '_blank');
});

document.getElementById('btn-gxr').addEventListener('click', function () {
    window.open('/info/gxr/', '_blank');
});

document.getElementById('btn-ypzg').addEventListener('click', function () {
    window.open('/info/ypzg/', '_blank');
});

document.getElementById('btn-zhzg').addEventListener('click', function () {
    window.open('/info/zhzg/', '_blank');
});

document.getElementById('btn-zgtj').addEventListener('click', function () {
    window.open('/info/zgtj/', '_blank');
});
