const socket = io.connect();

document.getElementById('uploadBtn').addEventListener('click', () => {
    const image = document.getElementById('fileInput').files[0];
    const reader = new FileReader();
    reader.onload = () => {
        socket.emit('image_upload', { image: reader.result });
    };
    reader.readAsDataURL(image);
});

socket.on('dish_identified', data => {
    document.getElementById('dishName').innerText = `Dish: ${data.dish}`;
});
