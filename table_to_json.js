const headers = Array.from(table.querySelectorAll("thead th span")).map(head => head.innerText.trim());
const jsonData = Array.from(table.querySelectorAll("tbody tr")).map(row => {
  const cells = Array.from(row.querySelectorAll("td"));
  let obj = {};
  cells.forEach((cell, i) => {
    obj[headers[i]] = cell.innerText.trim();
  });
  return obj;
})
const jsonString = JSON.stringify(jsonData, null, 2);
const blob = new Blob([jsonString], { type: 'application/json' });
const url = URL.createObjectURL(blob);

window.open(url, '_blank');