<template>
  <div>
    <header
      class="myheader fixed-top d-flex justify-content-center align-items-center"
    >
      <h1>My Gallery</h1>
    </header>

    <main class="container mt-5 pt-5">
      <div class="row">
        <div v-for="n in numberOfItems" :key="n" class="col-sm-6 col-md-4">
          <div class="card">
            <img
              src="@/assets/sample.png"
              class="card-img-top"
              alt="card-img"
            />
            <div class="card-body">
              <h5 class="card-title">Card {{ n }}</h5>
              <p class="card-text">This is a sample card description.</p>
              <button class="btn btn-primary">Go somewhere</button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref } from "vue";
const numberOfItems = ref(4);
</script>

<style scoped>
.myheader {
  color: white;
  background-color: rgb(255, 0, 0);
  padding: 10px;
}
</style>
