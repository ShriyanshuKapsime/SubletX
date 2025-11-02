document.getElementById("listForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("platformName").value;
  const description = document.getElementById("description").value;
  const price = document.getElementById("price").value;
  const validity = document.getElementById("validity").value;
  const responseMsg = document.getElementById("responseMsg");

  const payload = {
    name,
    description,
    price: parseFloat(price),
    validity_days: parseInt(validity)
  };

  responseMsg.textContent = "Submitting...";
  responseMsg.style.color = "#cbb977";

  try {
    const res = await fetch("/listings/create", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      responseMsg.textContent = "Listing added successfully! ✅ Redirecting...";
      responseMsg.style.color = "#9ccc65";

      setTimeout(() => {
        window.location.href = "/browse";
      }, 1500);
    } else {
      const data = await res.json();
      responseMsg.textContent = data.error || "Error adding listing ❌";
      responseMsg.style.color = "#e57373";
    }
  } catch (err) {
    console.error(err);
    responseMsg.textContent = "Server error ❌";
    responseMsg.style.color = "#e57373";
  }
});
