// Slider

let slideIndex = 1;
showSlides(slideIndex);

function changeSlide(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("slide");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}



// popular forum list

document.addEventListener('DOMContentLoaded', function() {
  fetchPopularTopics();
});

function fetchPopularTopics() {
  // Здесь должен быть запрос к вашему API форума для получения популярных тем
  // Это пример кода, вам нужно будет использовать реальный URL и логику обработки ответа
  fetch('/api/popular-topics?period=week')
    .then(response => response.json())
    .then(data => {
      const topicsList = document.getElementById('popular-topics-list');
      topicsList.innerHTML = ''; // Очистить список, если там уже что-то есть
      data.forEach(topic => {
        const listItem = document.createElement('li');
        listItem.textContent = topic.title; // Предполагается, что у темы есть заголовок
        // Добавьте другие элементы в listItem, если нужно
        topicsList.appendChild(listItem);
      });
    })
    .catch(error => console.error('Ошибка при получении популярных тем:', error));
}


// Personal recommendations

document.addEventListener('DOMContentLoaded', function() {
  fetchPersonalRecommendations();
});

function fetchPersonalRecommendations() {
  // Пример функции запроса к API для получения рекомендаций
  // Замените '/api/recommendations' на реальный URL вашего API
  fetch('/api/recommendations')
    .then(response => response.json())
    .then(recommendations => {
      const container = document.querySelector('.recommendations-container');
      container.innerHTML = ''; // Очистить текущие рекомендации
      recommendations.forEach(rec => {
        const item = createRecommendationItem(rec);
        container.appendChild(item);
      });
    })
    .catch(error => console.error('Ошибка при получении рекомендаций:', error));
}

function createRecommendationItem(rec) {
  const item = document.createElement('div');
  item.className = 'recommendation-item';
  item.innerHTML = `
    <img src="${rec.image}" alt="${rec.title}">
    <h3>${rec.title}</h3>
    <p>${rec.description}</p>
  `;
  return item;
}


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

