function search() {
    const word = document.getElementById("word").value;
    fetch(`http://localhost:5000/similar?word=${encodeURIComponent(word)}`)
      .then(response => response.json())
      .then(data => {
        const list = document.getElementById("results");
        list.innerHTML = "";
        if (data.results) {
          data.results.forEach(([word, score]) => {
            const li = document.createElement("li");
            li.textContent = `${word} (${score.toFixed(3)})`;
            list.appendChild(li);
          });
        } else {
          list.innerHTML = `<li>${data.error}</li>`;
        }
      });
  }