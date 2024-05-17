document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("nav a");
    const currentUrl = window.location.pathname;
    console.log(currentUrl);
    // 遍历所有导航链接，根据当前URL添加active-page类
    links.forEach(link => {
        console.log(link.getAttribute("href"));
        if (link.getAttribute("href") === currentUrl) {
            link.classList.add("active-page");
        }
    });
});
