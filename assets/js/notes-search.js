(function () {
  const box = document.querySelector('.notes-search');
  if (!box) return;
  const input = document.getElementById('notes-query');
  const rows = Array.from(document.querySelectorAll('.notes-item'));
  const normalize = text => text.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const texts = rows.map(row => normalize(row.dataset.search));
  function filter() {
    const words = normalize(input.value).trim().split(/\s+/).filter(Boolean);
    let count = 0;
    rows.forEach((row, i) => {
      row.hidden = !words.every(word => texts[i].includes(word));
      if (!row.hidden) count++;
    });
    document.querySelectorAll('.notes-year-group').forEach(group => {
      group.hidden = !group.querySelector('.notes-item:not([hidden])');
    });
    document.querySelectorAll('.notes-years a').forEach(link => {
      link.hidden = document.querySelector(link.hash).parentElement.hidden;
    });
    document.getElementById('notes-results').textContent = count
      ? `${count} of ${rows.length} notes` : 'No matching notes. Try fewer words or clear the search.';
  }
  input.addEventListener('input', filter);
  document.getElementById('notes-clear').addEventListener('click', () => {
    input.value = ''; filter(); input.focus();
  });
  box.hidden = false;
  filter();
})();
