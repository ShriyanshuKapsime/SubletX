document.addEventListener("DOMContentLoaded", () => {
  fetch("/profile")
    .then(res => res.json())
    .then(data => {
      if (data.error) {
        document.getElementById("userInfo").innerHTML = `<p>${data.error}</p>`;
        return;
      }

      const { user, listings, rentals } = data;

      // 🧍 Display user info
      document.getElementById("userInfo").innerHTML = `
        <p><strong>Username:</strong> ${user.username}</p>
        <p><strong>Email:</strong> ${user.email}</p>
        <p><strong>Role:</strong> ${user.role}</p>
        <p><strong>Phone:</strong> ${user.phone || 'N/A'}</p>
      `;

      // 📦 Display listings
      const listingsContainer = document.getElementById("myListings");
      if (listings.length === 0)
        listingsContainer.innerHTML = "<p>No listings yet.</p>";
      else
        listings.forEach(l => {
          const div = document.createElement("div");
          div.classList.add("profile-card");
          div.innerHTML = `
            <h3>${l.name}</h3>
            <p>₹${l.price} | ${l.validity_days} days</p>
          `;
          listingsContainer.appendChild(div);
        });

      // 💳 Display rentals
      const rentalsContainer = document.getElementById("myRentals");
      if (rentals.length === 0)
        rentalsContainer.innerHTML = "<p>No rentals yet.</p>";
      else
        rentals.forEach(r => {
          const div = document.createElement("div");
          div.classList.add("profile-card");
          div.innerHTML = `
            <h3>${r.listing_name}</h3>
            <p>Amount: ₹${r.amount} | Status: ${r.status}</p>
          `;
          rentalsContainer.appendChild(div);
        });
    })
    .catch(err => {
      console.error("Error loading profile:", err);
    });
});
