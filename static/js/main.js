const socket = io.connect();
document.getElementById('uploadBtn').addEventListener('click', () => {
    socket.emit('image_upload', { image: imageData });
});
socket.on('dish_identified', data => {
    document.getElementById('dishName').innerText = `Dish: ${data.dish}`;
});
