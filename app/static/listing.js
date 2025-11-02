document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("listingForm");
  const responseMsg = document.getElementById("responseMsg");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
      platform: document.getElementById("platform").value.trim(),
      name: document.getElementById("name").value.trim(),
      description: document.getElementById("description").value.trim(),
      price: parseFloat(document.getElementById("price").value),
      validity_days: parseInt(document.getElementById("validity").value),
      username: document.getElementById("username").value.trim(),
      password: document.getElementById("password").value.trim()
    };

    // Basic validation
    if (!formData.platform || !formData.name || !formData.price || !formData.username || !formData.password) {
      responseMsg.textContent = "⚠️ Please fill all required fields.";
      responseMsg.style.color = "#e57373";
      return;
    }

    responseMsg.textContent = "Submitting...";
    responseMsg.style.color = "#dcd4bb";

    try {
      const response = await fetch("/listings/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        responseMsg.textContent = "✅ Listing created successfully!";
        responseMsg.style.color = "#9ccc65";
        form.reset();

        // Optional: redirect to browse page after a short delay
        setTimeout(() => {
          window.location.href = "/browse";
        }, 1500);
      } else {
        const err = await response.json();
        responseMsg.textContent = `❌ Error: ${err.message || "Something went wrong."}`;
        responseMsg.style.color = "#e57373";
      }
    } catch (error) {
      console.error("Error submitting listing:", error);
      responseMsg.textContent = "❌ Failed to submit. Please try again.";
      responseMsg.style.color = "#e57373";
    }
  });
});
