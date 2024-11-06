<template>
  <div>
    <div class="album-container">
      <h4>앨범 제목</h4>
      <p class="song-list">노래 목록 1</p>
      <p class="song-list">노래 목록 2</p>
      <p class="song-list">노래 목록 3</p>
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.album-container {
  background-color: lightgray;
  /* border: 1px solid black; */
  border-radius: 5%;
  width: 100px;
  padding: 5px;
  margin: 20px auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.song-list {
  color: orange;
}
</style>
