document.addEventListener("DOMContentLoaded", () => {
    // Load properties on the listings page
    const propertyList = document.getElementById("property-list");
    if (propertyList) {
        fetch('/api/properties')
            .then(res => res.json())
            .then(properties => {
                properties.forEach(property => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        <h3>${property.title}</h3>
                        <p>${property.description}</p>
                        <p><strong>Price:</strong> $${property.price}</p>
                    `;
                    propertyList.appendChild(li);
                });
            })
            .catch(err => console.error("Error fetching properties:", err));
    }

    // Load recommendations on the recommendations page
    const recommendationList = document.getElementById("recommendation-list");
    if (recommendationList) {
        fetch('/recommendations', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: 1 })
        })
        .then(res => res.json())
        .then(recommendations => {
            recommendations.forEach(recommendation => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <h3>${recommendation.title}</h3>
                    <p>${recommendation.description}</p>
                    <p><strong>Price:</strong> $${recommendation.price}</p>
                `;
                recommendationList.appendChild(li);
            });
        })
        .catch(err => console.error("Error fetching recommendations:", err));
    }
});
