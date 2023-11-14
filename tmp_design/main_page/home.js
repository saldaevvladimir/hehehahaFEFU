const popup = document.getElementById('popup')

function openPopup() {
	popup.classList.add('open');
}

function closePopup() {
	popup.classList.remove('open');
	popup.classList.add('close');

	// Добавляем обработчик события transitionend для удаления класса 'close' после завершения анимации
	popup.addEventListener('transitionend', function () {
		popup.classList.remove('close');
	}, { once: true });
}