console.log("main.js loaded");

document.addEventListener('DOMContentLoaded', function() {
    // Modal logic
    const modal = document.getElementById('produitModal');
    const closeModal = document.getElementById('closeModal');
    const form = document.getElementById('editProduitForm');
    let currentId = null;

    document.querySelectorAll('.row-clickable').forEach(row => {
        row.addEventListener('click', function(e) {
            console.log(this.dataset)
            if (e.target.classList.contains('btn-delete')) return;
            currentId = this.dataset.id;
            document.getElementById('modalProduitId').value = this.dataset.id;
            document.getElementById('modalNom').value = this.dataset.nom;
            document.getElementById('modalPrix').value = this.dataset.prix;
            document.getElementById('modalDate').value = this.dataset.date;
            modal.style.display = 'block';
        });
    });

    closeModal.onclick = function() {
        modal.style.display = 'none';
    };
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };

    // Submit edit form via POST
    form.onsubmit = function(e) {
        e.preventDefault();
        const id = document.getElementById('modalProduitId').value;
        const nom = document.getElementById('modalNom').value;
        const prix = document.getElementById('modalPrix').value;
        const date = document.getElementById('modalDate').value;
        fetch(`/produits/edit/${id}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `nom=${encodeURIComponent(nom)}&prix=${encodeURIComponent(prix)}&date_peremption=${encodeURIComponent(date)}`
        }).then(response => {
            if (response.ok) {
                window.location.reload();
            } else {
                alert('Erreur lors de la modification.');
            }
        });
    };
});