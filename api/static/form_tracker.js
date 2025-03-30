(function () {
    function captureFormData(form) {
        const formData = new FormData(form);
        const formDetails = {};

        // Convert FormData entries to a plain object
        formData.forEach((value, key) => {
            formDetails[key] = value;
        });

        // Also capture data by ID and Class if name attribute is not available
        form.querySelectorAll('input, textarea').forEach(element => {
            const key = element.name || element.id || element.className;
            if (key && !formDetails[key]) {  // Only add if not already captured
                formDetails[key] = element.value || '';
            }
        });

        console.log("Form Captured: ", formDetails);

        // Check if name or email is missing
        if (!formDetails.name && !formDetails.id_name && !formDetails.class_name) {
            console.error("Name field is missing. Please add a name attribute, id, or class.");
            alert("Name field is required. Please fill it out.");
            return;
        }

        if (!formDetails.email && !formDetails.id_email && !formDetails.class_email) {
            console.error("Email field is missing. Please add a name attribute, id, or class.");
            alert("Email field is required. Please fill it out.");
            return;
        }

        // Send data to your Django backend
        fetch("http://127.0.0.1:8000/leads/create/", {  
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(formDetails)
        })
        .then(response => response.json())
        .then(data => {
            console.log("Server Response: ", data);
            if (data.message) {
                alert("Lead Captured Successfully!");
            } else {
                alert("Error: " + data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function handleFormSubmit(event) {
        event.preventDefault();
        const form = event.target;
        captureFormData(form);
    }

    document.addEventListener('DOMContentLoaded', () => {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => form.addEventListener('submit', handleFormSubmit));
        console.log(`Tracking ${forms.length} form(s) on this website.`);
    });
})();
