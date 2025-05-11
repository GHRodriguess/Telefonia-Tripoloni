document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            const btn = document.querySelector('.button_close');
            if (btn) {
                btn.click();
            } else {
                console.log("Botão não encontrado.");
            }
        }
    });
});