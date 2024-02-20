//AUTH
document.addEventListener('DOMContentLoaded', function() {

    // Регистрация пользователя
    var registrationForm = document.getElementById('registrationForm');
    registrationForm.onsubmit = function(e) {
        e.preventDefault();
        var formData = new FormData(registrationForm);
        fetch('/register/', { // URL регистрации
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken') // CSRF токен
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Обработка успешной регистрации
                alert('Регистрация прошла успешно.');
                window.location.href = '/login/'; // Переадресация на страницу входа
            } else {
                // Обработка ошибок регистрации
                alert('Ошибка регистрации: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    };

    // Авторизация пользователя
    var loginForm = document.getElementById('loginForm');
    loginForm.onsubmit = function(e) {
        e.preventDefault();
        var formData = new FormData(loginForm);
        fetch('/login/', { // URL авторизации
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken') // CSRF токен
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Обработка успешного входа
                alert('Вход выполнен успешно.');
                window.location.href = '/'; // Переадресация на главную страницу
            } else {
                // Обработка ошибок входа
                alert('Ошибка входа: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    };

    // Восстановление пароля (примерный код, дополните согласно вашей логике)
    var forgotPasswordForm = document.getElementById('forgotPasswordForm');
    forgotPasswordForm.onsubmit = function(e) {
        e.preventDefault();
        var formData = new FormData(forgotPasswordForm);
        // Здесь должен быть AJAX-запрос к вашему URL для восстановления пароля
        // ...
    };

    // Получаем модальные окна
    var loginModal = document.getElementById('loginModal');
    var registrationModal = document.getElementById('registrationModal');
    var forgotPasswordModal = document.getElementById('forgotPasswordModal');

    // Получаем кнопки для открытия модальных окон
    var loginBtn = document.getElementById('login');
    var registrationBtn = document.getElementById('registration');

    // Получаем элементы <span>, которые закрывают модальные окна
    var spans = document.getElementsByClassName('close');

    // Ссылки для переключения между модальными окнами
    var showLoginLink = document.getElementById('showLogin');
    var showRegistrationLink = document.getElementById('showRegistration');
    var forgotPasswordLink = document.getElementById('forgotPasswordLink');
    var backToLoginLink = document.getElementById('backToLogin');

    // Функции для показа и скрытия модальных окон
    function showModal(modal) {
        modal.style.display = 'block';
    }

    function hideModal(modal) {
        modal.style.display = 'none';
    }

    function hideAllModals() {
        hideModal(loginModal);
        hideModal(registrationModal);
        hideModal(forgotPasswordModal);
    }

    // Обработчики событий для кнопок открытия модальных окон
    loginBtn.onclick = function() {
        hideAllModals();
        showModal(loginModal);
    }

    registrationBtn.onclick = function() {
        hideAllModals();
        showModal(registrationModal);
    }

    // Обработчики событий для элементов закрытия модальных окон
    for (var i = 0; i < spans.length; i++) {
        spans[i].onclick = function() {
            hideAllModals();
        }
    }

    // Обработчики событий для ссылок переключения модальных окон
    if (showLoginLink) {
        showLoginLink.onclick = function() {
            hideAllModals();
            showModal(loginModal);
        }
    }

    if (showRegistrationLink) {
        showRegistrationLink.onclick = function() {
            hideAllModals();
            showModal(registrationModal);
        }
    }

    if (forgotPasswordLink) {
        forgotPasswordLink.onclick = function() {
            hideAllModals();
            showModal(forgotPasswordModal);
        }
    }

    if (backToLoginLink) {
        backToLoginLink.onclick = function() {
            hideAllModals();
            showModal(loginModal);
        }
    }

    // Закрыть модальные окна при клике вне их области
    window.onclick = function(event) {
        if (event.target == loginModal) {
            hideModal(loginModal);
        } else if (event.target == registrationModal) {
            hideModal(registrationModal);
        } else if (event.target == forgotPasswordModal) {
            hideModal(forgotPasswordModal);
        }
    }
});



// Game_profile
const form = document.getElementById('game-profile-form');
form.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const actionUrl = this.getAttribute('data-action-url'); // Получаем URL
    fetch(actionUrl, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
    })
    .then(response => response.json())
    .then(data => {
        if (!data.error) {
            const gameProfilesList = document.getElementById('game-profiles-list');
            const newProfileItem = document.createElement('div');
            newProfileItem.classList.add('game-profile-item');
            newProfileItem.style.display = 'flex';
            newProfileItem.style.alignItems = 'center';
            newProfileItem.style.justifyContent = 'space-between';
            newProfileItem.id = `game-profile-${data.id}`;

            const span = document.createElement('span');
            span.style.flexGrow = 1;
            span.textContent = `${data.game_name}: ${data.character_name}`;
            newProfileItem.appendChild(span);

            const deleteButton = document.createElement('button');
            deleteButton.textContent = '✖';
            deleteButton.style.backgroundColor = '#ff4d4d';
            deleteButton.style.borderRadius = '50%';
            deleteButton.style.width = '30px';
            deleteButton.style.height = '30px';
            deleteButton.style.border = 'none';
            deleteButton.style.cursor = 'pointer';
            deleteButton.style.color = 'white';
            deleteButton.onclick = function() { deleteGameProfile(data.id); };
            newProfileItem.appendChild(deleteButton);

            gameProfilesList.appendChild(newProfileItem);
        } else {
            alert(data.error);
        }
    })


    .catch((error) => {
        console.error('Error:', error);
    });
});



function deleteGameProfile(profileId) {
    fetch(`/Profile/delete_game_profile/${profileId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({'profile_id': profileId})
    })
    .then(response => {
        if (response.ok) {
            // Удаляем элемент из DOM
            document.getElementById(`game-profile-${profileId}`).remove();
        } else {
            console.error('Ошибка при удалении профиля');
        }
    })
    .catch(error => console.error('Error:', error));
}


//

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-profile-data'); // Убедитесь, что ID формы верный
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            // Используйте URL из action атрибута формы или укажите его явно
            const actionUrl = form.getAttribute('action');
            fetch(actionUrl, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    console.log('Profile updated successfully:', data);
                    // Опционально: Обновите DOM с новыми данными, если нужно
                } else {
                    alert('Error updating profile:', data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});


//

