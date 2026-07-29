const state = {
  resources: [],
  query: "",
  category: "all"
};

const grid = document.querySelector("#resource-grid");
const emptyState = document.querySelector("#empty-state");
const searchInput = document.querySelector("#resource-search");
const summary = document.querySelector("#result-summary");
const count = document.querySelector("#resource-count");

function normalize(value = "") {
  return value.toLowerCase().trim();
}

function matches(resource) {
  const categoryMatch =
    state.category === "all" || resource.category === state.category;

  const haystack = normalize([
    resource.name,
    resource.description,
    resource.category,
    resource.keywords.join(" ")
  ].join(" "));

  return categoryMatch && haystack.includes(normalize(state.query));
}

function render() {
  const visible = state.resources.filter(matches);
  grid.innerHTML = "";

  for (const resource of visible) {
    const article = document.createElement("article");
    article.className = "resource-card";
    article.innerHTML = `
      <div class="card-top">
        <span class="category">${resource.category}</span>
        <span class="access-badge">${resource.access}</span>
      </div>
      <h3>${resource.name}</h3>
      <p>${resource.description}</p>
      <div class="card-footer">
        <span class="verified">Last verified: ${resource.lastVerified}</span>
        <a class="resource-link" href="${resource.url}"
          target="_blank" rel="noopener noreferrer">
          Open official resource <span aria-hidden="true">↗</span>
        </a>
      </div>
    `;
    grid.appendChild(article);
  }

  summary.textContent = `${visible.length} of ${state.resources.length} resources shown`;
  emptyState.hidden = visible.length !== 0;
}

async function loadResources() {
  try {
    const response = await fetch("data/resources.json");
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.resources = await response.json();
    count.textContent = state.resources.length;
    render();
  } catch (error) {
    grid.innerHTML = `
      <div class="empty-state">
        <h3>Resources could not be loaded</h3>
        <p>Check that <code>data/resources.json</code> exists and contains valid JSON.</p>
      </div>
    `;
    console.error(error);
  }
}

searchInput.addEventListener("input", (event) => {
  state.query = event.target.value;
  render();
});

document.querySelectorAll(".filter").forEach((button) => {
  button.addEventListener("click", () => {
    document.querySelectorAll(".filter").forEach((item) =>
      item.classList.remove("active")
    );
    button.classList.add("active");
    state.category = button.dataset.category;
    render();
  });
});

document.querySelectorAll("[data-query]").forEach((button) => {
  button.addEventListener("click", () => {
    state.query = button.dataset.query;
    searchInput.value = state.query;
    searchInput.focus();
    render();
    document.querySelector("#resources").scrollIntoView();
  });
});

loadResources();
