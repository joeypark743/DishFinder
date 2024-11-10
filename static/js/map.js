function initMap() {
    const userLocation = { lat: 37.7749, lng: -122.4194 };  // Example coordinates
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: userLocation,
    });

    // Fetch and plot restaurant markers
    fetch('/get_restaurants').then(response => response.json()).then(data => {
        data.restaurants.forEach(restaurant => {
            new google.maps.Marker({
                position: restaurant.location,
                map: map,
                title: restaurant.name,
            });
        });
    });
}
