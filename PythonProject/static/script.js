// static/js/script.js
// 通用交互逻辑
document.addEventListener('DOMContentLoaded', function() {
    // 页面切换逻辑
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            window.location.href = this.href;
        });
    });

    // 注册弹窗逻辑（保持之前的功能）
});
// static/js/script.js 新增下载跟踪
document.querySelectorAll('.download-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        // 可以在此处添加下载统计逻辑
        console.log('下载文件:', this.href);
    });
});