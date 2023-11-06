
document.addEventListener("DOMContentLoaded", function() {
    const clearButton = document.getElementById("clear");
    if(clearButton){
        clearButton.addEventListener("click", function() {
            // Redirige a la página de búsqueda sin el parámetro de búsqueda
            window.location.href = "/search/";
        });
    }
});

