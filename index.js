document.addEventListener('DOMContentLoaded', function() {
 // 其他代码保持不变...
  
  // 趋势分析跳转逻辑
  const trendLinks = document.querySelectorAll('.bingfa-link');
  trendLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      // 跳转到趋势分析页面（替换为实际路径）
      window.location.href = 'bingfa.html';
      
      // 可选：添加加载动画（示例）
      const loading = document.createElement('div');
      loading.className = 'fixed inset-0 bg-black/50 flex items-center justify-center z-50';
      loading.innerHTML = `
        <div class="bg-white p-6 rounded-lg text-center">
          <div class="w-12 h-12 border-4 border-primary border-t-transparent rounded-full animate-spin mx-auto mb-4"></div>
          <p>正在加载趋势分析数据...</p >
        </div>
      `;
      document.body.appendChild(loading);
      
      // 模拟加载延迟（实际可移除）
      setTimeout(() => {
        document.body.removeChild(loading);
      }, 800);
    });
  });
});