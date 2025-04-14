(function () {
    // ✅ Detect traffic source & medium
    function getSourceAndMedium(referrer, utms) {
        const source = utms.utm_source || (referrer.includes("google") ? "google" :
                         referrer.includes("facebook") ? "facebook" :
                         referrer.includes("instagram") ? "instagram" :
                         referrer.includes("bing") ? "bing" :
                         referrer.includes("youtube") ? "youtube" :
                         referrer.includes("rvtrader") ? "rvtrader.com" :
                         referrer !== "" ? new URL(referrer).hostname : "direct");

        const medium = utms.utm_medium || (
            utms.utm_campaign ? "cpc" :
            referrer === "" ? "direct" :
            source === "google" || source === "bing" ? "organic" :
            "referral"
        );

        return { source, medium };
    }

    // ✅ Extract UTM params
    function getUTMs() {
        const urlParams = new URLSearchParams(window.location.search);
        return {
            utm_source: urlParams.get("utm_source"),
            utm_medium: urlParams.get("utm_medium"),
            utm_campaign: urlParams.get("utm_campaign"),
            utm_term: urlParams.get("utm_term"),
            utm_content: urlParams.get("utm_content")
        };
    }

    // ✅ Attach event listeners
    function initFormTracking() {
        function attachListenersToForms() {
            const forms = document.querySelectorAll('form:not([data-tracked])');
            forms.forEach(form => {
                form.setAttribute('data-tracked', 'true');
                form.addEventListener('submit', function (event) {
                    event.preventDefault();
                    captureFormData(form);
                });
            });
            console.log(`📡 Tracking ${forms.length} new form(s)...`);
        }

        attachListenersToForms();
        new MutationObserver(attachListenersToForms).observe(document.body, { childList: true, subtree: true });
    }

    // ✅ Capture and send form data
    function captureFormData(form) {
        const formData = new FormData(form);
        const formDetails = {};
        formData.forEach((value, key) => {
            formDetails[key.toLowerCase()] = value;
        });

        form.querySelectorAll('input, textarea, select').forEach(element => {
            const key = element.name || element.id || element.placeholder || element.className;
            if (key && !formDetails[key.toLowerCase()]) {
                formDetails[key.toLowerCase()] = element.value || '';
            }
        });

        const normalized = Object.fromEntries(Object.entries(formDetails).map(([k, v]) => [k.replace(/[-_]/g, '').toLowerCase(), v]));

        const name = normalized.name || normalized.yourname || '';
        const email = normalized.email || normalized.youremail || '';
        const phone = normalized.phone || normalized.yourphone || '';
        const subject = normalized.subject || normalized.yoursubject || '';
        const message = normalized.message || normalized.comments || normalized.enquiry || '';

        // if (!email && !name) {
        //     console.warn("❌ No email/name found — skipping submission.");
        //     return;
        // }

        const utms = getUTMs();
        const referrer = document.referrer || 'direct';
        const { source, medium } = getSourceAndMedium(referrer, utms);
        const pageLink = window.location.href;
        const formTitle = form.getAttribute("data-title") || form.getAttribute("name") || form.getAttribute("id") || form.querySelector("h1, h2, legend")?.innerText || "Unknown Form";

        console.log("📤 Sending to API", { name, email, phone, subject, message, source, medium, pageLink, formTitle });

        fetch("https://leadtracker-production.up.railway.app/leads/create/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                name, email, phone, subject, message,
                source, medium,
                page_link: pageLink,
                form_title: formTitle
            }),
        })
        .then(res => res.json())
        .then(data => {
            console.log("✅ Lead saved:", data);
            if (data.message) form.reset();
        })
        .catch(err => {
            console.error("❌ Error posting lead", err);
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initFormTracking);
    } else {
        initFormTracking();
    }
})();
