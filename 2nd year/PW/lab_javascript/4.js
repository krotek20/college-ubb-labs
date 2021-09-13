document.addEventListener('DOMContentLoaded', function() {
    const table1 = document.getElementById('table1');
    const headers1 = table1.querySelectorAll('th');
    const tableBody1 = table1.querySelector('tbody');
    const rows1 = tableBody1.querySelectorAll('tr');

    const table2 = document.getElementById('table2');
    const headers2 = table2.querySelectorAll('th');
    const tableBody2 = table2.querySelector('tbody');
    const rows2 = tableBody2.querySelectorAll('tr');

    const directions1 = Array.from(headers1).map(function(header) {
        return '';
    });

    const directions2 = Array.from(headers2).map(function(header) {
        return '';
    });

    const sortColumn = function(index, rows, directions, tableBody) {
        const direction = directions[index] || 'asc';
        const multiplier = (direction === 'asc') ? 1 : -1;
        const newRows = Array.from(rows);

        newRows.sort(function(rowA, rowB) {
            const cellA = rowA.querySelectorAll('td')[index].innerHTML;
            const cellB = rowB.querySelectorAll('td')[index].innerHTML;

            switch (true) {
                case cellA > cellB: return multiplier;
                case cellA < cellB: return -1 * multiplier;
                case cellA === cellB: return 0;
            }
        });

        [].forEach.call(rows, function(row) {
            tableBody.removeChild(row);
        });

        directions[index] = direction === 'asc' ? 'desc' : 'asc';

        newRows.forEach(function(newRow) {
            tableBody.appendChild(newRow);
        });
    };

    [].forEach.call(headers1, function(header, index) {
        header.addEventListener('click', function() {
            sortColumn(index, rows1, directions1, tableBody1);
        });
    });

    [].forEach.call(headers2, function(header, index) {
        header.addEventListener('click', function() {
            sortColumn(index, rows2, directions2, tableBody2);
        });
    });
});