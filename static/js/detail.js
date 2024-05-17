document.addEventListener("DOMContentLoaded", function() {
    // 获取所有侧边栏导航链接
    const links = document.querySelectorAll(".fixed-location a");

    // 为每个链接添加点击事件监听器
    for (const link of links) {
        link.addEventListener("click", function(e) {
            // 阻止默认的链接跳转行为
            e.preventDefault();
            
            // 获取目标元素的ID
            const targetId = this.getAttribute("href").substring(1);
            // 根据ID获取目标元素
            const targetElement = document.getElementById(targetId);

            // 如果目标元素存在，执行平滑滚动
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: "smooth"
                });
            }
        });
    }
});