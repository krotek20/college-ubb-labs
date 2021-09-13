document.addEventListener('DOMContentLoaded', function() {
    const backButton = document.getElementById('back');
    const nextButton = document.getElementById('next');
    const list = document.getElementById('list');
    const listSize = list.children.length;
    let current = 0;
    let interval;

    function move() {
        list.style.left = `-${current * 400}px`;
    }

    function moveBack() {
        current = (current + listSize - 1) % listSize;
        move();
    }

    function moveNext() {
        current = (current + listSize + 1) % listSize;
        move();
    }

    function createInterval() {
        if (interval) {
            clearInterval(interval);
        }
        interval = setInterval(moveNext, 3000);
    }

    createInterval();

    backButton.addEventListener('click', function () {
        moveBack();
        createInterval();
    });

    nextButton.addEventListener('click', function () {
        moveNext();
        createInterval();
    });
});