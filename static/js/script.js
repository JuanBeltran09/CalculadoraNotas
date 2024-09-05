document.addEventListener('DOMContentLoaded', function () {
    const addNoteButton = document.getElementById('addNote');
    const notesContainer = document.getElementById('notesContainer');

    addNoteButton.addEventListener('click', function () {
        const noteField = `
            <div class="input-group mt-3 note-item">
                <span class="input-group-text">Nota</span>
                <input type="text" aria-label="Nota" class="form-control">
                <span class="input-group-text">Porcentaje</span>
                <input type="text" aria-label="Porcentaje" class="form-control">
                <button class="btn btn-danger removeNote" type="button">Quitar Nota</button>
            </div>`;

        notesContainer.insertAdjacentHTML('beforeend', noteField);

    });
    notesContainer.addEventListener('click', function (event) {
        if (event.target.classList.contains('removeNote')) {
            event.target.closest('.note-item').remove();
        }
    });
});
