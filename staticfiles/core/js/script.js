document.addEventListener("DOMContentLoaded", function() {
    const openBtn = document.getElementById('openBtn');
    const closeBtn = document.getElementById('closeBtn');
    const menuContainer = document.getElementById('menuContainer');

    openBtn.addEventListener('click', function() {
        menuContainer.style.right = '0';
    });

    closeBtn.addEventListener('click', function() {
        menuContainer.style.right = '-250px';
    });

    // Exibe o menu por padrão em telas maiores
    if (window.innerWidth >= 768) {
        menuContainer.style.right = '0';
    }
});

