<template>
  <card>
    <div class="singer-detail">
      <h2>가수 이름</h2>
      <img
        src="@/assets/singer.jpg"
        alt="singer-img"
        width="150"
        style="border-radius: 50%; object-fit: cover"
      />
      <p>가수 소개글</p>
      <SingerAlbum />
    </div>
  </card>
</template>

<script setup>
import SingerAlbum from "@/components/singers/SingerAlbum.vue";
</script>

<style scoped>
.singer-detail {
  border: solid black 1px;
  text-align: center;
}
card {
  display: inline-block;
  width: 40%;
  margin: 20px;
  /* background-color: black;
  color: white; */
}
</style>

<style>
/* h1 {
  color: green;
} */
</style>
