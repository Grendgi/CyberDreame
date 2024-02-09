document.querySelectorAll('.category-list a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const href = this.getAttribute('href');
    const offsetTop = document.querySelector(href).offsetTop;

    window.scrollTo({
      top: offsetTop - 70, // Высота вашей фиксированной шапки
      behavior: 'smooth'
    });
  });
});
