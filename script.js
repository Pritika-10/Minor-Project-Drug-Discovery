
document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            alert(data.message);
            document.getElementById('filter-section').style.display = 'block';
        } else {
            alert(data.message);
        }
    });
});

document.getElementById('filter-btn').addEventListener('click', function() {
    const threshold = document.getElementById('threshold').value;
    fetch('/filter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `threshold=${threshold}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            const tbody = document.querySelector('#results-table tbody');
            tbody.innerHTML = "";
            data.data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML = `<td>${row.Molecule}</td><td>${row.SMILES}</td><td>${row.Docking_Score}</td>`;
                tbody.appendChild(tr);
            });
        } else {
            alert(data.message);
        }
    });
});

document.getElementById('visualize-btn').addEventListener('click', function() {
    fetch('/visualize', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            const img = document.getElementById('molecule-img');
            img.src = data.image_url;
            img.style.display = 'block';
        } else {
            alert(data.message);
        }
    });
});

document.getElementById('download-btn').addEventListener('click', function() {
    window.location.href = '/download';
});
