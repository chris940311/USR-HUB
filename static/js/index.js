document.addEventListener("DOMContentLoaded", () => {
  let count = 0;
  let details = document.querySelectorAll(".introduce");

  details.forEach((detail) => {
    if (count % 2) {
      detail.style.backgroundColor = "#cccccc";
    } else {
      detail.style.backgroundColor = "#ffffff";
    }
    detail.style.opacity = 0.8;
    count++;
  });
  // 定義觀察器的回調函數
  // 定義觀察器的回調函數
  // 定義觀察器的回調函數
  const callback = (entries, observer) => {
    entries.forEach((entry, index) => {
      const introduce = entry.target; // 取得 .introduce 元素
      const section = introduce.querySelector("section");
      const a = introduce.querySelector("a");

      if (entry.isIntersecting) {
        // 延遲觸發動畫
        setTimeout(() => {
          // 元素進入目標區域時執行的操作
          section.style.transform = "translateY(0px)";
          section.style.opacity = 1;

          section.addEventListener(
            "transitionend",
            () => {
              a.style.opacity = 1;
            },
            { once: true }
          );

          // 停止觀察該元素
          observer.unobserve(introduce);

          // 如果不是最後一個元素，則觀察下一個元素
          if (index < entries.length - 1) {
            observer.observe(entries[index + 1].target);
          }
        }, 500 * index); // 依序增加延遲時間
      } else {
        // 元素離開目標區域時執行的操作
        console.log("Element is now out of viewport:", introduce);
      }
    });
  };

  // 創建 IntersectionObserver 實例
  const observer = new IntersectionObserver(callback);

  // 對所有目標元素開始觀察
  details.forEach((detail, index) => {
    observer.observe(detail);
  });
});
