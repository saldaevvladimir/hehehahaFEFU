window.addEventListener('load', function () {
    //user text font size
    const userTextElement = document.getElementById('user-text');
    const initialText = userTextElement.textContent;
    var fontSize = 16;

    const textLength = initialText.length - 30;

    if (textLength <= 40) {
        fontSize = 52;
    } else if (textLength <= 85) {
        fontSize = 40;
    } else if (textLength <= 150) {
        fontSize = 30
    } else if (textLength <= 235) {
        fontSize = 24;
    } else if (textLength <= 360) {
        fontSize = 18;
    } else if (textLength <= 500) {
        fontSize = 16;
    } else {
        fontSize = 16;
        userTextElement.textContent = initialText.slice(0, 497) + '...';
    }
    
    userTextElement.style.fontSize = fontSize + 'px';

    // submit buttons sizes
    const likeSubmitBtn = document.getElementById('like');
    const dislikeSubmitBtn = document.getElementById('dislike');

    likeSubmitBtn.style.width = likeSubmitBtn.height + 'px';
    dislikeSubmitBtn.style.width = dislikeSubmitBtn.height + 'px';
});
