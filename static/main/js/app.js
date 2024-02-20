// Slider
// Инициализация индексов для всех слайдеров
// Объединенный объект индексов для всех слайдеров
let slideIndexes = { 'slider': 1, 'image-slider': 1, 'video-slider': 1 };

// Универсальная функция для смены слайдов
function changeSlide(sliderClass, n) {
  let slides = document.querySelectorAll(`.${sliderClass} .slide`);
  if (!slides.length) return; // Выходим, если нет слайдов

  slideIndexes[sliderClass] += n;
  if (slideIndexes[sliderClass] > slides.length) { slideIndexes[sliderClass] = 1; }
  if (slideIndexes[sliderClass] < 1) { slideIndexes[sliderClass] = slides.length; }

  slides.forEach(slide => slide.style.display = "none");
  slides[slideIndexes[sliderClass] - 1].style.display = "flex"; // Или "block", в зависимости от нужного стиля
}

// Универсальная функция для отображения слайдов
function showSlides(sliderClass, n) {
  let slides = document.querySelectorAll(`.${sliderClass} .slide`);
  if (!slides.length) return; // Выходим, если нет слайдов

  slides.forEach(slide => slide.style.display = "none");
  slides[n - 1].style.display = "flex"; // Или "block", в зависимости от нужного стиля
}

// Обработчик загрузки документа для инициализации всех слайдеров
document.addEventListener('DOMContentLoaded', function() {
  // Инициализация всех слайдеров
  Object.keys(slideIndexes).forEach(sliderClass => {
    showSlides(sliderClass, slideIndexes[sliderClass]);
  });
});







// Dynamic content

document.addEventListener('DOMContentLoaded', () => {
  const navItems = document.querySelectorAll('.navigation-panel .cont');
  const contentContainer = document.querySelector('.container');

  // Функция для загрузки содержимого секции
  function loadSectionContent(sectionId) {
  // Путь к файлу зависит от вашей структуры проекта
  const url = `/${sectionId}/`; // Это должно соответствовать вашему URL из Django

  // AJAX запрос для загрузки содержимого
  fetch(url)
    .then(response => response.text())
    .then(html => contentContainer.innerHTML = html)
    .catch(error => console.error('Ошибка при загрузке содержимого:', error));
}

  // Обработчик клика для каждой контрольной точки навигации
  navItems.forEach(item => {
    item.addEventListener('click', (event) => {
      event.preventDefault();
      const sectionId = item.dataset.section;

      // Удаляем класс 'active' у всех элементов и назначаем новый активный класс
      navItems.forEach(nav => nav.classList.remove('active'));
      item.classList.add('active');

      // Загружаем содержимое выбранного раздела
      loadSectionContent(sectionId);
    });
  });

  // Активируем первый раздел CDR по умолчанию
  document.querySelector('.navigation-panel .cont[data-section="section1"]').click();
});


//







