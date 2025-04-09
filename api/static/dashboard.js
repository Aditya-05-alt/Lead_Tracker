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
  // Set the selected dealer name in the placeholder
  const placeholder = document.getElementById("dropdownPlaceholder");
  placeholder.textContent = dealerName;

  // Update page title and heading
  document.getElementById("navbarTitle").textContent = "LEAD TRACKER"; // Static navbar title
  document.getElementById("pageTitle").textContent = dealerName; // Page title changes
  document.getElementById("tableTitle").textContent = dealerName; // Heading changes to dealer's name

  // Fetch leads for the selected dealer (this can be dynamic based on real data)
  updateLeadsTable(dealerName);

  // Close dropdown
  document.getElementById("dropdownList").style.display = "none";
}

// Reset the dealer selection to "Choose a dealer"
function resetSelection() {
  const placeholder = document.getElementById("dropdownPlaceholder");
  placeholder.textContent = "Choose a dealer";

  // Reset the page title and heading
  document.getElementById("pageTitle").textContent = "Lead Tracker";
  document.getElementById("tableTitle").textContent = "Dealer Dashboard";

  // Clear the table
  const leadsBody = document.getElementById("leadsBody");
  leadsBody.innerHTML = ""; // Clear previous data
}

// Update the table based on selected dealer
function updateLeadsTable(dealerName) {
  const leadsBody = document.getElementById("leadsBody");
  leadsBody.innerHTML = ""; // Clear previous data


}

// Set username from URL params
const params = new URLSearchParams(window.location.search);
const username = params.get("username");
document.getElementById("username").textContent = username ? username : "Guest";


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
  if (savedDealer) {
    selectDealer(savedDealer);
  }
});
