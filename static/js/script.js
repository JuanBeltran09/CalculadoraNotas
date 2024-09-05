document.addEventListener('DOMContentLoaded', function () {
    const addNoteButton = document.getElementById('addNote');
    const notesContainer = document.getElementById('notesContainer');
    const form = document.querySelector('form');
    const errorMessage = document.createElement('div');
    errorMessage.style.color = 'red';
    notesContainer.insertAdjacentElement('afterend', errorMessage);

    addNoteButton.addEventListener('click', function () {
        const noteField = `
            <div class="input-group mt-3 note-item">
                <span class="input-group-text">Nota</span>
                <input type="text" aria-label="Nota" class="form-control nota-field" >
                <span class="input-group-text">Porcentaje</span>
                <input type="text" aria-label="Porcentaje" class="form-control porcentaje-field">
                <button class="btn btn-danger removeNote" type="button">Quitar Nota</button>
            </div>`;

        notesContainer.insertAdjacentHTML('beforeend', noteField);

    });
    notesContainer.addEventListener('click', function (event) {
        if (event.target.classList.contains('removeNote')) {
            event.target.closest('.note-item').remove();
            validatePercentageSum();
        }
    });
    notesContainer.addEventListener('input', function (event) {
        if (event.target.classList.contains('nota-field') || event.target.classList.contains('porcentaje-field')) {
            validateNumberInput(event);
        }
        if (event.target.classList.contains('porcentaje-field')) {
            validatePercentageSum();
        }
    });
    function validateNumberInput(event) {
        const value = event.target.value;
        if (isNaN(value) || value < 0 || value > 100) {
            event.target.value = '';  // Borra el valor si no es un número válido
            errorMessage.textContent = "Solo se pueden ingresar números entre 0 y 100.";
        } else {
            errorMessage.textContent = '';  // Limpia el mensaje de error si es correcto
        }
    }
    function validatePercentageSum() {
        const porcentajeFields = document.querySelectorAll('.porcentaje-field');
        let totalPercentage = 0;

        porcentajeFields.forEach(function (field) {
            totalPercentage += parseFloat(field.value) || 0;
        });

        if (totalPercentage > 100) {
            errorMessage.textContent = "La suma de los porcentajes no puede superar el 100%.";
        } else {
            errorMessage.textContent = '';
        }
    }
    form.addEventListener('submit', function (event) {
        const porcentajeFields = document.querySelectorAll('.porcentaje-field');
        let totalPercentage = 0;

        porcentajeFields.forEach(function (field) {
            totalPercentage += parseFloat(field.value) || 0;
        });

        if (totalPercentage !== 100) {
            event.preventDefault();  // Evita el envío del formulario
            errorMessage.textContent = "La suma total de los porcentajes debe ser exactamente 100%.";
        }
    });
});
