// Toggle dropdown visibility
function toggleDropdown() {
  const dropdown = document.getElementById("dropdownList");
  dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}

// Close dropdown on clicking outside
document.addEventListener("click", function (event) {
  const dropdown = document.getElementById("dealerDropdown");
  const list = document.getElementById("dropdownList");
  if (!dropdown.contains(event.target)) {
    list.style.display = "none";
  }
});

// Select dealer and update table
function selectDealer(dealerName) {
  const placeholder = document.getElementById("dropdownPlaceholder");
  placeholder.textContent = dealerName;

  document.getElementById("navbarTitle").textContent = "LEAD TRACKER";
  document.getElementById("pageTitle").textContent = dealerName;
  document.getElementById("tableTitle").textContent = dealerName;

  // Show table and hide loader
  document.getElementById("leadsTable").style.display = "table";
  document.getElementById("loadingContainer").style.display = "none";

  updateLeadsTable(dealerName);
}

// Reset the dealer selection to "Choose a dealer"
function resetSelection() {
  const placeholder = document.getElementById("dropdownPlaceholder");
  placeholder.textContent = "Choose a dealer";

  document.getElementById("pageTitle").textContent = "Lead Tracker";
  document.getElementById("tableTitle").textContent = "Dealer Dashboard";

  // Hide table and show loader
  document.getElementById("leadsTable").style.display = "none";
  document.getElementById("loadingContainer").style.display = "block";
}

// Update the table based on selected dealer
function updateLeadsTable(dealerName) {
  document.getElementById("dropdownList").style.display = "none";
  localStorage.setItem("selectedDealer", dealerName);


}

// Set username from URL params
const params = new URLSearchParams(window.location.search);
const username = params.get("username");
document.getElementById("username").textContent = username ? username : "Admin";


function updateLeadsTable(dealerName) {
  const rows = document.querySelectorAll("#leadsBody tr");

  rows.forEach(row => {
    const rowDealer = row.getAttribute("data-dealer");

    // Show only rows matching selected dealer
    if (dealerName === "All" || rowDealer === dealerName) {
      row.style.display = "";
    } else {
      row.style.display = "none";
    }
  });
}

localStorage.setItem("selectedDealer", dealerName);

// On load
document.addEventListener("DOMContentLoaded", () => {
  const savedDealer = localStorage.getItem("selectedDealer");
  const domain = window.location.hostname.toLowerCase();

  if (savedDealer) {
    selectDealer(savedDealer);
  } else if (domain.includes("brandmirchi")) {
    selectDealer("BrandMirchi");
  } else if (domain.includes("themcostudio")) {
    selectDealer("MCO-Studio");
  } else {
    resetSelection();
  }
});