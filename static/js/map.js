function initMap() {
    // Default location set to Boston, Kenmore
    const defaultLocation = { lat: 42.3482, lng: -71.0951 }; // Coordinates for Boston, Kenmore

    // Check if Geolocation is supported
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                // User's actual location
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude
                };

                // Initialize map with user's location
                const map = new google.maps.Map(document.getElementById("map"), {
                    zoom: 12,
                    center: userLocation,
                });

                // Add marker for user's location
                new google.maps.Marker({
                    position: userLocation,
                    map: map,
                    title: "Your Location",
                });

                // Fetch and plot restaurant markers
                fetchRestaurants(map);
            },
            () => {
                // If permission is denied, use the default location (Boston, Kenmore)
                initializeMapWithDefaultLocation(defaultLocation);
            }
        );
    } else {
        // If Geolocation is not supported, use the default location
        initializeMapWithDefaultLocation(defaultLocation);
    }
}

// Initialize map with the default location if geolocation fails
function initializeMapWithDefaultLocation(location) {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: location,
    });

    // Add marker for the default location
    new google.maps.Marker({
        position: location,
        map: map,
        title: "Default Location (Boston, Kenmore)",
    });

    // Fetch and plot restaurant markers
    fetchRestaurants(map);
}

// Function to fetch and plot restaurant markers
function fetchRestaurants(map) {
    fetch('/get_restaurants')
        .then(response => response.json())
        .then(data => {
            data.restaurants.forEach(restaurant => {
                new google.maps.Marker({
                    position: { lat: restaurant.latitude, lng: restaurant.longitude },
                    map: map,
                    title: restaurant.name,
                });
            });
        });
}
