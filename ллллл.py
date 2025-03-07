<!DOCTYPE html>
<html>
<head>
<title>Кнопка</title>
<style>
#myImage {
  display: none; /* Сначала скрыто */
  width: 300px;
  height: auto;
}
</style>
</head>
<body>

<button id="myButton">Нажми меня</button>
<img id="myImage" src="your_image.jpg" alt="Другое изображение">

<script>
const button = document.getElementById('myButton');
const image = document.getElementById('myImage');

button.addEventListener('click', () => {
  image.style.display = 'block'; // Показать изображение
  button.style.display = 'none'; // Скрыть кнопку (необязательно)
});
</script>

</body>
</html>
