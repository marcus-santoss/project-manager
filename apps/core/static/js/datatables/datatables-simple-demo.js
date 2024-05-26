window.addEventListener('DOMContentLoaded', event => {
    const datatablesSimple = document.querySelector(".data-table");
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple,
            {
                paging: true,
                scrollCollapse: false,
            });
    }
});
