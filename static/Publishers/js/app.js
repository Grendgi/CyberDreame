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


//Slider

// let slideIndexes = { 'image-slider': 1, 'video-slider': 1 };
//
// function showSlides(sliderClass, n) {
//   let slides = document.querySelectorAll(`.${sliderClass} .slide`);
//   if (n > slides.length) { slideIndexes[sliderClass] = 1; }
//   if (n < 1) { slideIndexes[sliderClass] = slides.length; }
//   slides.forEach(slide => slide.style.display = "none");
//   slides[slideIndexes[sliderClass] - 1].style.display = "flex";
// }
//
// function changeImageSlide(n) {
//   showSlides('image-slider', slideIndexes['image-slider'] += n);
// }
//
// function changeVideoSlide(n) {
//   showSlides('video-slider', slideIndexes['video-slider'] += n);
// }
//
// document.addEventListener('DOMContentLoaded', function() {
//   showSlides('image-slider', slideIndexes['image-slider']);
//   showSlides('video-slider', slideIndexes['video-slider']);
// });


//

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.page-create-news form');
    const submitButton = form.querySelector('button[type="submit"]');

    submitButton.addEventListener('click', function(e) {
        e.preventDefault();
        const formData = new FormData(form);
        const data = {};

        formData.forEach((value, key) => {
            if (!data.hasOwnProperty(key)) {
                data[key] = value;
            } else if (Array.isArray(data[key])) {
                data[key].push(value);
            } else {
                data[key] = [data[key], value];
            }
        });

        fetch('/publishers/create_news/', {
            method: 'POST',
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Перенаправление на страницу новости или обновление страницы
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});


//

document.addEventListener('DOMContentLoaded', function() {
    let form = document.getElementById('commentForm');
    let textEditor = document.getElementById('textEditor');
    let boldButton = document.getElementById('boldButton');
    let italicButton = document.getElementById('italicButton');
    let submitButton = document.getElementById('submitComment');

    function updateButtonStyles() {
        boldButton.classList.toggle('active', document.queryCommandState('bold'));
        italicButton.classList.toggle('active', document.queryCommandState('italic'));
    }

    function toggleStyle(command) {
        document.execCommand(command, false, null);
        updateButtonStyles();
        textEditor.focus();
    }

    boldButton.addEventListener('click', function() { toggleStyle('bold'); });
    italicButton.addEventListener('click', function() { toggleStyle('italic'); });

    textEditor.addEventListener('keyup', updateButtonStyles);
    textEditor.addEventListener('mouseup', updateButtonStyles);
    textEditor.addEventListener('input', updateButtonStyles);

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        let formData = new FormData();
        formData.append('content', textEditor.innerHTML);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            },
            credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'ok') {
                let newComment = document.createElement('article');
                newComment.classList.add('comment');
                newComment.innerHTML = `
                    <div class="comment-avatar">
                        <img src="${data.authorAvatarUrl || 'path_to_default_avatar'}" alt="Avatar">
                    </div>
                    <div class="comment-body">
                        <header class="comment-header">
                            <h3 class="comment-author">${data.author}</h3>
                            <time class="comment-time">${data.created_at}</time>
                        </header>
                        <p class="comment-content">${data.content}</p>
                    </div>
                `;

                let commentsList = document.querySelector('.comment-list');
                commentsList.insertBefore(newComment, commentsList.firstChild);

                textEditor.innerHTML = '';
                updateButtonStyles();

                let commentsCountElement = document.getElementById('comments-count');
                let currentCount = parseInt(commentsCountElement.textContent, 10) || 0;
                commentsCountElement.textContent = currentCount + 1;
            }
        })
        .catch(error => console.error('Error:', error));
    });

    function getCookie(name) {
        let cookieValue = null;
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
        return cookieValue;
    }

    // Слушатель изменений для сортировки комментариев
    document.getElementById('sortComments').addEventListener('change', function(e) {
        sortComments(e.target.value);
    });

    function sortComments(criteria) {
        const commentsList = document.querySelector('.comment-list');
        let comments = Array.from(commentsList.children);

        comments.sort((a, b) => {
            const timeA = parseInt(a.dataset.time, 10);
            const timeB = parseInt(b.dataset.time, 10);

            return criteria === 'newest' ? timeB - timeA : timeA - timeB;
        });

        // Очищаем и добавляем отсортированные комментарии обратно
        commentsList.innerHTML = '';
        comments.forEach(comment => commentsList.appendChild(comment));
    }
});






