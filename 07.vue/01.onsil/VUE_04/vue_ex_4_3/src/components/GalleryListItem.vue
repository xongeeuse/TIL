<template>
  <div>
    <div class="card">
      <img src="@/assets/sample.png" class="card-img-top" alt="..." />
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </p>
        <GalleryListButton />
      </div>
    </div>
  </div>
</template>

<script setup>
import GalleryListButton from "@/components/GalleryListButton.vue";
// import { ref } from "vue";
// const numberOfItems = 4;
</script>

<style scoped></style>
